# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:42:21 2020

@author: shen
"""
#Import important libraries.
import numpy as np
import matplotlib.pyplot as plt

# Make array of all susceptible population 
population = np.zeros ( (100, 100) )
outbreak = np.random.choice (range(100),2)
#Produce the first infected point.
population [ outbreak [0], outbreak [1] ] = 1
#Draw the 100*100 image as population
plt. figure ( figsize =(6,4), dpi=150) 
plt. imshow( population, cmap= 'viridis', interpolation='nearest' )
#Set the time points count.
time_point = 0



#Define a function to return the coordinates of neighbors of the 'point' 
#Also return the number of infected people in neighbors.
def sudoku(point):
    global population
    sudoku_list = []
    count = 0
    p0 = int(point[0])
    p1 = int(point[1])
#The possible addresses of the neighbors
    a = [p0-1,p1-1]
    b = [p0-1,p1]
    c =[p0,p1-1]
    d =[p0,p1+1]
    e =[p0+1,p1-1]
    f =[p0-1,p1+1]
    g =[p0+1,p1]
    h =[p0+1,p1+1]
#Deal with care for the corners and boundaries
#Append the coordinates to the returnning list
    if point[0]==0 and point[1]!=0 and point[1]!= 99:
        sudoku_list.extend([c,d,e,g,h])
    if point[0]==99 and point[1]!=0 and point[1]!= 99:
        sudoku_list.extend([a,b,c,d,f])
    if point[1]==0 and point[0]!=0 and point[0]!=99:
        sudoku_list.extend([b,d,f,g,h])
    if point[1]==99 and point[0]!=0 and point[0]!=99:
        sudoku_list.extend([a,b,c,e,g])
    if point[0]==0 and point[1]==0:
        sudoku_list.extend([d,g,h])
    if point[0]==0 and point[1]== 99:
        sudoku_list.extend([c,e,g])
    if point[0]==99 and point[1]==0:
        sudoku_list.extend([b,d,f])
    if point[0]==99 and point[1]== 99:
        sudoku_list.extend([a,b,c])
    if point[0]!=0 and point[1]!=0 and point[1]!= 99 and point[0]!=99:
        sudoku_list.extend([a,b,c,d,e,f,g,h])
    for point1 in sudoku_list:

        if population[point1[0], point1[1]] ==1:
            count +=1
    answer = [sudoku_list,count]#Return the coordinates and the count of the infected

    return answer
while time_point < 100:
    #Pass the whole matrix
    for i0 in range(0,population.shape[0]): 
        for i1 in range(0,population.shape[1]):
            p0 = i0
            p1 = i1
            sudoku_data = sudoku([p0,p1])
            #Uptake the points who is susceptible and adjacent with the infected
            if (population[p0,p1] == 0) and sudoku_data[1] !=0:
                population[p0,p1] = 4#4 is the susceptible person having been passed this time

                for i in sudoku_data[0]:#I re-calculated the infected possibility based on the β and the susceptible persons' neighbors
                    if list(np.random.choice(range(2),1,p=[0.7**sudoku_data[1],1-0.7**sudoku_data[1]]))[0] ==1:#0 is healthy and 1 is sick
                        population[int(i[0]),int(i[1])]=3#3 is the person who is new case this time point
            #Infected ones to recovered ones
            if population[p0,p1] == 1:
                for i in sudoku_data[0]:
                    if list(np.random.choice(range(2),1,p=[0.95,0.05]))[0] ==1:#0 is infected and 1 is recovered
                        population[int(i[0]),int(i[1])]=2
    time_point +=1#Count the time point.
    #Pass the matrix to convert the new cases and passed susceptible cases into normal(1 and 0)
    for ri0 in range(0,population.shape[0]):
        for ri1 in range(0,population.shape[1]):
            rp0 = int(ri0)
            rp1 = int(ri1)
            if population[rp0,rp1] == 4:
                population[rp0,rp1] = 0
            elif population[rp0,rp1] ==3:
                population[rp0,rp1] = 1
#Show the images at 10, 50, 100 time points 
    if time_point == 10:
        plt. figure ( figsize =(6,4), dpi=150) 
        plt. imshow( population, cmap= 'viridis', interpolation='nearest' )
        plt.show()
    if time_point == 50:
        plt. figure ( figsize =(6,4), dpi=150) 
        plt. imshow( population, cmap= 'viridis', interpolation='nearest' )
        plt.show()
if time_point == 100:
    plt. figure ( figsize =(6,4), dpi=150) 
    plt. imshow( population, cmap= 'viridis', interpolation='nearest' )
    plt.show()