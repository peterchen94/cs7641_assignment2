#!/usr/bin/env python
# coding: utf-8

# In[1]:

### GT ID:cchen376
### CS7641 Spring 2019 (OMSA program)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# In[9]:


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
            ax_fit.set_title('Cont Peaks Fitness - GA')
            ax_fit.set_xlabel('iterations')
            ax_fit.set_ylabel('fitness')
            
            
            ax_time.plot(df['iterations'],df['time'])
            ax_time.set_title('Cont Peaks time - GA')
            ax_time.set_xlabel('iterations')
            ax_time.set_ylabel('time')
            
            ga_metrics['method'].append(file[10:-10])
            ga_metrics['fitness'].append(df['fitness'].iloc[-1])
            ga_metrics['total time'].append(df['time'].iloc[-1])

            
ga_list=[file[10:-10] for file in file_list]

ax_time.legend(ga_list)
ax_fit.legend(ga_list)

f_fit.savefig('FIT_Cont_Peaks_GA_plot.png')
f_time.savefig('TIME_Cont_Peaks_GA_plot.png')

df_ga = pd.DataFrame(ga_metrics)
df_ga


# In[7]:


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
            ax_fit.set_title('Cont_Peaks Fitness - SA')
            ax_fit.set_xlabel('iterations')
            ax_fit.set_ylabel('fitness')
            
            ax_time.plot(df['iterations'],df['time'])
            ax_time.set_title('Cont_Peaks time - SA')
            ax_time.set_xlabel('iterations')
            ax_time.set_ylabel('time')
            
            sa_metrics['method'].append(file[10:-10])
            sa_metrics['fitness'].append(df['fitness'].iloc[-1])
            sa_metrics['total time'].append(df['time'].iloc[-1])

            
sa_list=[file[10:-10] for file in file_list]
ax_time.legend(sa_list)
ax_fit.legend(sa_list)

f_fit.savefig('FIT_Cont_Peaks_SA_plot.png')
f_time.savefig('TIME_Cont_Peaks_SA_plot.png')

df_sa = pd.DataFrame(sa_metrics)
df_sa


# In[10]:


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
            ax_fit.set_title('Cont_Peaks Fitness - MIMIC')
            ax_fit.set_xlabel('iterations')
            ax_fit.set_ylabel('fitness')
            
            ax_time.plot(df['iterations'],df['time'])
            ax_time.set_title('Cont_Peaks time - MIMIC')
            ax_time.set_xlabel('iterations')
            ax_time.set_ylabel('time')
            
            MIMIC_metrics['method'].append(file[10:-10])
            MIMIC_metrics['fitness'].append(df['fitness'].iloc[-1])
            MIMIC_metrics['total time'].append(df['time'].iloc[-1])

            
sa_list=[file[10:-10] for file in file_list]
ax_time.legend(sa_list)
ax_fit.legend(sa_list)

f_fit.savefig('FIT_Cont_Peaks_MIMIC_plot.png')
f_time.savefig('TIME_Cont_Peaks_MIMIC_plot.png')

df_MIMIC = pd.DataFrame(MIMIC_metrics)
df_MIMIC


# In[11]:


f_fit=plt.figure(figsize=(8,6))
ax_fit = f_fit.add_subplot(1, 1, 1)

f_time=plt.figure(figsize=(8,6))
ax_time = f_time.add_subplot(1, 1, 1)


overall_file_list=['CONTPEAKS_GA100_50_50_1_LOG.txt',
                   'CONTPEAKS_SA0.4_1_LOG.txt',
                   'CONTPEAKS_MIMIC200_40_0.8_1_LOG.txt',
                   'CONTPEAKS_RHC_1_LOG.txt']

overall_metrics={'method':[],'fitness':[],'total time':[]}
file_list=[]
for dirpath, dirnames, filenames in os.walk('./'):
    for file in filenames:
        if file in overall_file_list:
            print(file)
            file_list.append(file)
            df=pd.read_csv(file)
            ax_fit.plot(df['iterations'],df['fitness'])
            ax_fit.set_title('CONTPEAKS Fitness - 4 model comparison')
            ax_fit.set_xlabel('iterations')
            ax_fit.set_ylabel('fitness')
            
            ax_time.plot(df['iterations'],df['time'])
            ax_time.set_title('CONTPEAKS time - 4 model comparison')
            ax_time.set_xlabel('iterations')
            ax_time.set_ylabel('time')
            
            overall_metrics['method'].append(file[10:-10])
            overall_metrics['fitness'].append(df['fitness'].iloc[-1])
            overall_metrics['total time'].append(df['time'].iloc[-1])

            
sa_list=[file[10:-10] for file in file_list]
ax_time.legend(sa_list)
ax_fit.legend(sa_list)

f_fit.savefig('FIT_CONTPEAKS_Overall_plot.png')
f_time.savefig('TIME_CONTPEAKS_Overall_plot.png')

df_overall = pd.DataFrame(overall_metrics)
df_overall


# In[ ]:




