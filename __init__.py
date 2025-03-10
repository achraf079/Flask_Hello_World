from flask import Flask, request
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)

@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"

@app.route('/somme/<path:valeurs>')
def somme(valeurs):
    valeurs_list = valeurs.split('/')
    total = 0
    for valeur in valeurs_list :
        total += int(valeur)
    if total % 2 == 0:
        parite = "pair"
    else:
        parite = "impair"
    valeurs_int = [int(valeur) for valeur in valeurs_list]
    valeurMax = max(valeurs_int)
    return f"<h2>La somme des valeurs : {valeurs_list } est : {total} ==> est donc {parite} <BR> | La valeur maximale : {valeurMax} </h2>"
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/etoiles/')
def etoiles():
    return render_template('carre_etoiles.html')
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
