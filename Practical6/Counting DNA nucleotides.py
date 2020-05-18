# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 09:55:24 2020

@author: shen
"""
temp = input('Please input a gene sequence:')
gene = temp
a = gene.count('A')
b = gene.count('T')
c = gene.count('G')
d = gene.count('C')# Count the numbers of every basic groups.

e = a + b + c + d
a1 = str(a*100/e)[:4] + '%'
b1 = str(b*100/e)[:4] + '%'
c1 = str(c*100/e)[:4] + '%'
d1 = str(d*100/e)[:4] + '%'# Convert all the numbers into percentages, data to two decimal point.
genedic1 = {'A':str(a1), 'T':str(b1), 'G':str(c1), 'C':str(d1)}
print(genedic1)  #Build a dictionary.
#Import the library.
import matplotlib.pyplot as plt

sizes = [a, b, c, d]#Show labels, the start angle for the first pie is 50°
plt.pie(sizes, startangle = 50)
plt.axis()
plt.show # Draw a pie.