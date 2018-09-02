from flask import Flask, render_template, request, redirect, session, flash, url_for
from jogo import Jogo
from usuario import Usuario

app = Flask(__name__)
app.secret_key = 'qgdostark'

user1 = Usuario("stark","Marcos","1234")
user2 = Usuario("paty","Patricia","4321")
user3 = Usuario("admin","admin","admin")

usuarios = {user1.get_id(): user1,
            user2.get_id(): user2,
            user3.get_id(): user3 }

jogo1 = Jogo("Super Mario","Ação","SNES")
jogo2 = Jogo("Pokemon GO!","RPG", "Mobile")
jogo3 = Jogo("League of Legends", "Moba","PC")
lista_jogos = [jogo1, jogo2, jogo3]

# Rota, caminho definido
@app.route('/')
def index():
    return render_template('lista.html',titulo='Minha lista de jogos', jogos=lista_jogos)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima= url_for('novo')))
    return render_template('novo.html',titulo='Novo Jogo')

@app.route('/criar',methods=['POST'])
def criar():
    #Pegando informações do request
    nome = request.form['nome']
    categoria = request.form['categoria']
    plataforma = request.form['console']

    jogo = Jogo(nome, categoria, plataforma)
    lista_jogos.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima') # pegando argumentos passados pela requisição
    return render_template('/login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():

    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]

        if usuario.get_senha() == request.form['senha']:
            session['usuario_logado'] = usuario.get_id()
            flash(usuario.get_nome() + ' logou com sucesso')
            proxima_pagina = request.form['proxima']
            # Se eu não vim de nenhuma pagina antes de login, eu devo ir para a pagina especifica
            return redirect(proxima_pagina)
    else:
        flash('Não logado, tente novamente!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))

# Definindo acesso externo e definido porta 8080
# Debug=True, detecta as alterações automaticamente, para não precisar restartar a aplicação
app.run(debug=True, host='0.0.0.0', port=8080)

