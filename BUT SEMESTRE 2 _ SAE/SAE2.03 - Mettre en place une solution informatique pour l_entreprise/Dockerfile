# Utiliser une image de base Python 3.8
FROM python:3.9-slim

# Mettre en place un répertoire de travail
WORKDIR /web

ENV http_proxy=http://cache-etu.univ-artois.fr:3128

ENV https_proxy=http://cache-etu.univ-artois.fr:3128

# Copier le fichier des dépendances et installer les dépendances
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install mysql-connector-python
RUN pip install flask
RUN pip install bcrypt


# Copier le reste du code de l'application
COPY . .

# Exposer le port sur lequel l'application sera exécutée
EXPOSE 5000

# Définir la variable d'environnement pour indiquer à Flask comment s'exécuter
ENV FLASK_APP=app.py

# Démarrer l'application
CMD ["flask", "run", "--host=0.0.0.0"]


