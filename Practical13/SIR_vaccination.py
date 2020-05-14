# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:24:42 2020

@author: shen
"""

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
#Define a function as SIR model
def SIR_vaccination(v_p):
    
    s_count = s = 9999-int(v_p*10000)
    i_count = i = 1
    r_count = r = 0
    t_count = 0
    s_list = [s]

    i_list = [i]
    r_list = [r]
    if v_p < 1:        
        while t_count < 1000:
            
    
            si_list = list(np.random.choice(range(2),s_count,p=[1-0.3*i_count/10000,0.3*i_count/10000]))#0 is healthy and 1 is sick
            s_count = si_list.count(0)
            s_list.append(s_count)
            
            
            ir_list = list(np.random.choice(range(2),i_count,p=[0.95,0.05]))#0 is infected and 1 is recovered
            copyr_list = copy.deepcopy(r_list)
            r_count = ir_list.count(1)+copyr_list[-1]
            r_list.append(r_count)
    
            i_count = 10000-int(v_p*10000) - r_count - s_count
            i_list.append(i_count)
            t_count += 1
    else:
        s_count = s = 0
        while t_count < 1000:
            
    
            si_list = list(np.random.choice(range(2),s_count,p=[1-0.3*i_count/10000,0.3*i_count/10000]))#0 is healthy and 1 is sick
            s_count = si_list.count(0)
            s_list.append(s_count)
            
            
            ir_list = list(np.random.choice(range(2),i_count,p=[0.95,0.05]))#0 is infected and 1 is recovered
            copyr_list = copy.deepcopy(r_list)
            r_count = ir_list.count(1)+copyr_list[-1]
            r_list.append(r_count)
    
            i_count = 10000 -int(v_p*10000) - r_count - s_count
            i_list.append(i_count)
            t_count += 1        
    
    answer = [i_list, v_p]
    return answer
#Define a function to return plot syntaxes and labels
def SIR_v_plot(ilist):
    labels = str(ilist[1]*100) + '%'
    return plt.plot(range(0,1001), ilist[0], label = labels)

plt.xlabel('time')
    
plt.ylabel('number of people')
    
plt.title('SIR model')
    
#Plot infected cureves with different immune coverage
SIR_v_plot(SIR_vaccination(0))
SIR_v_plot(SIR_vaccination(0.1))
SIR_v_plot(SIR_vaccination(0.2))
SIR_v_plot(SIR_vaccination(0.3))
SIR_v_plot(SIR_vaccination(0.4))
SIR_v_plot(SIR_vaccination(0.5))
SIR_v_plot(SIR_vaccination(0.6))
SIR_v_plot(SIR_vaccination(0.7))
SIR_v_plot(SIR_vaccination(0.8))
SIR_v_plot(SIR_vaccination(0.9))
SIR_v_plot(SIR_vaccination(1))
#Show the legend
plt.legend(bbox_to_anchor=(0.7, 1, 1., .102), loc=9,ncol=1, mode=None, borderaxespad=0.)


plt.show()
