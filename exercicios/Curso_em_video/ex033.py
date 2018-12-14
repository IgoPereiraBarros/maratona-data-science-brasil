from time import sleep
print('Somente números positivos e inteiros')
print('...')
sleep(2)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print(n1, 'É maior')
elif n2 > n1 and n2 > n3:
    print(n2, 'É maior')
elif n3 > n1 and n3 > n2:
    print(n3, 'É maior')

if n1 < n2 and n1 < n3:
    print(n1, 'É menor')
elif n2 < n1 and n2 < n3:
    print(n2, 'É menor')
elif n3 < n1 and n3 < n2:
    print(n3, 'É menor')