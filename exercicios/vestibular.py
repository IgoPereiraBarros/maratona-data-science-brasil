N = int(input())
gabarito_prova = input().split()
gabarito_aluno = input().split()

list_aluno = []
list_prova = []

count = 0

for i in range(gabarito_aluno):
    for j in range(gabarito_prova):
        if gabarito_aluno[i] == gabarito_prova[j]:
            count += 1

print(count)
