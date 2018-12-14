# -*- coding: utf-8 -*-
"""
Created on Sun May 27 00:42:48 2018

@author: Igo
"""

x = [1, 7, 5]
w = [0.8, 0.1, 0]

def soma(x, w):
	sun = 0
	for i in range(len(x)):
			sun += x[i] * w[i]
	return sun

s = soma(x, w)
print(s)

def step_function(sun):
	if sun >= 1:
		return 1
	return 0

sf = step_function(s)
print(sf)


