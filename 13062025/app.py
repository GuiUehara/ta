from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
@app.route("/")
def home():
    produtos = ["Maçã", "Banana", "Laranja"]
    logado = True
    return render_template("home.html", produtos = produtos, logado = logado)

app.secret_key = 'uma-chave-secreta-muito-segura-e-dificil-de-adivinhar'

@app.route('/login', methods = ['POST'])

def login():
    username = request.form['username']
    session['username'] = username
    return redirect(url_for('profile'))