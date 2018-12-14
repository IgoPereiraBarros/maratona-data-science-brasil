from app import app

from bottle import request, template
from bottle import static_file

'''@route('/')
@route('/user/<nome>')
def index(nome='null'):
	return '<center><h1>Eae ' + nome + ' </h1></center>'

@route('/artigo/<id>')
def index_artigo(id):
	return '<h2>Você está lendo o artigo ' + id + '</h2>'

@route('/pagina/<id>/<nome>')
def index_pagina(id, nome):
	return '<h1>Você está lendo a página ' + id + ' com o nome ' + nome + '</h1>'
'''

# static rotes
@app.get('/<filename:re:.*\.css>')
def stylesheets(filename):
	return static_file(filename, root='static/css')

@app.get('/<filename:re:.*\.js>')
def stylesheets(filename):
	return static_file(filename, root='static/js')

@app.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def stylesheets(filename):
	return static_file(filename, root='static/img')

@app.get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def stylesheets(filename):
	return static(filename, root='static/fonts')

@app.route('/') # @get('/login')
def login():
	return template('login')

@app.route('/cadastro')
def cadastro():
	return template('cadastro')

@app.route('/cadastro', method='POST')
def acao_cadastro():
	username = request.forms.get('username')
	password = request.forms.get('password')
	insert_user(username, password)
	return template('verificacao_cadastro', nome=username)


'''@route('/')
def indexHome():
	return template('index_home')
'''

@app.route('/', method='POST')
def acao_login(): # @post('/login')
	username = request.forms.get('username')
	password = request.forms.get('password')
	return template('verificacao_login', sucesso=True, nome=username) # ou sucesso=auth_login(username, password)

@app.error(404)
def error404(error):
	return template('pagina404')