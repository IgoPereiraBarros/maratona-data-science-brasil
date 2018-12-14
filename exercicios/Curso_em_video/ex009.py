t = int(input('Digite o número que deseja tabuar: '))

aux = 1

print('-' * 12, 'TABUADA' ,12 * '-')
print('{} x {:2} = {}'.format(t, aux, (t * aux)))
print('{} x {:2} = {}'.format(t, (aux+1), (t * (aux+1))))
print('{} x {:2} = {}'.format(t, (aux+2), (t * (aux+2))))
print('{} x {:2} = {}'.format(t, (aux+3), (t * (aux+3))))
print('{} x {:2} = {}'.format(t, (aux+4), (t * (aux+4))))
print('{} x {:2} = {}'.format(t, (aux+5), (t * (aux+5))))
print('{} x {:2} = {}'.format(t, (aux+6), (t * (aux+6))))
print('{} x {:2} = {}'.format(t, (aux+7), (t * (aux+7))))
print('{} x {:2} = {}'.format(t, (aux+8), (t * (aux+8))))
print('{} x {} = {}'.format(t, (aux+9), (t * (aux+9))))
print('-' * 32)