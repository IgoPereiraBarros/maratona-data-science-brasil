dic = {
    101111: 'Igor',
    202222: 'Dina',
    303333: 'Afonso',
    404444: 'Luana'
}

dic2 = {
    404444: 'Luana',
    505555: 'Dasdores'
}

t = (1, 2, 3)

print(dic)
print(len(dic))
#del(dic[101111])
#print(dic)
print(dic.keys()) # retorna as chavez do meu dicionario
print(dic.values()) # retorna os valores do meu dicionario
print(dic.get(202222))
print(dic.popitem()) # retorna um elemento aleatoriamente e o remove automaticamente
print(dic)

'''if 404444 in dic:
    print('Sim')
else:
    print('Não')'''

dic.update(dic2)
print(dic)

dic[t] = 'Udacity'
print(dic)
