'''
	Se um objeto anda como um pato  e faz quack então ele é um pato

	Programe para INTERFACES  e não para uma IMPREMENTAÇÃO
'''

class Pato:

	def quack(self):
		print('quack, quack!')

class Pessoa:

	def quack(self):
		print('QUACK!')

def pato_pessoa(obj):
	obj.quack()


pato_pessoa(Pato())
pato_pessoa(Pessoa())