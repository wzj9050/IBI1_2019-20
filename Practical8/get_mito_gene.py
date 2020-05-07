# -*- coding: utf-8 -*-
"""
Created on Wed May  6 14:57:45 2020

@author: shen
"""
count1 = 0
count2 = -1
sequence = ''
name_len_sequence = []
seq_len = ''
data_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
for each_line in data_file:
    if each_line[:1] != '>':
        sequence_line = each_line.rstrip('\n')
        if count1 == count2:
            sequence += sequence_line
            seq_len = 'Length: ' + str(len(sequence)) +'\n'
            
    else:
        count1 += 1
        (nonsense1, nonsense2, position, nonsense3, nonsense4, nonsensence5, name, nonsense6) = each_line. split(':', 7)
        if position == 'Mito':
            count1 = count2
            name_Mito = name.rstrip(' gene_biotype\n')
            seq_name = 'Name: ' + name_Mito + '\n'
            name_len_sequence.append(seq_len)
            name_len_sequence.append(sequence + '\n')
            sequence = ''
            name_len_sequence.append(seq_name)
name_len_sequence.append(seq_len)
name_len_sequence.append(sequence)
extract_file = open('mito_gene.fa', 'w')
extract_file.writelines(name_len_sequence)
extract_file.close
data_file.close