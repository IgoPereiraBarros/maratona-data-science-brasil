import unittest
from sec4_aula72_1 import Calculadora

class TddExemplo(unittest.TestCase):

	def test_soma(self):

		calc = Calculadora()
		result = calc.somar(10, 21)
		self.assertEqual(-11, result)




if __name__ == '__main__':
	unittest.main()