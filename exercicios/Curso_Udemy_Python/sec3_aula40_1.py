from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):

	@abstractmethod
	def som_animal(self):
		return 'som de algum outro animal'
		pass

class Cachorro(Animal):

	def som_animal(self):
		s = super(Cachorro, self).som_animal()
		return '%s - %s' % (s, 'AUAU')

c = Cachorro()

print(c.som_animal())