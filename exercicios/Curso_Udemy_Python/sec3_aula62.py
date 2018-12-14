# Generators (Geradores)
# Fibonacci: 1, 1, 2, 3, 5, 8, ...

def fib(max):

	x, y = 1, 1
	while x < max:
		yield x
		x, y = y, x + y

fib = fib(10)
'''print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))'''

for i in fib:
	print('{}'.format(i), end=' ')