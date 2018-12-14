# -*- coding: utf-8 -*-
"""
Created on Sun May 27 00:42:48 2018

@author: Igo
"""

import numpy as np

x = np.array([1, 7, 5])
w = np.array([0.8, 0.1, 0])

def soma(x, w):
    return x.dot(w)

s = soma(x, w)

def step_function(sun):
    if sun >= 1:
        return 1
    return 0

sf = step_function(s)
