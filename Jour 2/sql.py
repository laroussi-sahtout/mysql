import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages')
import mysql.connector


host = "localhost"
user = "root"
password = "123456789"
database = "LaPlateforme"


connexion = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

curseur = connexion.cursor()


requete_sql = "SELECT * FROM etudiant"
curseur.execute(requete_sql)

resultats = curseur.fetchall()


for resultat in resultats:
    print(resultat)


curseur.close()
connexion.close()


        
  
