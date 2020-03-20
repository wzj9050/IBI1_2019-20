# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 10:26:39 2020

@author: shen
"""
# Limit the range of the input
# Set up a loop to function the collatz fomullation
# Print results at the every end of the loop
temp = input("Please input a random positive integer:")
n = int(temp)
while n != 1 or 2 or 4:
    if n % 2 == 0:
        n = n/2
    else:
        n = n*3 + 1
    print(n)
 