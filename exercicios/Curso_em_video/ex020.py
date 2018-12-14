from random import shuffle
a = input('Digite o nome do aluno: ')
a2 = input('Digite o nome do aluno: ')
a3 = input('Digite o nome do aluno: ')
a4 = input('Digite o nome do aluno: ')
lista = [a, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será a seguinte: ')
print(lista)
