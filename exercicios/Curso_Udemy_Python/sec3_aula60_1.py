# Serializando 	objetos: JSON - javaScript Object Notation

import json

class Contato:

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	@property
	def carrega_nome(self):
		return ('{}{}'.format(self.first_name, self.last_name))


c = Contato('Igo', 'Barros')

print(json.dumps(c.__dict__))