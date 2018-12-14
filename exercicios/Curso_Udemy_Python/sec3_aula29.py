class Funcionario:

	def __init__(self, CPF, nome, cargo, salario):
		self.CPF = CPF
		self.nome = nome
		self.cargo = cargo
		self.salario = salario

	def get_calc_salario(self):
		return self.salario * 0.1

class Gerente(Funcionario):

	def __init__(self, CPF, nome, cargo, salario, senha):
		super().__init__(CPF, nome, cargo, salario)
		self.senha = senha

	def get_calc_salario(self):
		return super().get_calc_salario() + 1000.00

g = Gerente('111.222.333.00', 'Joãozim', 'Gerente', 2000.00, 'senha@123')

print(g.CPF)
print(g.nome)
print(g.cargo)
print(g.senha)
print(g.get_calc_salario())