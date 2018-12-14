n = int(input('Digite um número: '))

print('O dobro de {} é igual a {}'.format(n, (n*2)))
print('O triblo do valor {} é igual a {}'.format(n, (n*3)))
print('A raiz quandrada de {} é igual a {}'.format(n, (n ** (1/2))))

# outra maneira
print('O triblo de {0} vale {1}. A raiz quadrada de {0} vale {2:.2f}'.format(n, (n*3), (n**(1/2))))

#outra maneira
print('O triblo de {0} vale {1}. A raiz quadrada de {0} vale {2:.2f}'.format(n, (n*3), pow(n, (1/2))))
