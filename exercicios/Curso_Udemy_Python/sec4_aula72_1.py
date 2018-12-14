class Calculadora(object):

	def somar(self, n1, n2):
		for i in range(n1, n2):
			if n1 and n2 % i == 0:
				return n1 + n2
			else:
				return n1 - n2
