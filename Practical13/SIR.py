# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Counts to record the transient data and time points
#Lists/arrays to record the acumulated data for plot
import numpy as np 
import matplotlib . pyplot as plt
import copy
s_count = s = 9999#Susceptible
i_count = i = 1#Infected
r_count = r = 0#Recovered
t_count = 0
s_list = [s]#List accumulates susceptible numbers
copys_list = copy.deepcopy(s_list)
i_list = [i]#List accumulates infected numbers
r_list = [r]#List accumulates recovered numbers
while t_count < 1000:
        
    #Susceptible to infected. The possibility depends on β and proportion of infected ones in population
    si_list = list(np.random.choice(range(2),s_count,p=[1-0.3*i_count/10000,0.3*i_count/10000]))#0 is healthy and 1 is sick
    s_count = si_list.count(0)
    s_list.append(s_count)
        
    #Infected to recovered    
    ir_list = list(np.random.choice(range(2),i_count,p=[0.95,0.05]))#0 is infected and 1 is recovered
    copyr_list = copy.deepcopy(r_list)#Copy the list
    r_count = ir_list.count(1)+copyr_list[-1]#Growth add the base to get the present recovered number
    r_list.append(r_count)
    #Population minus S and R to get infected sum
    i_count = 10000 - r_count - s_count
    i_list.append(i_count)
    t_count += 1#Count the time point

#Plot the figure
answer = [s_list, i_list, r_list]

slist = answer[0]
ilist = answer[1]
rlist = answer[2]
plt.xlabel('time')

plt.ylabel('number of people')

plt.title('SIR model')





plt.plot(range(0,1001), slist, label = 'susceptible')
plt.plot(range(0,1001), ilist, label = 'infected')
plt.plot(range(0,1001), rlist, label = 'recovered')
#Show the legend for the plot
plt.legend(bbox_to_anchor=(0.7, 1, 1., .102), loc=9,ncol=1, mode=None, borderaxespad=0.)
plt.show()
