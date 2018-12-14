
'''class MinhaClasse(object):
	var = True

myClass = type('MinhaClasse', (), {'var': True})
print(myClass)'''

'''idade = 20
print(idade.__class__) # aqui me mostra a classe do objeto idade
print(idade.__class__.__class__) # aqui mostra a classe da classe(Meta Classe) do objeto idade'''

class MinhaMetaClasse(type):

	def __new__(cls, clsname, superclasses, attributedict):
		print('clsname: {}'.format(clsname))
		print('superclasses: {}'.format(superclasses))
		print('atributo: {}'.format(attributedict))

		return type.__new__(cls, clsname, superclasses, attributedict)

class Pai:
	pass

class Filha(Pai, metaclass=MinhaMetaClasse):
	pass

obj = Filha()

print(obj.__class__)
print(obj.__class__.__class__)
			