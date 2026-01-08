# Importation des bibliothèques nécessaires
import csv 
import json 
import os

def csv_to_json(csvFilePath, jsonFilePath):
    """
    Fonction qui prend en entrée les chemins d'accès des fichiers CSV et JSON et effectue la conversion.
    """
    deces_compteur = {}  				# Création d'un dictionnaire pour stocker les comptages de deces par mois
    
    with open(csvFilePath, encoding='utf-8') as csvf:	# Ouverture du fichier CSV en mode lecture
        csvReader = csv.DictReader(csvf)		# Utilisation de DictReader pour convertir les lignes du fichier CSV en dictionnaires Python
        
        for row in csvReader:				# Boucle pour parcourir chaque ligne du fichier CSV convertie en dictionnaire Python
            month = row['MNAIS']			# Récupération de la valeur de la colonne "MNAIS" pour chaque ligne
            if month in deces_compteur:
                deces_compteur[month] += 1		# Incrémentation si le mois existe déjà dans le dictionnaire
            else:
                deces_compteur[month] = 1		# Ajout du mois au dictionnaire s'il n'existe pas encore

##########################################################################################################################################################################################################

    data = []							# Création d'une liste pour stocker les données converties au format JSON
    
    for month, count in deces_compteur.items():			# Boucle pour parcourir les entrées du dictionnaire deces_compteur
        month_int = int(month)  				# Conversion de la valeur de "month" en entier
        count_str = str(count)  				# Conversion de la valeur de "count" en chaîne de caractères
        data.append({"y": count, "x": month_int, "label": count_str})	# Ajout d'une entrée à la liste "data"

    data = sorted(data, key=lambda x: x["x"])			# Tri de la liste "data" selon la valeur de x

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:	# Ouverture du fichier JSON en mode écriture
        json.dump(data, jsonf, indent=2)			# Écriture des données de la liste "data" dans le fichier JSON avec une indentation de 2 espaces

##########################################################################################################################################################################################################

csvFilePath = r'userdata.csv'					# Chemins d'accès des fichiers CSV et JSON
jsonFilePath = r'userdata.json'

csv_to_json(csvFilePath, jsonFilePath)				# Appel de la fonction pour convertir le fichier CSV en JSON

php_script_path = os.path.join("/Documents/sae15", "index.php")	# Redirection vers la page PHP en utilisant le chemin absolu du fichier PHP
script_directory = os.path.dirname(os.path.abspath(__file__))	# Définition du répertoire de travail

os.chdir(script_directory)
os.system("php {}".format(php_script_path))			# Redirection vers la page PHP



