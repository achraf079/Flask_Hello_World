from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)

@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"

@app.route('/somme/', methods=['GET'])
def somme():
  try:    
    valeur1 = int(input("Veuillez saisir un nombre"))
    valeur2 = int(input("Veuillez saisir un nombre"))
  except ValueError:    
    print("Veuillez entrer un nombre entier valide.")
    
  return "<h2>Le carré de votre valeur est : </h2>" + str(valeur1 + valeur2)
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
