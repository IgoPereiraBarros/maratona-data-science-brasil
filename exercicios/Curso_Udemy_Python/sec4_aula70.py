# F = F(n-1) + F(n-2)

import doctest

class fib:

	def calc_fib(self, n):

		"""
			Método para calcular o Fibonacci

			>>> f.calc_fib(10)
			55

			>>> f.calc_fib(5)
			5
		"""

		if n < 0:
			raise ValueError('N tem que ser maior que zero!')

		a, b = 0, 1
		for i in range(n):
			a, b = b, a + b
		return a

if __name__ == '__main__':
	doctest.testmod(extraglobs={'f':fib()})