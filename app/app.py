from flask import Flask, render_template
#from data import *

app = Flask(__name__)

# esta ruta equivale al home a root
@app.route("/")
def pgHome():
    #return "<h1>Hello, World!</h1>"
    #saludo = "Hola Mundo"
    return render_template ("index.html")

# ruta a la parte de recetas
@app.route('/recetas')
def pgRecetas():
    return render_template ("recetas.html")

# ruta a la parte de nostrs
@app.route('/nosotros')
def pgNosotros():
    return render_template ("nosotros.html")

# ruta a la parte de contacto
@app.route('/contacto')
def pgContacto():
    return render_template ("contacto.html")