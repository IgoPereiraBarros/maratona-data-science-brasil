from math import hypot
from math import sqrt, pow
co = float(input('Digite o comprimento do (CO): '))
ca = float(input('Digite o comprimento do (CA): '))

hip = (((co ** 2) + (ca ** 2)) ** (1/2))
hip2 = sqrt(pow(co, 2) + pow(ca, 2))
hip3 = hypot(co, ca)

print('O comprimento da hipotenusa é {}'.format(hip)) # usando lógica
print('O comprimento da hipotenusa é {}'.format(hip2)) # usando lib sqrt e pow
print('O comprimento da hipotenusa é {}'.format(hip3)) # usando a lib hypot

