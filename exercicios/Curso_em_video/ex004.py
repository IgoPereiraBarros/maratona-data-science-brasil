n = input('Digite alguma coisa: ')

print('O tipo primitivo desse valor é {}: '.format(type(n)))
print('Tem espaço? {}'.format(n.isspace()))
print('É um número? {}'.format(n.isnumeric()))
print('É alfabético? {}'.format(n.isalpha()))
print('É alfa numerico? {}'.format(n.isalnum()))
print('É maiúsculo? {}'.format(n.isupper()))
print('É minusculo? {}'.format(n.islower()))
print('Está capitalizada? {}'.format(n.istitle()))
