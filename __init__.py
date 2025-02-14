from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)

@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"

@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
  resultat = valeur1 + valeur2
  if resultat % 2 == 0:
        parite = "pair"
  else:
        parite = "impair"
  return f"<h2>La somme de {valeur1} et {valeur2} est : {resultat} ==> est donc{parite})</h2>"
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')
  
@app.route('/cnam/')
def cnam():
    return render_template('cnam.html')
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
