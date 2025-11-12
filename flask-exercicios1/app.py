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