from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from models import Jogo
from dao import JogoDao, UsuarioDao
import time
import os
from helpers import deleta_arquivo, recupera_imagem
from jogoteca import db, app

jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)

# Rota, caminho definido
@app.route('/')
def index():
    lista_jogos = jogo_dao.listar()
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
    jogo = jogo_dao.salvar(jogo)

    arquivo = request.files['arquivo'] #Acessando arquivo vindo do formulario
    upload_path = app.config['UPLOAD_PATH']

    timestamp = time.time()

    arquivo.save(f'{upload_path}/capa{jogo.get_id()}-{timestamp}.jpg')

    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        print("não logado")
        return redirect(url_for('login', proxima= url_for('editar')))
    jogo = jogo_dao.busca_por_id(id)
    #capa_jogo = f'capa{id}.jpg'

    nome_imagem = recupera_imagem(id)

    return render_template('editar.html',titulo='Editar Jogo', jogo=jogo, capa_jogo=nome_imagem)

@app.route('/atualizar',methods=['POST'])
def atualizar():
    # Pegando informações do request
    nome = request.form['nome']
    categoria = request.form['categoria']
    plataforma = request.form['console']
    id = request.form['id']
    jogo = Jogo(nome, categoria, plataforma, id)
    jogo_dao.salvar(jogo)

    arquivo = request.files['arquivo']  # Acessando arquivo vindo do formulario
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    deleta_arquivo(jogo.get_id())
    arquivo.save(f'{upload_path}/capa{jogo.get_id()}-{timestamp}.jpg')

    return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
    # Verificar se está logado
    jogo_dao.deletar(id)
    flash('O jogo foi removido com sucesso')
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima') # pegando argumentos passados pela requisição
    return render_template('/login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])

    if usuario:
        if usuario.get_senha() == request.form['senha']:
            session['usuario_logado'] = usuario.get_id()
            flash(usuario.get_nome() + ' logou com sucesso')
            proxima_pagina = request.form['proxima']
            # Se eu não vim de nenhuma pagina antes de login, eu devo ir para a pagina especifica
            return redirect(proxima_pagina)
    else:
        flash('Não logado, tente novamente!')
        return redirect(url_for('login'))


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))
