# dicionarios

'''d = dict()

d['igor'] = 21
d['dina'] = 50
d['luana'] = 18
d['afonso'] = 48

d1 = {'igor':21, 'afonso':48}

print(d1.get('igor'))
print(d1.keys())
print(d1.values())
print(d1.items())


for key, values in d1.items():
	print('Chaves {} e valores {}'.format(key, values))'''

class MyClass:

	def __init__(self, valor):
		self.valor = valor

obj = MyClass(1)
d = {}
d[obj] = 'luana'

obj2 = MyClass(2)
d[obj2] = 'Dina'

print(d[obj2])
