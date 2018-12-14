preco = float(input('Qual o preço do produto? R$ '))

desc = (preco - (preco * 0.05))

print('O produto que custava R$ {}, com desconto de 5%, agora custa {}'.format(preco, desc))
