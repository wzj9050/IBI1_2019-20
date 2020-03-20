# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 09:50:04 2020

@author: shen
"""

a = 123
b = 123123
c = b/7
d = c/11
e = d/13
print(e)


X = True
Y = False
Z = (X and not Y) or (Y and not X)
print(Z)
W = X != Y
print(W)
X = True
Y = True
Z = (X and not Y) or (Y and not X)
print(Z)
W = X != Y
print(W)