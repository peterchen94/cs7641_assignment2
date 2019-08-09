#!/usr/bin/env python
# coding: utf-8

# In[2]:
### GT ID:cchen376
### CS7641 Spring 2019 (OMSA program)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# In[13]:


f_fit=plt.figure(figsize=(7,5))
ax_fit = f_fit.add_subplot(1, 1, 1)

f_time=plt.figure(figsize=(7,5))
ax_time = f_time.add_subplot(1, 1, 1)


ga_metrics={'method':[],'fitness':[],'total time':[]}
file_list=[]
for dirpath, dirnames, filenames in os.walk('./'):
    for file in filenames:
        if 'GA' in file and '.txt' in file:
            print(file)
            file_list.append(file)
            df=pd.read_csv(file)
            ax_fit.plot(df['iterations'],df['fitness'])
            ax_fit.set_title('FLIPFLOP Fitness - GA')
            ax_fit.set_xlabel('iterations')
            ax_fit.set_ylabel('fitness')
            
            
            ax_time.plot(df['iterations'],df['time'])
            ax_time.set_title('FLIPFLOP time - GA')
            ax_time.set_xlabel('iterations')
            ax_time.set_ylabel('time')
            
            ga_metrics['method'].append(file[9:-10])
            ga_metrics['fitness'].append(df['fitness'].iloc[-1])
            ga_metrics['total time'].append(df['time'].iloc[-1])

            
ga_list=[file[9:-10] for file in file_list]

ax_time.legend(ga_list)
ax_fit.legend(ga_list)

f_fit.savefig('FIT_FLIPFLOP_GA_plot.png')
f_time.savefig('TIME_FLIPFLOP_GA_plot.png')

df_ga = pd.DataFrame(ga_metrics)
df_ga


# In[12]:


f_fit=plt.figure(figsize=(7,5))
ax_fit = f_fit.add_subplot(1, 1, 1)

f_time=plt.figure(figsize=(7,5))
ax_time = f_time.add_subplot(1, 1, 1)

sa_metrics={'method':[],'fitness':[],'total time':[]}
file_list=[]
for dirpath, dirnames, filenames in os.walk('./'):
    for file in filenames:
        if 'SA' in file and '.txt' in file:
            print(file)
            file_list.append(file)
            df=pd.read_csv(file)
            ax_fit.plot(df['iterations'],df['fitness'])
            ax_fit.set_title('FLIPFLOP Fitness - SA')
            ax_fit.set_xlabel('iterations')
            ax_fit.set_ylabel('fitness')
            
            ax_time.plot(df['iterations'],df['time'])
            ax_time.set_title('FLIPFLOP time - SA')
            ax_time.set_xlabel('iterations')
            ax_time.set_ylabel('time')
            
            sa_metrics['method'].append(file[9:-10])
            sa_metrics['fitness'].append(df['fitness'].iloc[-1])
            sa_metrics['total time'].append(df['time'].iloc[-1])

            
sa_list=[file[9:-10] for file in file_list]
ax_time.legend(sa_list)
ax_fit.legend(sa_list)

f_fit.savefig('FIT_FLIPFLOP_SA_plot.png')
f_time.savefig('TIME_FLIPFLOP_SA_plot.png')

df_sa = pd.DataFrame(sa_metrics)
df_sa


# In[14]:


f_fit=plt.figure(figsize=(8,6))
ax_fit = f_fit.add_subplot(1, 1, 1)

f_time=plt.figure(figsize=(8,6))
ax_time = f_time.add_subplot(1, 1, 1)

MIMIC_metrics={'method':[],'fitness':[],'total time':[]}
file_list=[]
for dirpath, dirnames, filenames in os.walk('./'):
    for file in filenames:
        if 'MIMIC' in file and 'txt' in file:
            print(file)
            file_list.append(file)
            df=pd.read_csv(file)
            ax_fit.plot(df['iterations'],df['fitness'])
            ax_fit.set_title('FLIPFLOP Fitness - MIMIC')
            ax_fit.set_xlabel('iterations')
            ax_fit.set_ylabel('fitness')
            
            ax_time.plot(df['iterations'],df['time'])
            ax_time.set_title('FLIPFLOP time - MIMIC')
            ax_time.set_xlabel('iterations')
            ax_time.set_ylabel('time')
            
            MIMIC_metrics['method'].append(file[9:-10])
            MIMIC_metrics['fitness'].append(df['fitness'].iloc[-1])
            MIMIC_metrics['total time'].append(df['time'].iloc[-1])

            
sa_list=[file[9:-10] for file in file_list]
ax_time.legend(sa_list)
ax_fit.legend(sa_list)

f_fit.savefig('FIT_FLIPFLOP_MIMIC_plot.png')
f_time.savefig('TIME_FLIPFLOP_MIMIC_plot.png')

df_MIMIC = pd.DataFrame(MIMIC_metrics)
df_MIMIC


# In[15]:


f_fit=plt.figure(figsize=(8,6))
ax_fit = f_fit.add_subplot(1, 1, 1)

f_time=plt.figure(figsize=(8,6))
ax_time = f_time.add_subplot(1, 1, 1)


overall_file_list=['FLIPFLOP_GA100_30_50_1_LOG.txt',
                   'FLIPFLOP_SA0.2_1_LOG.txt',
                   'FLIPFLOP_MIMIC200_80_0.8_1_LOG.txt',
                   'FLIPFLOP_RHC_1_LOG.txt']

overall_metrics={'method':[],'fitness':[],'total time':[]}
file_list=[]
for dirpath, dirnames, filenames in os.walk('./'):
    for file in filenames:
        if file in overall_file_list:
            print(file)
            file_list.append(file)
            df=pd.read_csv(file)
            ax_fit.plot(df['iterations'],df['fitness'])
            ax_fit.set_title('FLIPFLOP Fitness - 4 model comparison')
            ax_fit.set_xlabel('iterations')
            ax_fit.set_ylabel('fitness')
            
            ax_time.plot(df['iterations'],df['time'])
            ax_time.set_title('FLIPFLOP time - 4 model comparison')
            ax_time.set_xlabel('iterations')
            ax_time.set_ylabel('time')
            
            overall_metrics['method'].append(file[9:-10])
            overall_metrics['fitness'].append(df['fitness'].iloc[-1])
            overall_metrics['total time'].append(df['time'].iloc[-1])

            
sa_list=[file[9:-10] for file in file_list]
ax_time.legend(sa_list)
ax_fit.legend(sa_list)

f_fit.savefig('FIT_FLIPFLOP_Overall_plot.png')
f_time.savefig('TIME_FLIPFLOP_Overall_plot.png')

df_overall = pd.DataFrame(overall_metrics)
df_overall


# In[ ]:




