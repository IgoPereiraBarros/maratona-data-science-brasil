'''' style
        - 0 (none)
        - 1 (bold)
        - 4 (underline)
        - 7 (negative)
    text
        30 a 37
    backgraund
        40 a 47

    ex: /033[;;m
'''

print('\033[1;34;42mHello World\033[m')
print('\033[7;30mTeste1\033[m')
a = 'vermelho'
b = 'azul'
print('Aqui vai sair a cor \033[31m{}\033[m, já aqui a cor \033[34m{}\033[m'.format(a, b))

nome = 'Igor Pereira Barros'
print('Seja muito bem vindo {0}{1}{2}'.format('\033[1;35m', nome, '\033[m'))

colors = {'limpa': '\033[m', 'azul': '\033[34m', 'amarelo': '\033[33m', 'verde': '\033[32m', 'roxo': '\033[35m', 'pretoebranco': '\033[7;30m'}
print('Parazer em te conhecer {}{}{}, seja muito bem vindo!!'.format(colors['azul'], nome, colors['limpa']))
