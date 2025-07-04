from flask import Flask, request, redirect, url_for, render_template, make_response

app = Flask(__name__)

USUARIO_CADASTRADO = 'admin'
SENHA_CADASTRADA = '1234'

# Rota para a raiz do site: redireciona para /login
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('username')
        senha = request.form.get('password')

        if usuario == USUARIO_CADASTRADO and senha == SENHA_CADASTRADA:
            resposta = make_response(redirect(url_for('bemvindo')))
            resposta.set_cookie('username', usuario, max_age=60*10)  # inserindo valor no cookie (10 min)
            return resposta
        else:
            mensagem = "Usuário ou senha inválidos. Tente novamente."
            return render_template('login.html', error=mensagem)
    
    return render_template('login.html')


@app.route('/bemvindo')
def bemvindo():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
    return render_template('bemvindo.html', user=username)


@app.route('/logout')
def logout():
    resposta = make_response(redirect(url_for('login')))
    resposta.set_cookie('username', '', expires=0)  # deletar cookie
    return resposta


if __name__ == '__main__':
    app.run(debug=True)
