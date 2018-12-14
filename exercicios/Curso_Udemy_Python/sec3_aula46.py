
class Pessoa:

	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade


p = Pessoa.__new__(Pessoa)
dados = {'nome': 'Igo', 'idade':21}
for key, value in dados.items():
	setattr(p, key, value)
print(p.nome, p.idade)