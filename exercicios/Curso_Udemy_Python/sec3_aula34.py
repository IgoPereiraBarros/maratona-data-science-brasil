from math import pi as PI

class Forma:

	def __init__(self):
		print('Inicialização da forma')

	def area(self):
		print('Área da forma')

	def perimetro(self):
		print('Perimetro da forma')

	def descricao(self):
		print('Descrição da forma')

class Quadrado(Forma):
	''' Classe da forma do Quadrado'''
	def __init__(self, lado):
		self.lado = lado

	def area(self):
		return self.lado ** 2

	def perimetro(self):
		return self.lado * 4

	def descricao(self):
		return 'Quadrado'

class Circulo(Forma):
	''' Classe da forma do Circulo'''
	def __init__(self, raio):
		self.raio = raio

	def area(self):
		return self.raio ** 2 * PI

	def perimetro(self):
		return 2 * PI * self.raio

	def descricao(self):
		return 'Circulo'



q = Quadrado(10)
print('Área do Quadrado: %.2f' % q.area())
print('Perímetro do Quadrado: {:.2f}'.format(q.perimetro()))
print(q.descricao())



cir  = Circulo(3)

print('\nÁrea do Circulo: %.2f' % cir.area())
print('Perímetro do Circulo: {:.2f}'.format(cir.perimetro()))
print(cir.descricao())