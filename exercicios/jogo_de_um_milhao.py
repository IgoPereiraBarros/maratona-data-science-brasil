N = int(input())

lista = []
soma = 0
count = 0
recebe = 0


for i in range(N):
    values = int(input())
    lista.append(values)

for i, v in enumerate(lista):
    count += 1
    soma += v
    if soma >= 1000000:
        recebe = count
        break


print(recebe)
