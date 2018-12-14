num = int(input('Informe um número: '))
print('''Escolha uma das bases para a conversão
    [1] converter para  BINARIO
    [2] converter para OCTAL
    [3] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('({})10 = ({})2'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('({})10 = ({})8'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('({})10 = ({})16'.format(num, hex(num)[2:]))
else:
    print('Opção de animal, nem existe! KKKKKKK')
