import unittest
import sys

#classe principal a ser testada
class ConverterNumerosRomano:

	def __init__(self):
		self.digito_map = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

	def converter_decimal(self, numero_romano):
		val = 0
		for char in numero_romano:
			val += self.digito_map[char]
		return val


class TestConverterNumerosRomano(unittest.TestCase):

	def setUp(self):
		#print('Contruir o objeto da class ConverterNumerosRomano')
		self.cnr = ConverterNumerosRomano()

	def tearDown(self):
		#print('Destruir o objeto da class ConverterNumerosRomano')
		self.cnr = None

	@unittest.skipIf(sys.version_info > (2,7), 'Não suporta versões superiores a python 2.7')
	def test_mil(self):
		self.assertEqual(1000, self.cnr.converter_decimal('M'))

	def test_quinhentos(self):
		self.assertEqual(500, self.cnr.converter_decimal('D'))

	def test_dez(self):
		self.assertEqual(10, self.cnr.converter_decimal('X'))

	def test_vazio(self):
		self.assertTrue(self.cnr.converter_decimal('') == 0)
		self.assertFalse(self.cnr.converter_decimal('') > 0)


if __name__ == '__main__':
	unittest.main()
