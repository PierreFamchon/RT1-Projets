import redis
from flask import Flask ,render_template
import mysql.connector as MC
import json

app = Flask(__name__)
cache = redis.Redis(host='redis',port=6379)

def sql():
	conn = MC.connect(host= 'db', port = 3306, database = 'sae23', user = 'theo', password = 'progtr00')
# création du cursor
	cursor = conn.cursor()
# création de notre requête
	req = 'SELECT idlis, AC, UE.nomUE,Etat from AC INNER JOIN UE using(Numéro_UE);'
# lancement de la requête
	cursor.execute(req)
	results = cursor.fetchall()
	return(results)

@app.route('/')
def home():
    foin=sql()
    data = 0;
    with open("profil.json", 'r') as f:
        data = json.load(f)
    return render_template("index.html",data=data, foin=foin)
    
