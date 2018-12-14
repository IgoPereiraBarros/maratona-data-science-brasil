a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if (a + b) > c:
    area = a + b + c
    print('FORMA TRIÂNGULO DE ÁREA {}'.format(area))
else:
    print('NÃO FORMA TRIÂNGULO')

if a == b == c:
    print('Equilátero: todos os lados são iguais')
elif a == b or b == c or a == c:
    print('Isósceles: dois lados iguais')
else:
    print('Escaleno: todos os lados são diferentes')