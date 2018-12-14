from abc import ABCMeta, abstractmethod

class ClasseAbstrata(metaclass=ABCMeta):

	@abstractmethod
	def fazer_algo(self):
		pass

	@abstractmethod
	def fazer_outra_coisa(self, a):
		pass


c = ClasseAbstrata() # Aqui dará erro, pois uma classe abstrata nunca poderá ser instanciada