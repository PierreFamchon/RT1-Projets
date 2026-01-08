#!/usr/bin/env bash
#!/usr/bin/env node

# proxy de l'iut
export http_proxy=cache-etu.univ-artois.fr:3128
export https_proxy=cache-etu.univ-artois.fr:3128

# téléchargement du fichier csv et extration du fichier
wget https://www.insee.fr/fr/statistiques/fichier/4768335/etatcivil2019_nais2019_csv.zip
unzip etatcivil2019_nais2019_csv.zip

# selection de la colonne qui nous intéresse
cut -d';' -f22 FD_NAIS_2019.csv > userdata.csv

# création du fichier json
touch userdata.json
python3 python.py

# suppression des fichiers inutiles
rm varmod_NAIS_2019.csv  
rm -r etatcivil2019_nais2019_csv.zip
rm FD_NAIS_2019.csv
rm userdata.csv

# attribution des droits d'exécution
chmod +x python.py
chmod 777 index.php
chmod 777 userdata.json

# organisation des fichiers
mkdir ~/public_html
cp index.php ~/public_html
mv userdata.json ~/public_html

username=$(whoami)
firefox http://172.31.25.9/~$username/


