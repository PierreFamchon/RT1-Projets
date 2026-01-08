from flask import Flask, render_template, request, redirect, session
import mysql.connector
import bcrypt

app = Flask(__name__)
app.secret_key = 'votre_secret_key'  # Vous pouvez définir votre propre clé secrète

# Configuration de la base de données
db_config = {
    'host': 'localhost',
    'database': 'asae23',
    'user': 'admin',
    'password': 'progtr00'
}

@app.route('/login', methods=['GET', 'POST']) 
def login(): 
    if request.method == 'POST': 
        username = request.form.get('username') 
        password = request.form.get('password').encode('utf-8')  # Encode le mot de passe en bytes
  
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor(dictionary=True)
            
            # Recherche de l'utilisateur dans la base de données
            query = "SELECT * FROM user WHERE nom = %s"
            cursor.execute(query, (username,))
            user = cursor.fetchone()
            cursor.close()
            conn.close()

            if user and bcrypt.checkpw(password, user['mot_de_passe'].encode('utf-8')):
                session['utilisateur_authentifie'] = True 
                return redirect('/')
            else: 
                return 'Identifiants invalides'

        except mysql.connector.Error as error:
            print('Erreur de connexion à la base de données:', error)
            return 'Erreur de connexion à la base de données'
  
    return render_template('login.html') 
    
@app.route('/register', methods=['POST'])
def register():
    nom = request.form.get('username')  # Utilisateur fournit son nom d'utilisateur
    mot_de_passe = request.form.get('password').encode('utf-8')  # Utilisateur fournit son mot de passe
    
    # Hachage du mot de passe
    hashed_password = bcrypt.hashpw(mot_de_passe, bcrypt.gensalt())

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insérer le nouvel utilisateur dans la base de données avec le mot de passe haché
        query = "INSERT INTO user (nom, mot_de_passe) VALUES (%s, %s)"
        cursor.execute(query, (nom, hashed_password))
        conn.commit()

        cursor.close()
        conn.close()

        return redirect('/login')

    except mysql.connector.Error as error:
        print('Erreur de connexion à la base de données:', error)
        return 'Erreur de connexion à la base de données'



@app.route('/logout')
def logout():
    session.pop('utilisateur_authentifie', None)
    return redirect('/')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect('/')

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Exécution de la requête SQL
        query = '''
        SELECT BC.nom AS bloc_nom, C.nom AS competence_nom, NA.nom AS niveau_nom 
        FROM BlocsCompetences BC
        JOIN Competences C ON C.bloc_id = BC.id
        JOIN CompetencesNiveaux CN ON CN.competence_id = C.id
        JOIN NiveauxAcquisition NA ON NA.id = CN.niveau_id
        ORDER BY BC.nom ASC, C.nom ASC;
        '''
        cursor.execute(query)

        # Récupération des résultats de la requête
        rows = cursor.fetchall()

        # Organiser les données dans des tableaux
        tableaux = {}
        for row in rows:
            bloc_nom = row[0]
            competence_nom = row[1]
            niveau_nom = row[2]

            if bloc_nom not in tableaux:
                tableaux[bloc_nom] = []

            tableaux[bloc_nom].append((competence_nom, niveau_nom))

        # Fermeture de la connexion à la base de données
        cursor.close()
        conn.close()

        # Rendu de la page HTML avec les résultats
        return render_template('index.html', tableaux=tableaux)

    except mysql.connector.Error as error:
        # Gestion des erreurs de connexion à la base de données
        print('Erreur de connexion à la base de données:', error)
        return 'Erreur de connexion à la base de données'

@app.route('/ajouter_competence', methods=['GET', 'POST'])
def ajouter_competence():
   if request.method == 'POST':
       try:
           conn = mysql.connector.connect(**db_config)
           cursor = conn.cursor()

           competence_nom = request.form['nom_competence']
           niveau_id = request.form['niveau_competence']
           bloc_id = request.form['bloc_competence']

           # Insertion de la compétence avec le bloc_id
           query = "INSERT INTO Competences (nom, bloc_id) VALUES (%s, %s)"
           cursor.execute(query, (competence_nom, bloc_id))
           competence_id = cursor.lastrowid  # Récupération de l'ID de la compétence insérée


           # Insertion du niveau de compétence
           query = "INSERT INTO CompetencesNiveaux (competence_id, niveau_id) VALUES (%s, %s)"
           cursor.execute(query, (competence_id, niveau_id))
           conn.commit()

           cursor.close()
           conn.close()

           return redirect('/login')


       except mysql.connector.Error as error:
           print('Erreur de connexion à la base de données:', error)
           return 'Erreur de connexion à la base de données'
   else:
       try:
           conn = mysql.connector.connect(**db_config)
           cursor = conn.cursor(dictionary=True)


           query = "SELECT id, nom FROM BlocsCompetences"
           cursor.execute(query)
           blocs = cursor.fetchall()

           cursor.close()
           conn.close()

           return render_template('ajouter_competence.html', blocs=blocs)

       except mysql.connector.Error as error:
           print('Erreur de connexion à la base de données:', error)
           return 'Erreur de connexion à la base de données'
            
            
@app.route('/modifier_competence', methods=['GET', 'POST'])
def modifier_competence():

    if request.method == 'GET':
        # Récupérez la liste des blocs de compétences depuis la base de données
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT id, nom FROM BlocsCompetences")
        blocs = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('modifier_competence.html', blocs=blocs)
    elif request.method == 'POST':
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            competence_id = request.form['competence_id']
            competence_nom = request.form['nom_competence']
            nouveau_niveau = request.form['nouveau_niveau']

            # Mettre à jour le nom de la compétence
            query = "UPDATE Competences SET nom = %s WHERE id = %s"
            cursor.execute(query, (competence_nom, competence_id))

            # Récupération de l'ID du niveau d'acquisition
            query = "SELECT id FROM NiveauxAcquisition WHERE nom = %s"
            cursor.execute(query, (nouveau_niveau,))
            result = cursor.fetchone()

            if result is None:
                # Niveau d'acquisition non trouvé
                return "Niveau d'acquisition non trouvé", 400

            niveau_id = result[0]

            # Mise à jour de la relation Competence - NiveauAcquisition
            query = "UPDATE CompetencesNiveaux SET niveau_id = %s WHERE competence_id = %s"
            cursor.execute(query, (niveau_id, competence_id))
            conn.commit()

            cursor.close()
            conn.close()

            return redirect('/login')

        except mysql.connector.Error as error:
            print('Erreur de connexion à la base de données:', error)
            return 'Erreur de connexion à la base de données'

@app.route('/supprimer_competence', methods=['GET', 'POST'])
def supprimer_competence():
    if request.method == 'GET':
        return render_template('supprimer_competence.html')

    if request.method == 'POST':
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            competence_id = request.form['competence_id']

            # Suppression de la compétence
            query = "DELETE FROM Competences WHERE id = %s"
            cursor.execute(query, (competence_id,))
            conn.commit()

            cursor.close()
            conn.close()

            return redirect('/login')

        except mysql.connector.Error as error:
            # Gestion des erreurs de connexion à la base de données
            print('Erreur de connexion à la base de données:', error)
            return 'Erreur de connexion à la base de données'

if __name__ == '__main__':
    app.run(debug=True)

