#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


supermarket_df = pd.read_csv('C:\\Users\\Jadhav\\Downloads\\supermarket_sales - Sheet1.csv')
supermarket_df.head(20)


# In[3]:


supermarket_df.dtypes


# In[4]:


supermarket_df['Date']


# In[5]:


supermarket_df.describe().T


# In[6]:


supermarket_df.corr()


# In[7]:


np.round(supermarket_df.corr(),2)


# In[8]:


plt.figure(figsize = (18,9))
sns.heatmap(np.round(supermarket_df.corr(),2),annot = True)


# In[9]:


sns.scatterplot(x = 'Tax 5%',y = 'gross income',data = supermarket_df)


# In[10]:


sns.scatterplot(x = 'Quantity',y = 'cogs',data = supermarket_df,color = 'purple')


# In[11]:


sns.regplot(x = 'Quantity',y = 'cogs',data = supermarket_df,color = 'green')


# In[12]:


supermarket_df.info()


# In[13]:


supermarket_df.isnull().sum()


# In[14]:


supermarket_df.drop(['Invoice ID','Date','Time'], axis = 1, inplace = True)


# In[15]:


supermarket_df['gross margin percentage'].unique()


# In[16]:


supermarket_df.drop(['gross margin percentage'], axis = 1)


# In[17]:


print(supermarket_df.shape)
supermarket_df['Gender'].value_counts()


# In[18]:


sns.countplot('Gender', data = supermarket_df)


# In[19]:


gender_dummies = pd.get_dummies(supermarket_df['Gender'])
gender_dummies.head()


# In[20]:


supermarket_df = pd.concat([supermarket_df, gender_dummies], axis = 1)
supermarket_df.head(20)


# In[21]:


plt.figure(figsize = (17,8))
sns.barplot(x = 'Product line', y = 'Female',data = supermarket_df)


# In[22]:


plt.figure(figsize = (20,8))
sns.barplot(x = 'Product line', y = 'Male',data = supermarket_df)


# In[23]:


supermarket_df = pd.DataFrame(supermarket_df['City']. value_counts())
supermarket_df


# In[24]:


sns.barplot(x = supermarket_df.index , y = supermarket_df['City'], palette = 'hot')
supermarket_df


# In[ ]:





# In[ ]:




