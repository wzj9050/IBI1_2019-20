# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:34:08 2020

@author: shen
"""

import random, copy

global solutions
temp = input('''Please input numbers (integers from 1 to 23)to compute 24:(use ','to divide them)\n''')
original_seq = temp.split(',')
#Define a function for testing whether the input numbers are integers from 1 to 23
def input_test(inputlist):
    count = 0
    for element in inputlist:
        if element.count('.') == 0 and 0<int(element)<24:#'.' is to eliminate float
            count +=1#Count the quantity of eligible from 1 to 23
    if count == len(inputlist):
        return True#If the quatity equals to the length of the input list, the function returns Ture
    else:
        return False#Or return False
while not input_test(original_seq):#If False, the user will be reminded and the code return to the input port until the input is eligible
    print('The input number must be integers from 1 to 23!')
    temp = input('''Please input numbers (integers from 1 to 23)to compute 24:(use ','to divide them)\n''')
    original_seq = temp.split(',')
    input_test(original_seq)
    if input_test(original_seq):
        break
original_seq = list(map(int, original_seq))
aim = 24
count = 0
answer = ''
list_solutions = []
    
def operations(a,b,oper):#Define a function to do the four operations, +/-/*//

    if oper==1:#1 is for sum
        c = a+b
        return c         
    if oper==2:#2 is for difference
        if a>=b:
            c = a-b
            return c
        else:
            c = b-a
            return c
    if oper==3:#3 is for product
        c = a*b
        return c
    if oper==4:#4 is for the quotient of a/b
        if abs(b) > 0:
            c = a/b    
            return c
        elif abs(a) > 0:
            oper = random.choice([1,2,3,5])#If b == 0 and a != 0, do a random operation from other kinds
            if oper==1:
                c = a+b
                return c         
            if oper==2:
                if a>=b:
                    c = a-b
                    return c
                else:
                    c = b-a
                    return c
            if oper==3:
                c = a*b
                return c
            if oper == 5:
                c = b/a
                return c          
        else:
            oper = random.choice([1,2,3])#If a == b ==0, do a operation from +/-/*
            if oper==1:
                c = a+b
                return c         
            if oper==2:
                if a>=b:
                    c = a-b
                    return c
                else:
                    c = b-a
                    return c
            if oper==3:
                c = a*b
                return c
    if oper==5:
        if abs(a) > 0:#The same as a/b
            c = b/a
            return c
        elif abs(b) > 0:
            oper = random.choice([1,2,3,4])
            if oper==1:
                c = a+b
                return c         
            if oper==2:
                if a>=b:
                    c = a-b
                    return c
                else:
                    c = b-a
                    return c
            if oper==3:
                c = a*b
                return c
            if oper==4:
                c = a/b
                return c
        else:
            oper = random.choice([1,2,3])
            if oper==1:
                c = a+b
                return c         
            if oper==2:
                if a>=b:
                    c = a-b
                    return c
                else:
                    c = b-a
                    return c
            if oper==3:
                c = a*b
                return c    

#Define the function calculate to recursively picking two numbers and merging them through all available operands until there is only one value left     
#'variable_seq' is the transient list for every recursion, 'original' is the input list and the 'goal' is the set value. In this problem it is 24.
def calculate(variable_seq,original,goal):
    ANSWER = []
    global count#Define the 'count' as a global variable
                #In case that it would be cleared every function using
    solutions = [] #'Solution' serves as the transfer station of the final values every recurtion
    length = len(variable_seq)
    copyChild_variable_seq = []#'copyChild_variable_seq' acts as the deepcopy of the list with child result replacing its parent numbers every recursion
                
    if length != 1:
        for i in range(0,length-1):
            for j in range (i+1,length):
                child_variable_seq = copy.deepcopy(variable_seq)#Copy the input list
                A = variable_seq[i]#Pick the first number.
                B = variable_seq[j]#Pick the second number.
                child_variable_seq.remove(A)#Remove the numbers in the copy.
                child_variable_seq.remove(B)
    
                for k in range(1,6):#Copy the list removing the two numbers
                    copyChild_variable_seq = copy.deepcopy(child_variable_seq)
                    childInputOriginal = original#Succcess the original list
                      
                    C = operations(A,B,k)#Merge the two numbers with four operations.
                                                                           
                    count += 1#Count the recursion times
       
                    copyChild_variable_seq.append(C)#Add the result of the operation           
                    if len(copyChild_variable_seq) ==1:
                        solutions.append(copyChild_variable_seq[0])#Add the final one value to the 'solutions'                         

                    else:#recurse the list to the next circulation
                        calculate(copyChild_variable_seq,childInputOriginal,goal)        
                for result in solutions:#Convey the transient answers from 'solutions' to 'list_solutions'
                        list_solutions.append(result)#'list_solutions' is the list of all available calculation results from N cards
    if list_solutions.count(24) > 0:#Identify whether 24 exists
        answer = 'Yes'
        ANSWER = [answer, count]
    
    elif list_solutions.count(24) == 0:
        answer = 'No'
        ANSWER = [answer, count]
    return ANSWER
#Use the function for enumeration method          
answer = calculate(original_seq,original_seq,aim)
print(answer[0])
print('Recursion times: ', answer[1])


