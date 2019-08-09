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


# # SA

# In[85]:


f_mse=plt.figure(figsize=(7,5))
ax_mse = f_mse.add_subplot(1, 1, 1)

f_acc=plt.figure(figsize=(7,5))
ax_acc = f_acc.add_subplot(1, 1, 1)

f_time=plt.figure(figsize=(7,5))
ax_time = f_time.add_subplot(1, 1, 1)
xlim=1000
file_list=[]

sa_metrics={'method':[],'test acc':[],'test mse':[],'total time':[]}
for dirpath, dirnames, filenames in os.walk('./'):
    for file in filenames:
        if 'SA_LOG' in file:
            df=pd.read_csv(file)
            ax_mse.plot(df['iteration'],df['MSE_tst'])
            ax_mse.set_xlim([0,xlim])
            ax_mse.set_title('MSE for test data set')
            ax_mse.set_xlabel('iterations')
            ax_mse.set_ylabel('MSE')
            
            ax_acc.plot(df['iteration'],df['acc_tst'])
            ax_acc.set_xlim([0,xlim])
            ax_acc.set_ylim([0,1])
            ax_acc.set_title('acccuracy for test data set')
            ax_acc.set_xlabel('iterations')
            ax_acc.set_ylabel('Accuracy') 
            
            ax_time.plot(df['iteration'],df['elapsed'])
            ax_time.set_xlim([0,xlim])
            ax_time.set_title('time elapsed')
            ax_time.set_xlabel('iterations')
            ax_time.set_xlabel('Time Elapsed')
            file_list.append(file)
            
            sa_metrics['method'].append(file.split('_')[2][:-4])
            sa_metrics['test acc'].append(df['acc_tst'].iloc[-1])
            sa_metrics['test mse'].append(df['MSE_tst'].iloc[-1])
            sa_metrics['total time'].append(df['elapsed'].iloc[-1])


sa_legend=[file.split('_')[2][:-4] for file in file_list]
ax_mse.legend(sa_legend)
ax_acc.legend(sa_legend)
ax_time.legend(sa_legend)
f_mse.savefig('MSE_NN_SA_plot.png')
f_acc.savefig('ACC_NN_SA_plot.png')
f_time.savefig('Time_NN_SA_plot.png')

            
df_sa = pd.DataFrame(sa_metrics)
df_sa


# # GA

# In[86]:


f_mse=plt.figure(figsize=(7,5))
ax_mse = f_mse.add_subplot(1, 1, 1)

f_acc=plt.figure(figsize=(7,5))
ax_acc = f_acc.add_subplot(1, 1, 1)

f_time=plt.figure(figsize=(7,5))
ax_time = f_time.add_subplot(1, 1, 1)
xlim=1000

ga_metrics={'method':[],'test acc':[],'test mse':[],'total time':[]}
file_list=[]
for dirpath, dirnames, filenames in os.walk('./'):
    for file in filenames:
        if 'GA_OUTPUT' in file:
            df=pd.read_csv(file)
            ax_mse.plot(df['iteration'],df['MSE_tst'])
            ax_mse.set_xlim([0,xlim])
            ax_mse.set_title('MSE for test data set')
            ax_mse.set_xlabel('iterations')
            ax_mse.set_ylabel('MSE')
            
            
            ax_acc.plot(df['iteration'],df['acc_tst'])
            ax_acc.set_xlim([0,xlim])
            ax_acc.set_ylim([0,1])
            ax_acc.set_title('acccuracy for test data set')
            ax_acc.set_xlabel('iterations')
            ax_acc.set_ylabel('Accuracy') 
            
            ax_time.plot(df['iteration'],df['elapsed'])
            ax_time.set_xlim([0,xlim])
            ax_time.set_title('time elapsed')
            ax_time.set_xlabel('iterations')
            ax_time.set_xlabel('Time Elapsed')
            file_list.append(file)

                        
            ga_metrics['method'].append(file[10:-4])
            ga_metrics['test acc'].append(df['acc_tst'].iloc[-1])
            ga_metrics['test mse'].append(df['MSE_tst'].iloc[-1])
            ga_metrics['total time'].append(df['elapsed'].iloc[-1])

ga_legend=[file[10:-4] for file in file_list]
ax_mse.legend(ga_legend)
ax_acc.legend(ga_legend)
ax_time.legend(ga_legend)

f_mse.savefig('MSE_NN_GA_plot.png')
f_acc.savefig('ACC_NN_GA_plot.png')
f_time.savefig('Time_NN_GA_plot.png')

df_ga = pd.DataFrame(ga_metrics)
df_ga


# In[89]:


f_mse=plt.figure(figsize=(7,5))
ax_mse = f_mse.add_subplot(1, 1, 1)

f_acc=plt.figure(figsize=(7,5))
ax_acc = f_acc.add_subplot(1, 1, 1)

f_time=plt.figure(figsize=(7,5))
ax_time = f_time.add_subplot(1, 1, 1)
xlim=1000
overall_metrics={'method':[],'test acc':[],'test mse':[],'total time':[]}

file_list=[]
for dirpath, dirnames, filenames in os.walk('./'):
    for file in filenames:
        if file in ['RHC_LOG.txt','BACKPROP_LOG.txt','GA_OUTPUT_GA_50_10_20.txt','SA_LOG_SA0.25.txt']:
            print(file)
            df=pd.read_csv(file)
            ax_mse.plot(df['iteration'],df['MSE_tst'])
            ax_mse.set_xlim([0,xlim])
            ax_mse.set_title('MSE for test data set')
            ax_mse.set_xlabel('iterations')
            ax_mse.set_ylabel('MSE')
            
            ax_acc.plot(df['iteration'],df['acc_tst'])
            ax_acc.set_xlim([0,xlim])
            ax_acc.set_ylim([0,1])
            ax_acc.set_title('acccuracy for test data set')
            ax_acc.set_xlabel('iterations')
            ax_acc.set_ylabel('Accuracy') 
            
            ax_time.plot(df['iteration'],df['elapsed'])
            ax_time.set_xlim([0,xlim])
            ax_time.set_title('time elapsed')
            ax_time.set_xlabel('iterations')
            ax_time.set_xlabel('Time Elapsed')
            file_list.append(file)
            
            overall_metrics['method'].append(file.split('_')[0])
            overall_metrics['test acc'].append(df['acc_tst'].iloc[-1])
            overall_metrics['test mse'].append(df['MSE_tst'].iloc[-1])
            overall_metrics['total time'].append(df['elapsed'].iloc[-1])
            
overall_legend = ['RHC','Best SA','Best GA','Backprop']
ax_mse.legend(overall_legend)
ax_acc.legend(overall_legend)
ax_time.legend(overall_legend)

f_mse.savefig('MSE_NN_OVERALL_plot.png')
f_acc.savefig('ACC_NN_OVERALL_plot.png')
f_time.savefig('Time_NN_OVERALL_plot.png')

df_overall = pd.DataFrame(overall_metrics)
df_overall


# In[ ]:




