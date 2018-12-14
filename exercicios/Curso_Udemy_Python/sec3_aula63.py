def algo():
	return 1 + 2

def is_prime(n):
	for i in range(3, n):
		if n % i == 0:
			return False
	return True

def get_primes(input_list):
	return (e for e in input_list if is_prime(e))


'''def gerar_numero():
	yield 1
	yield 2
	yield 3

for i in gerar_numero():
	print('{}'.format(i), end=' ')
try:

	nosso_gerador = gerar_numero()
	print(next(nosso_gerador))
	print(next(nosso_gerador))
	print(next(nosso_gerador))
except StopIteration as s:
	print('Erro: {}'.format(s))'''

def get_primes(init, fim):
	while init <= fim:
		if is_prime(init):
			yield init
		init += 1

meu_gera = get_primes(10, 103)

for i in meu_gera:
	print(i)

