import sqlite3

class DataBase:

	''' Classe que representa o banco de dados (database) da aplicação '''
	def __init__(self, nome='database.db'):
		self.nome, self.connection = nome, None

	def connects(self):
		''' Conecta passando o nome do arquivo '''
		self.connection = sqlite3.connect(self.nome)

	def disconnect(self):
		''' Desconecta do banco '''
		try:
			self.connection.close()
		except AttributeError as a:
			print('Faça a conexão do banco de dados antes: {}'.format(a))

	def create_table(self):
		''' Cria a tabela do banco de dados '''
		try:
			cursor = self.connection.cursor()
			cursor.execute("""
					CREATE TABLE IF NOT EXISTS clientes(
						id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
						nome TEXT NOT NULL,
						senha VARCHAR(8) NOT NULL,
						cpf VARCHAR(11) UNIQUE NOT NULL,
						email TEXT NOT NULL
					);

				""")
		except AttributeError as a:
			print('Antes de criar uma tabela conecte ao banco de dados.\nErro: {}'.format(a))

	def insert_client(self, nome, senha, cpf, email):
		''' Insere dados na tabela '''
		try:
			cursor = self.connection.cursor()
			try:

				cursor.execute("""
						INSERT INTO clientes (nome, senha, cpf, email) VALUES (?,?,?,?)

					""", (nome, senha, cpf, email))
			except sqlite3.IntegrityError as si:
				print('O cpf <{}> já existe no banco de dados'.format(cpf))
				print('<Error>: {}'.format(si))

			self.connection.commit()
		except AttributeError as a:
			print('Antes de inserir dados na tabela conecte-se ao banco de dados.\nErro: {}'.format(a))

	def buscar_client(self, cpf):
		''' Buscar cliente pelo cpf '''
		try:
			cursor = self.connection.cursor()

			cursor.execute("""
					SELECT * FROM clientes WHERE cpf = ?
				""", ([cpf]))

			# Como o cpf é unico, basta buscar apenas uma única vez, ou seja, sempre buscará o primeiro resultado
			# por isso usamos fetchone()
			client = cursor.fetchone() # returna uma tupla

			if client:
				#print('Cliente {} encontrado com sucesso!'.format(client[1]))
				return True
			return False
			#else:
				#print('Cliente não encontrado, ou nunca existiu')

			'''cursor.execute("""
					SELECT * FROM clientes;
				""")

			for linha in cursor.fetchall():
				#linha[0] é a posição que está o ID
				#linha[1] nome do cliente...e assim por diante, 
				#porém queremos a linha do cpf que é a linha[2]
				if linha[2] == cpf:
					print('Cliente {} encontrado com sucesso!'.format(linha[1]))
					break
				else:
					continue
					print('Cliente não encontrado!')'''
		except AttributeError as a:
			print('Antes de buscar um cliente conecte-se ao banco de dados')
			print('Erro: {}'.format(a))

	def delete_client(self, cpf):
		''' Buscar client pelo cpf '''
		''' Precisando de algumas correções... '''
		try:
			cursor = self.connection.cursor()
			cli = self.buscar_client(cpf)

			cursor.execute(""" DELETE FROM clientes WHERE cpf = %s """ % str(cpf))
			self.connection.commit()

			if self.buscar_client(cpf) != 'None':
				print('O cliente  foi removido com sucesso!')
			else:
				print('O cpf {} não consta no banco de dados!'.format(cpf))
		except AttributeError as a:
			print('Antes de excluir um cliente faça conexão ao banco de dados')
			print('Erro: {}'.format(a))

	def buscar_email(self, email):
		''' Buscar cliente pelo email '''

		try:
			cursor = self.connection.cursor()
			cursor.execute("""
					SELECT * FROM clientes;
				""")
			self.connection.commit()

			clientes = cursor.fetchall()

			for linha in clientes:
				if linha[4] == email:
					print('Cliente {} encontrado com sucesso!'.format(linha[1]))
					break

		except AttributeError as a:
			print('Antes de fazer uma busca faça a conexão com o banco de dados')
			print('Erro: {}'.format(a))


	def login(self, username, password):
		try:
			cursor = self.connection.cursor()
			sql = 'SELECT * FROM clientes WHERE nome=? and senha=?'
			cliente = cursor.execute(sql, [username, password]).fetchone()
			if cliente:
				return True
			return False
		except AttributeError as a:
			print('Conecte ao banco de dados!')
