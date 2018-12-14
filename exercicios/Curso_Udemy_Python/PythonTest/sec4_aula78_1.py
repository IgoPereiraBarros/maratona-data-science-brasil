import unittest
from sec4_aula78 import Operacoes

class OperacoesTests(unittest.TestCase):

	def soma_test(self):
		op = Operacoes(10, 10)
		value = op.soma()
		self.assertEquals(20, value)

	def sub_test(self):
		op = Operacoes(10, 5)
		value = op.sub()
		self.asserEquals(5, value)

	def mult_test(self):
		op = Operacoes(10, 2)
		value = op.mult()
		self.asserEquals(20, value)

	def divisao_test(self):
		op = Operacoes(15, 5)
		value = op.divisao()
		self.asserEquals(3, value)

	def potencia_test(self):
		op = Operacoes(2, 6):
		value = op.potencia()
		self.asserEquals(64, value)

	def divisaoInteira_test(self):
		op = Operacoes(3, 10)
		value = op.divisaoInteira()
		self.assertEquals(3, value)


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(OperacoesTests)
	unittest.TextTestRunner(verbosity=2).run(suite)