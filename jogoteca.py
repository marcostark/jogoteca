from flask import Flask, render_template, request, redirect
from jogo import Jogo

app = Flask(__name__)

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
    return render_template('novo.html',titulo='Novo Jogo')

@app.route('/criar',methods=['POST'])
def criar():
    #Pegando informações do request
    nome = request.form['nome']
    categoria = request.form['categoria']
    plataforma = request.form['console']

    jogo = Jogo(nome, categoria, plataforma)
    lista_jogos.append(jogo)
    return redirect('/')

# Definindo acesso externo e definido porta 8080
# Debug=True, detecta as alterações automaticamente, para não precisar restartar a aplicação
app.run(debug=True, host='0.0.0.0', port=8080)

