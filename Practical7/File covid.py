# -*- coding: utf-8 -*-
"""
Created on Wed May 13 12:15:21 2020

@author: shen
"""

import os 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
os.chdir('D:\Initial learning\IBI\Practicals')
covid_data = pd.read_csv("full_data.csv")
judge_list1 = []
judge_list2 = []
judge_list3 = []

for i in range(0,7996):#Produce Booleans for 'show all columns, and every third row between (and including) 0 and 15'
    if (((i+1)%3 == 0) and i < 16) or i == 0:
        judge_list1.append(True)
    else:
        judge_list1.append(False)
print(covid_data.loc[judge_list1,:])
for i in list(covid_data.loc[:,'location']):#Produce Booleans for 'every row where location is "Afghanistan"'
    if i == 'Afghanistan':
        judge_list2.append(True)
    else:
        judge_list2.append(False)
print(covid_data.loc[judge_list2,"total_cases"])
for i in list(covid_data.loc[:, 'location']):#Produce Booleans for 'every row where location is "world"'
    if i == 'World':
        judge_list3.append(True)
    else:
        judge_list3.append(False)

world_newcases = covid_data.iloc[judge_list3,[0,2]]

x = np.array(list(world_newcases.iloc[:,1]))#Transform the list of world newcases into array for np calculation
world_newcases_mean = np.mean(x)#Calsulate the mean
world_newcases_median = np.median(x)#Calculate the median
print('The mean of new cases in the world is ', world_newcases_mean)
print('The median of new cases in the world is ', world_newcases_median)
world_dates = world_newcases.iloc[:,0]
world_newcases_list = list(world_newcases.iloc[:,1])
world_newdeaths_list = list(covid_data.iloc[judge_list3,3])
plt.xlabel('New cases around the world')
plt.ylabel('Value')
plt.boxplot(world_newcases_list, #Plot the boxplot of the world new cases
            sym='o',vert=True,
            whis=1.5,patch_artist=True,
            meanline=False,showbox=True,
            showcaps=True,showfliers=True,
            notch=False)

plt.show()
world_dates_list = list(world_newcases.iloc[:,0])#Plot the plot of world new cases and new deaths
plt.ylabel('Number')
plt.xlabel('Dates')
plt.title('New cases and new deaths around the world')
plt.plot(world_dates_list, world_newcases_list, 'bo', label = 'New cases')
plt.plot(world_dates_list, world_newdeaths_list, 'ro', label = 'New deaths')
plt.xticks(world_dates[0:len(world_dates):4],rotation=-90)
#Add legends
plt.legend(bbox_to_anchor=(0.7, 1, 1., .102), loc=9,ncol=1, mode=None, borderaxespad=0.)
plt.show()
judge_list4 = []
for i in list(covid_data.loc[:,'location']):#Produce Booleans for 'every row where location is "Spain"'
    if i == 'Spain':
        judge_list4.append(True)
    else:
        judge_list4.append(False)
Spain_newcases_totalcases = covid_data.iloc[judge_list4,[0,2,4]]
Spain_newcases_list = list(Spain_newcases_totalcases.iloc[:,1])
Spain_totalcases_list = list(Spain_newcases_totalcases.iloc[:,2])
plt.ylabel('Number')
plt.xlabel('Dates')
plt.title('New cases and total cases in Spain')
plt.plot(world_dates_list, Spain_newcases_list, 'yo', label = 'New cases')#Plot the Spain new cases and total cases
plt.plot(world_dates_list, Spain_totalcases_list, 'ko', label = 'Total cases')
plt.xticks(world_dates[0:len(world_dates):4],rotation=-90)
#Add legends.
plt.legend(bbox_to_anchor=(0.7, 1, 1., .102), loc=9,ncol=1, mode=None, borderaxespad=0.)
plt.show()