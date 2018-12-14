# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 22:53:39 2018

@author: Igo
"""

from sklearn.neural_network import MLPClassifier
from sklearn import datasets

iris = datasets.load_iris()
entradas = iris.data
saidas = iris.target

redeNeural = MLPClassifier(verbose=True, max_iter=1000, tol=0.00001, activation='logistic', learning_rate_init=0.03)
redeNeural.fit(entradas, saidas)


