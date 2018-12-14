
class Operador():

''' Esta classe é apenas pra exemplificar a sobrecarga dos métodos __add__(soma), __mul__(mult)...'''
	def __init__(self, num):
		self.num = num

	def __add__(self, op):
		return self.num + op.num

	def __mul__(self, op):
		return self.num ** op.num

	def __sub__(self, op):
		return self.num / op.num

op = Operador(10)
op1 = Operador(3)

print(op - op1)