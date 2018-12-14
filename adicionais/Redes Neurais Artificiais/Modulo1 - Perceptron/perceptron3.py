# -*- coding: utf-8 -*-
"""
Created on Mon May 28 20:21:00 2018

@author: Igo
"""

import numpy as np

# Aplicando o operador E
entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
saidas = np.array([0, 0, 0, 1])

# Aplicando o operador OU
#entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
#saidas = np.array([0, 1, 1, 1])

# Aplicando o operador XOR
#entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
#saidas = np.array([0, 1, 1, 0])

pesos = np.array([0.0, 0.0])
taxaAprendizagem = 0.1

def step_function(sum_):
    if sum_ >= 1:
        return 1
    return 0

def calcular_saida(record):
    # produto escalar entre meu registro(valor passado no parametro da função) e minha entrada (x)
    s = record.dot(pesos)
    return step_function(s)

def train():
    erroTotal = 1
    while erroTotal != 0:
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calcular_saida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada) # calcula o meu erro
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro) #ajusta o peso
                print('Peso atualizado: {}'.format(str(pesos[j])))
        print('Total de erros: {}'.format(str(erroTotal)))
        
train()

print('REDE TREINADA')
for i in range(len(entradas)):
    print('--->' , calcular_saida(entradas[i]))