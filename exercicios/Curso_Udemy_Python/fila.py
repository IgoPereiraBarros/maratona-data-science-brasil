import heapq

class FilaPrioridade:
	''' Classe utilizada para inserir e remover elemenos de uma fila '''
	def __init__(self):
		self.fila = []
		self.indice = 0

	def push(self, item, prioridade):
		''' Insere elementos na lista de fila'''
		heapq.heappush(self.fila, (-prioridade, self.indice, item))

	def pop(self):
		''' Remove elementos na lista de fila'''
		return heapq.heappop(self.fila)[-1]

class Item:

	def __init__(self, nome):
		self.nome = nome

	def __repr__(self):
		return self.nome

fila = FilaPrioridade()
fila.push(Item('Igo'), 21)
fila.push(Item('Maria Dina'), 50)
fila.push(Item('Maria Luana'), 18)
fila.push(Item('Afonso'), 49)

print(fila.pop())
print(fila.pop())
print(fila.pop())
print(fila.__doc__)	
