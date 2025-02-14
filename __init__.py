from flask import Flask, request
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
    valeur1 = int(request.args.get('valeur1'))
    valeur2 = int(request.args.get('valeur2'))
  except (ValueError, TypeError):
    return "<h2>Erreur : Veuillez entrer des nombres entiers valides.</h2>", 400
  return "<h2>Le carré de votre valeur est : </h2>" + str(valeur1 + valeur2)
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
