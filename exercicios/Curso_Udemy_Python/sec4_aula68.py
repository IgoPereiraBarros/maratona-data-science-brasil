import unittest

#classe principal a ser testada
class ConverterNumerosRomano:

	def __init__(self, numero_romano):
		self.numero_romano = numero_romano
		self.digito_map = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

	def converter_decimal(self):
		val = 0
		for char in self.numero_romano:
			val += self.digito_map[char]
		return val


class TestConverterNumerosRomano(unittest.TestCase):

	def test_mil(self):
		value = ConverterNumerosRomano('M')
		self.assertEqual(1000, value.converter_decimal(), 'Erro Inesperado')

	def test_quinhentos(self):
		value = ConverterNumerosRomano('D')
		self.assertEqual(500, value.converter_decimal(), 'Erro Inesperado')

	def test_dez(self):
		value = ConverterNumerosRomano('X')
		self.assertEqual(10, value.converter_decimal(), 'Erro Inesperado')

	def test_vazio(self):
		value = ConverterNumerosRomano('')
		self.assertTrue(value.converter_decimal() == 0)
		self.assertFalse(value.converter_decimal() > 0)


if __name__ == '__main__':
	unittest.main()


