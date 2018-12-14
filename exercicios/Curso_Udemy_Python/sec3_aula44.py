
class Data:

	def __init__(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano
		print(self)

	@classmethod
	def de_string(cls, data_string):
		dia, mes, ano = map(int, data_string.split('-'))
		data = cls(dia, mes, ano)
		return data

	@staticmethod
	def is_date_valid(data_string):
		dia, mes, ano = map(int, data_string.split('-'))
		return dia <= 31 and mes <= 12 and ano <= 2020


data = Data(31, 7, 1996)
data1 = Data.de_string('31-07-1996')
print(data1)
print(data1.is_date_valid('31-07-1996'))