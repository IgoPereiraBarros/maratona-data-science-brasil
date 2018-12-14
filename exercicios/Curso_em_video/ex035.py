a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c= float(input('Digite o terceiro segmento: '))
if (a + b) > c:
    area = a + b + c
    print('Essas retas formam um triângulo de área {}'.format(area))
else:
    print('Essas retas não formam um triângulo.')