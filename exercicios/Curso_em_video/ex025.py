from time import sleep
nome = input('Digite um nome: ')

print('Vamos verificar se seu nome tem Silva...')

sleep(3)

if 'Silva' in nome and nome.upper() and nome.lower():
    print('Sim')
else:
    print('Não')
