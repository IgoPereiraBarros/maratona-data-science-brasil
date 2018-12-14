'''
Módulo Simulador mantem o estado da simulacao e
os procedimentos para simular. Note que a classe
Simulador "esconde" o modulo random da funcao main.
'''


from random import seed, randrange
from Balde import *

# Constantes
CAP_MIN = 10
CAP_MAX = 51  # ja ajustado ao random
VOL_MIN = 1
VOL_MAX = 11  # ja ajustado ao random


class Simulador:
    def __init__(self, semente):
        seed(semente)
        capacidade = randrange(CAP_MIN, CAP_MAX)
        self.rec = Balde(capacidade)
        self.vol = 0
        self.avisou = False # saber se o volume passou da metade da capacidade do balde

    def sorteio(self):
        self.vol = randrange(VOL_MIN, VOL_MAX)
        print()
        print('Volume atual: {}'.format(self.rec.vol))
        print('Volume sorteado: {}'.format(self.vol))
        return self.vol

    def deposito(self):
        ''' adiciona o ultimo volume sorteado self.vol
            ao balde e retorna True se o
            balde estiver cheio e False caso contrario.
        '''

        self.rec.deposita(self.vol)

        if self.rec.vol >= self.rec.cap / 2 and not self.avisou:
            self.avisou = True
            print('O volume do balde atingiu/passou da metade do balde')

        return self.rec.cheio

    def finaliza(self):
        print('\nFim da simulação')
        print('Capacidade do balde: {}'.format(self.rec.cap))
        print('Volume final: {}'.format(self.rec.vol))

        if self.rec.der > 0:
            print('Balde esta cheio, e houve derramamento de agua')
            print('Volume derramando: {}'.format(self.rec.der))
        else:
            if self.rec.cheio:
                print('Balde esta cheio e não houve derramamento de agua')
            elif self.rec.cap - self.rec.vol >= self.vol:
                print('Balde não está cheio')
                print('Havia espaço para o ultimo volume sorteado. [{}]'.format(self.vol))
            else:
                print('Balde não está cheio')
                print('Não havia espaço para o ultimo volume sorteado. [{}]'.format(self.vol))


if __name__ == '__main__':
    s = Simulador(123)
    v1 = s.sorteio()
    r1 = s.deposito()
    print(v1, r1)
    v2 = s.sorteio()
    r2 = s.deposito()
    print(v2, r2)
    s.finaliza()
