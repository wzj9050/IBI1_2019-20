# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:21:00 2020

@author: shen
"""

file_name = input('Please input a filename as the new fasta file:')
data_extract = open('mito_gene.fa', 'r')
re_com_seq =[]
for each_line in data_extract:
    if each_line[:1] == 'N':
        (title, name) = each_line.split(': ')
        new_name = name.rstrip('\n')
    elif each_line[:1] == 'L':
        (title, length) = each_line.split(': ')
        re_com_seq.append(new_name + ' ' + length)
    else:
        reverse_complementary = ''
        for base in each_line:
            if base == 'A':
                reverse_complementary = 'T' + reverse_complementary
            elif base == 'C':
                reverse_complementary = 'G' + reverse_complementary
            elif base == 'G':
                reverse_complementary = 'C' + reverse_complementary
            elif base == 'T':
                reverse_complementary = 'A' + reverse_complementary
        re_com_seq.append(reverse_complementary + '\n')


data_export = open(file_name, 'w')
data_export.writelines(re_com_seq)
data_export.close
data_extract.close
        