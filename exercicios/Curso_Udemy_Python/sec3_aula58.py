
class MyList(list):

	def append(self, *args):
		self.extend(args)

m = MyList()

m.append(0)
m.append(1,2,3,4,5,6)
print(m)

class MyList1(list):

	def sort(self):
		return 'eae vey? ta afim de ordenar?'

l = [4,1,78,34,4,9]

'''l.sort()
print(l)'''

lista = MyList1()
print(lista.sort())

