from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
# Exercício 1
@app.route('/')
def index():
    return "<h1>Hello, Flask !!</h1>"

# Exercício 2
@app.route('/versao')
def versao():
    versao = "1.0.0"
    return f"App v{versao}"

# Exercício 3 
@app.route('/saudar/<nome>')
def saudar(nome):
    nome = nome.capitalize()
    return f"Olá, {nome}!"

# Exercício 4 
@app.route('/quadrado/<int:n>')
def quadrado(n):
    resultado = n ** 2
    return f"{n}² = {resultado}"

# Exercício 5 
@app.route('/home')
def home():
    return redirect(url_for('index')) 

# Exercício 6 - Página HTML via template
@app.route('/pagina')
def pagina():
    return render_template('pagina.html')

