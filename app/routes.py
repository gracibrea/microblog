from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = "Cláudia"
    sobrenome = "Brea"
    naturalidade = "Curitiba"
    dados = {"estudando": "Python + Flask", "professora": "Alba Lopes", "canal": "Profa. Alba Lopes"}
    return render_template('index.html', nome = nome, sobrenome = sobrenome, naturalidade = naturalidade, dados = dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')