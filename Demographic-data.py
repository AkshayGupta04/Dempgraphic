#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import pandas as pd


# In[4]:


stats=pd.read_csv(r'C:\Users\aksha\OneDrive\Desktop\python\DemographicData.csv') # read csv into dataframe


# In[5]:


stats


# In[6]:


stats.describe()


# In[7]:


stats.head() #top 5 of Data frame


# In[8]:


stats.tail()#bottom 5 of Data frame


# In[9]:


stats.head(20)#top 5 of Data frame


# In[10]:


stats.head(-10) # excluding 10 data


# In[11]:


stats.tail(10)


# In[12]:


stats.tail().describe()


# In[13]:


len(stats) # length of dataframe or row count


# In[14]:


stats.columns #Name of  all column


# In[15]:


len(stats.columns)# number of column


# In[16]:


stats.describe().transpose() #transposing the descriptive dataframe of stats


# In[17]:


stats.InternetUsers # All Internet user data


# In[18]:


stats.InternetUsers<5 # Return boolena result


# In[19]:


stats[stats.InternetUsers<2] # list of dataframe having internet users less than 2


# In[20]:


stats[stats.IncomeGroup=='Lower middle income']


# In[21]:


stats.IncomeGroup.unique() # Unique value


# In[22]:


import seaborn as sns


# In[23]:


plt.rcParams['figure.figsize']=8,4


# In[24]:


vis1=sns.distplot(stats['InternetUsers'])
# Distribution Plot-Flexibly plot a univariate distribution of observations.


# In[24]:


import warnings


# In[25]:


warnings.filterwarnings('ignore')


# In[26]:


vis1=sns.distplot(stats['InternetUsers'],bins=10,color='red')# Bins means number of bin


# In[28]:


vis2=sns.boxplot(data=stats,x='IncomeGroup',y='InternetUsers')


# In[27]:


sns.relplot(data=stats,x='IncomeGroup',y='InternetUsers')


# In[29]:


vis3=sns.lmplot(data=stats,x='BirthRate',y='InternetUsers',
                fit_reg=True,hue='IncomeGroup',markers=["o","1","2","p"],
                hue_order=['Low income','High income','Upper middle income','Lower middle income'])


# In[30]:


vis4=sns.lineplot(data=stats,x='IncomeGroup',y='InternetUsers') #Draw a line plot with possibility of several semantic groupings.


# In[31]:


vis5=sns.scatterplot(data=stats,x='IncomeGroup',y='InternetUsers')#Draw a scatter plot with possibility of several semantic groupings.


# In[32]:


vis6=sns.kdeplot(data=stats)


# In[33]:


vis7=sns.histplot(data=stats)#A histogram is a classic visualization tool that represents the distribution
#of one or more variables by counting the number of observations that fall within
#disrete bins


# In[34]:


vis8=sns.distplot(stats['InternetUsers'])#plot a univariate distribution of observations.


# In[35]:


vis9=sns.ecdfplot(data=stats)#the proportion or count of observations falling below each
#unique value in a dataset.


# In[36]:


sns.rugplot(data=stats)
sns.ecdfplot(data=stats)


# In[37]:


vis10=sns.boxplot(data=stats,x='IncomeGroup',y='InternetUsers')


# In[38]:


vis11=sns.lmplot(data=stats,x='BirthRate',y='InternetUsers',hue='IncomeGroup',fit_reg=True,legend_out=False,legend=True,markers=["o","1","2","p"],hue_order=['Low income','High income','Upper middle income','Lower middle income'])


# In[ ]:




