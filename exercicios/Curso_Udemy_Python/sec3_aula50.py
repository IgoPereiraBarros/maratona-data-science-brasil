
'''def algo():
	raise Exception('exceção')
	print('Depois do raise') # mesmo um print após o raise, ainda assim esse print não
							 # será executado...neste caso

try:
	algo()
except:
	print('Peguei uma exceção')
	print('Após a exceção')'''


def divisao(divisor):
	try:
		if divisor == 15:
			raise ValueError('Não gosto do 15')
		return 10 / divisor
	except ZeroDivisionError:
		return 'Erro ao dividir por zero(0)'
	except TypeError:
		return 'Apenas números'
	except ValueError:
		print('Não entre com o valor 15')
		raise
	#else:
		#print('Não ocorreu nenhuma exceção')
	finally:
		print('O finally sempre será executado')


print(divisao(12))
