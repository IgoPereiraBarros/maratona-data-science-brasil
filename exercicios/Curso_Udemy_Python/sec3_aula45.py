

class Pessoa:
	''' Definindo mais de um contrutor'''
	def __init__(self, nome):
		self.nome = nome

	@classmethod
	def op1_contrutor(cls, nome):
		return cls(nome)


p = Pessoa('Construtor 1')
print(p.nome)

print(Pessoa.op1_contrutor('Construtor 2').nome)