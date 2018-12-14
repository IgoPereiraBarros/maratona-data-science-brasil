# -*- coding: utf-8 -*-
"""
Created on Tue May 29 23:25:35 2018

@author: Igo
"""

import numpy as np

# Função de ativação - Sigmoid
def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

# Função que calcula a derivada da função sigmoid
def sigmoidDerivada(sig):
    return sig * (1 - sig)

'''sgm = sigmoid(0.5)
sgmd = sigmoidDerivada(sgm)'''


# Array de entradas da RNA
entradas = np.array([[0,0],
                     [0,1],
                     [1,0],
                     [1,1]])

# Array de saídas esperadas da RNA
saidas = np.array([[0], [1], [1], [0]])

# Array pesos sinapticos da primeira parte 
'''pesos0 = np.array([[-0.424, -0.740, -0.961],
                   [0.358, -0.577, -0.469]])'''

# Array pesos sinapticos da segunda parte 
#pesos1 = np.array([[-0.017], [-0.893], [0.148]])
    
pesos0 = 2*np.random.random((2,3)) - 1 # são dois neuronios na camada de entrada e 3 na camada de sáida
pesos1 = 2*np.random.random((3,1)) - 1 # 3 neuronios na camada escondida e 1 neuronio que é a camada de saída

taxaAprendizagem = 0.6
momento = 1

# épocas de treino
epocas = 1000000

for j in range(epocas):
    camadaEntrada = entradas # Variável que ira receber todas as minhas entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0) # Faz o produto escalar das entradas com os pesos da primeira parte
    camadaOculta = sigmoid(somaSinapse0) # chama a função de ativação e passa a soma das minhas camadas de entrada
    
    somaSinapse1 = np.dot(camadaOculta, pesos1) # Faz o produto escalar das camadas Ocultas com os pesos da segunda parte
    camadaSaida = sigmoid(somaSinapse1) # chama a função de ativação e passa a soma das minhas camadas Ocultas
    
    erroCamadaSaida = saidas - camadaSaida # calcula o erro  (erro = saidaCorreta - saidaCalculada)
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida)) # calcula a média absoluta dos erros da rede
    print('Números de erros: {}'.format(str(mediaAbsoluta)))
    
    derivadaSaida = sigmoidDerivada(camadaSaida) # deriva o resultado da função sigmoid da camada de saída
    deltaSaida = erroCamadaSaida * derivadaSaida # produto do erro da camada de saída com a derivada da camada de saída. Ex.: deltaSaida = erro * derivadaSigmoid
    
    pesos1Transporta = pesos1.T # transforma matriz de pesos1 em uma matriz transporta (troca coluna por linhas e virse-versa)
    deltaSaidaXPeso = deltaSaida.dot(pesos1Transporta) # produto escalar do deltaSaida com os pesos1 ja transformado para matriz transposta
    deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)
    
    camadaOcultaTransposta = camadaOculta.T # transforma a matriz da camada oculta em matriz transposta
    pesosNovo1 = camadaOcultaTransposta.dot(deltaSaida) # produto escalar da camada oculta transposta com o delta de saída
    pesos1 = (pesos1 * momento) + (pesosNovo1 * taxaAprendizagem) # ajuste dos segundo peso
    
    camadaEntradaTransposta = camadaEntrada.T
    pesosNovo0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    pesos0 = (pesos0 * momento) + (pesosNovo0 * taxaAprendizagem)
    
    