t = 'Tres Pratos de Trigo para Tigres Tristes'
r = t.upper().count(t[0])
print(r)

from random import randint
num = randint(1, 6)
res = num // 2
print(res)

from random import choice
n = [2, 5, 9, 1, 4]
res = choice(n) % n[0]
print(res)