import pickle

dados = ['joão', 123, 1.34, [2,3,4], ['a', 'b', 'c']]

with open('dadosSalvos.txt', 'wb') as file:
	pickle.dump(dados, file)

with open('dadosSalvos.txt', 'rb') as file:
	dados_carregados = pickle.load(file)

# verifica se os meus dados de entrada são iguais aos meus dados que foram salvos
assert dados == dados_carregados 

print(dados_carregados)