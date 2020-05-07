# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 09:43:53 2020

@author: shen
"""

seq = 'ATGCGACTACGATCGAGGGCCAT'
l = list(seq)
l.reverse()
table = str.maketrans("ACTG","TGAC") 
string = "".join(l)
string = string.translate(table)
print('The reverse complementary sequence is %s' %(string))