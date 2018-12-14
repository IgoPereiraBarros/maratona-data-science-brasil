nome = str(input('Digite seu nome completo: ')).strip()
sep = nome.split()
print('Primeiro nome: {}'.format(sep[0]))
print('Último nome: {}'.format(sep[-1]))
# ou
print('Último nome: {}'.format(sep[len(sep)-1]))

