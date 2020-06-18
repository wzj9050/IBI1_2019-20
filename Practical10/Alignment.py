# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:46:24 2020

@author: shen
"""

import pandas as pd

#Import the file of "BLOSUM62.xlsx"
matrix_path = "./BLOSUM62.xlsx"
#Convert the file into matrix
matrix = pd.read_excel(matrix_path, sheet_name=0, header=0, index_col=0)


#The sequences for comparison.
seq1 = '''MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'''
seq2 = '''MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'''
seq3 = 'WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'

sum1=0
sum2=0
sum3=0
edit_distance1=0
edit_distance2=0
edit_distance3=0
for i in range(len(seq1)):
    col_name = seq1[i]
    index_name = seq2[i]
    sum1 += matrix[col_name][index_name]#Uptake scores with aas in two sequences as column titles and row indexes.
    if col_name!=index_name:
        edit_distance1 +=1#Count the Hamming distance.
for i in range(len(seq1)):
    col_name = seq1[i]
    index_name = seq3[i]
    sum2 += matrix[col_name][index_name]
    if col_name!=index_name:
        edit_distance2 +=1
for i in range(len(seq2)):
    col_name = seq2[i]
    index_name = seq3[i]
    sum3 += matrix[col_name][index_name]
    if col_name!=index_name:
        edit_distance3 +=1
print("The score of alignment between human sequence and mouse sequence is: "+str(sum1)+".")
print("The score of alignment between human sequence and random sequence is: "+str(sum2)+".")
print("The score of alignment between mouse sequence and random sequence is: "+str(sum3)+".")
print("The Hamming distance of alignment between human sequence and mouse sequence is: "+str(edit_distance1)+".")
print("The Hamming distance of alignment between human sequence and random sequence is: "+str(edit_distance2)+".")
print("The Hamming distance of alignment between mouse sequence and random sequence is: "+str(edit_distance3)+".")





















