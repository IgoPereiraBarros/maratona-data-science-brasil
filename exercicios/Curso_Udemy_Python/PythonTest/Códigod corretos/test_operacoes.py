import unittest

from operacoes import Operacoes

class OperacoesTest(unittest.TestCase):

	 def test_soma(self):
	 	op = Operacoes(10, 10)
	 	value = op.soma()
	 	self.assertEquals(20, value)

	 def test_subtracao(self):
	 	op = Operacoes(10, 10)
	 	value = op.subtracao()
	 	self.assertEquals(0, value)

	 def test_divisao(self):
	 	op = Operacoes(50, 10)
	 	value = op.divisao()
	 	self.assertEquals(5, value)

	 def test_multiplicacao(self):
	 	op = Operacoes(10, 10)
	 	value = op.multiplicacao()
	 	self.assertEquals(100, value)


	 def test_potencia(self):
	 	op = Operacoes(10, 2)
	 	value = op.potencia()
	 	self.assertEquals(100, value)	 		 		 	


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(OperacoesTest)
	unittest.TextTestRunner(verbosity=2).run(suite)