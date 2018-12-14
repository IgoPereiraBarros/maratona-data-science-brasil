nome = str(input('Digite sue nome: '))

if nome == 'Igo' or nome == 'igo':
    print('Que nome orginal você tem!')
elif nome in 'Jarmeson Iago João Marcos Luis Felipe':
    print('Um dos nomes dos seu amigos!')
elif nome in 'Maria Dina Luana Afonso':
    print('É um dos membros de sua família!')
elif nome == 'Pedro' or nome == 'Jonatas' or nome == 'Carlos':
    print('Não conhece nenhum desses nomes')
else:
    print('Que nome estranho!')

print('Seja bem vindo {}'.format(nome))