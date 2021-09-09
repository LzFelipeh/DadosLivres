from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():

    usuario = {"nome": "Dados Livres"}

    return render_template('index.html', usuario = usuario, titulo = 'Página inicial')

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo='DadosLivres - contato')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo='DadosLivres - sobre')