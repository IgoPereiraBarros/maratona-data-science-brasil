x = 1
y = 4
z = 6

if ((x and y) or (x and z)) in range(1, 6):
    print('Certo')
else:
    print('Errado')

if (10 or x) in range(1, 5): # se a primeira premissa for for falsa e a outra verdadeira irá retornar FALSE
    print('Sim')
else:
    print('Não')

if (x or 10) in range(1, 5): # se a primeira premissa for verdadeira e a outra falsa irá retornar TRUE
    print('Sim')
else:
    print('Não')

                            # isso por que o Python so verifica a primeira premissa, se a primeira premissa for falsa, ele da o resto da expressao
                        # como false, caso a primeira premissa for verdadeira, ai ele verifica a segunda e a expressão ira ser true