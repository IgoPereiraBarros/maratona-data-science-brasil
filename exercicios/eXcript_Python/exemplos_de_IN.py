'''a = 1
b = 2
c = 3

x = int(input('Digite um numero: '))

if x in [a, b, c]:
    print('True')
else:
    print('False')'''

#------------------------------------------------------

cores = ['Blue', 'Red', 'Brack', 'Green', 'Yellom']

while True:
    cor = str(input('Digite uma cor, ou 0 para sair: ')).strip()

    if cor == '0':
        break
    elif cor in cores:
        print('\nEstá contida nas cores')
    else:
        print('\nNão está contida nas cores')


