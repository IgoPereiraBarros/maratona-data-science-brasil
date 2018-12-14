from random import randint
from emoji import emojize
from time import sleep
jogador = int(input('Escolha um número de 0 a 5: '))
computador = randint(0, 5)
print('Aguarde...')
sleep(3)
print('Número sorteado: {}'.format(computador))
if jogador == computador:
    print(emojize('Parabéns você acertou :smile:!', use_aliases=True))
elif jogador < 0:
    print(emojize('Digite apenas números positivos e inteiros :no_entry_sign:', use_aliases=True))
else:
    print(emojize('Que pena, você errou! Tente outra vez! :grin:', use_aliases=True))
