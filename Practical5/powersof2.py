# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:57:47 2020

@author: shen
"""

temp = input("'Please input a possitive integer in range(1,2**13)':")
num = int(temp)
i = 0
binum = "'Result':"
while num // 2 != 0:
    if num%2 == 1:
        binum = str(binum) + "2**" + str(i) + " + "
        i +=1
        num = num/2
    else:
        i +=1
        num = num/2
binum = str(binum) + "2**" + str(i)
print(binum)