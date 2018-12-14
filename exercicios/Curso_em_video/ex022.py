from time import sleep
nome = str(input('Digite seu nome completo: ')).strip()
print('Analiando o seu nome...')
sleep(3)
print('Seu nome em Maiúsculo: {}'.format(nome.upper()))
print('Seu nome em Minúsculo: {}'.format(nome.lower()))
print('A quantidade de letra do seu nome completo, sem os espaços é: {}'.format(len(nome) - nome.count(' ')))
qtd = nome.split()
print('A quantidade de letras do seu primeiro nome é: {}'.format(len(qtd[0])))
# ou
print('A quantidade de letras do seu primeiro nome é: {}'.format(nome.find(' ')))