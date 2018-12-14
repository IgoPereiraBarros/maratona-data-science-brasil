
class A:

	def aa(self):
		pass

	def bb(self):
		pass

	def cc(self, nome):
		print(nome)

class B:

	def __init__(self):
		self.a = A()

	def aa(self):
		# delega para self.a
		return self.a.aa()

	def bb(self):
		# delega para self.a
		return self.a.bb()

	def __getattr__(self, nome):
		return getattr(self.a, nome)


b = B()
b.aa() # chama o B.aa (existe esse método em B)
b.cc('python') # chama B.__getattr__('python') e delega para A.aa
