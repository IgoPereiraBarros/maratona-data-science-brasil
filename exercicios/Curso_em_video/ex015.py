km = float(input('Quantos km o carro percorreu? '))
qtd_dias = int(input('Quantos dias o carro foi usado? '))
preco = ((60 * qtd_dias) + (km * 0.15))

print('O preco do aluguel do carro que percorreu {} km e foi alugado com {} custará R$ {} '.format(km, qtd_dias, preco))
