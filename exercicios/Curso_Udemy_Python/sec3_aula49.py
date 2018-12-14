
'''def algo1():
	print('Antes da exceção')
	raise Exception('exceção do algo1')
	print('Depois da exceção')

algo1()'''

def algo1():
	print('Anterior a exceção')
	algo2()
	print('Após a exceção')

def algo2():
	raise Exception('exceção do algo2')

algo1()