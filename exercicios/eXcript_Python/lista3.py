lista = [1, 2, 3, 4, 5]
lista = lista + [6]
print(lista)

lista += [7, 8, 9, 10]
print(lista)

lista.append(11)
print(lista)

lista.append([11])
print(lista)
print(type(lista[-1]))

del(lista[-1])
print(lista)

lista += 10 * [0]
print(lista)