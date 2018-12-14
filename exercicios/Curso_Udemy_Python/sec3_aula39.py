class Encap():

	def __init__(self, x):
		self.__x = x

	'''def getX(self):
		return self.__x
							>>>> Não é pythonico
	def setX(self, x):
		if x > 0:
			self.__x = x'''

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, x):
		if x > 0:
			self.__x = x

e = Encap(1)

print(e.x)
e.x = 12
print(e.x)
e.x = 13
print(e.x)