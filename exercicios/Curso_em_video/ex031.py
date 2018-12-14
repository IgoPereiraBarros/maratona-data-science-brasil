viagem = float(input('Digite quantos kilometros vc percorreu na viagem? '))
if viagem <= 200:
    preco = viagem * 0.50
    print('Você andou até 200km, por isso paragá R$ {}'.format(preco))
else:
    preco = viagem * 0.45
    print('Você andou mais que 200km, por isso paragá R$ {}'.format(preco))

preco = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print('Você andou {}km, por isso pagará R$ {}'.format(viagem, preco))
