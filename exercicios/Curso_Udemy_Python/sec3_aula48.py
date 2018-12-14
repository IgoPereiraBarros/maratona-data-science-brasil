
class SomenteInteiros(list):

	def append(self, inteiro):

		if not isinstance(inteiro, int):
			raise TypeError('Somente inteiros')
		if inteiro % 2:
			raise ValueError('Somente pares')


s = SomenteInteiros()
s.append(2)