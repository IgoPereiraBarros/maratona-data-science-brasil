
def funcao1(*args):
	print(args)

funcao1(1,2,3,4, 'oi')

def funcao2(**kwargs):
	#print(kwargs)
	for k, v in kwargs.items():
		print(k, v)

funcao2(rua='José ovidio bona', numero='1428', bairro='cariri')