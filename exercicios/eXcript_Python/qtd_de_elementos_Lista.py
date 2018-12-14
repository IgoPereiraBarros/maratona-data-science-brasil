lista = ['Igo', 'Dina', 'Luana', 'Afonso', 'Dasdores', 'Zilda', 'Betoven', ]
print(lista[len(lista)-1])

lista.insert(3, 'Zilda')
print(lista)

lista.append('Zilda')
print(lista)

print(lista.count('Zilda'))

print(lista.index('Afonso'))

print(lista.index('Zilda')) # so exibe a primeira ocorrencia do nome passado por parametro