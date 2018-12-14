class Pessoa():

	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

class PessoaFisica(Pessoa):

	def __init__(self, nome, idade, CPF):
		Pessoa.__init__(self, nome, idade)
		self.CPF = CPF

	def imprimir(self):
		return "CPF: " + self.CPF + ", Nome: " + self.nome + ", Idade: " + self.idade

p = Pessoa('igo', 21)
pf = PessoaFisica('Igo', 23, '058.894.363-09')

print(pf.imprimir())