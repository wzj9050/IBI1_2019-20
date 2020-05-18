# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 12:06:12 2020

@author: shen
"""

#Input a gene length list.
temp = input('Please impport some DNA lengths divided by blanks:')
#Transform the impot into a list
l = list(map(lambda x:int(x),list(temp.split(' '))))
l.sort()
del l[0]#Sort the list from little to big and delete the minimum
l.sort(reverse = True)
del l[0]#Reverse the sorted list and delete the maximum
print(l)

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams["font.sans-serif"] = ["Times New Roman"]#Set the typeface as 'Times New Roman'
mpl.rcParams["axes.unicode_minus"] = False


x = np.array(l)


plt.boxplot(x)

plt.xticks([1], ["Sorted Gene Lengths"])#Preserve only one label 'Sorted Gene Lengths' for the x axis
plt.ylabel("Lengths")#Y label is 'Lengths'
plt.title("The distribution of gene lengths")#Plot title is 'The distribution of gene lengths'

plt.grid(axis="y", ls=":", lw=1, color="gray", alpha=0.4)#Draw 'gray' grid line on axis y, linestyle is 'imaginary'

plt.show()