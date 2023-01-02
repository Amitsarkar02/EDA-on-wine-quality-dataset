#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


wine=pd.read_csv("wine_quality.csv")


# In[3]:


wine.head()


# In[5]:


wine.info()


# In[6]:


wine.isnull().sum()


# In[8]:


wine.shape


# In[9]:


wine.index


# In[16]:


plt.figure(figsize = (10,5))
plt.hist(data = wine,x = 'fixed acidity',color = 'Red',bins = 5)


# In[21]:


round(wine['fixed acidity'].mean(),2)


# In[20]:


wine['fixed acidity'].median()


# In[25]:


plt.figure(figsize = (10,5))
plt.hist(data = wine,x = 'fixed acidity',color = 'orange',bins = 5)
plt.title("histogram of Fixed")
plt.xlabel("Fixed Acidity")
plt.ylabel("count")
plt.vlines(wine['fixed acidity'].mean(), ymin = 0, ymax = 4000, colors='blue', label='Mean')
plt.vlines(wine['fixed acidity'].median(), ymin = 0, ymax = 4000, colors='red', label='Median')
plt.legend()
plt.show()


# # create a histogram of the "volatile acidity" feature 

# In[28]:


plt.figure(figsize = (10,5))
sns.histplot(data = wine,x = 'volatile acidity',color = 'green',bins = 5)
plt.title("volatile acidity")
plt.xlabel("volatile acidity")
plt.ylabel("count")
plt.show()


# In[32]:


plt.figure(figsize = (10,5))
sns.distplot(wine['volatile acidity'], color = 'blue')
plt.title("volatile acidity")
plt.xlabel("volatile acidity")
plt.ylabel("count")
plt.show()


# In[ ]:


# the plot above shows the normal disturbution 


# In[38]:



plt.figure(figsize = (11,6))

sns.histplot(data = wine ,x = 'volatile acidity', color = 'green', 
             edgecolor = 'linen', alpha = 0.5, bins = 5)

plt.title("Histogram of Volatile Acidity")                         
plt.xlabel('Volatile Acidity')                         
plt.ylabel('Density')
plt.vlines(wine['volatile acidity'].mean(), ymin = 0, ymax = 4000, colors='blue', label='Mean')
plt.vlines(wine['volatile acidity'].median(), ymin = 0, ymax = 4000, colors='red', label='Median')
plt.legend()
plt.show()


# In[40]:


# Create a histogram of the "citric acid" feature

plt.figure(figsize = (11,6))

sns.histplot(data = wine ,x = 'citric acid', color = 'red', 
             edgecolor = 'linen', alpha = 0.5, bins = 5)

plt.title("Histogram of Citric Acidity")                         
plt.xlabel('Citric Acidity')                         
plt.ylabel('Count')
plt.show()


# In[43]:


wine['citric acid'].mean()


# In[44]:


wine['citric acid'].median()


# In[47]:


plt.figure(figsize = (11,6))

sns.histplot(data = wine ,x = 'citric acid', color = 'yellow', 
             edgecolor = 'linen', alpha = 0.5, bins = 5)

plt.title("Histogram of Volatile Acidity")                         
plt.xlabel('Volatile Acidity')                         
plt.ylabel('count')
plt.vlines(wine['citric acid'].mean(), ymin = 0, ymax = 4000, colors='blue', label='Mean')
plt.vlines(wine['citric acid'].median(), ymin = 0, ymax = 4000, colors='red', label='Median')
plt.legend()
plt.show()


# In[ ]:


# We can safely choose the mean as the measure of the central tendency here.


# In[49]:


plt.figure(figsize = (11,6))

sns.distplot(wine['citric acid'], color = 'blue')

plt.title("Distplot of Citric Acid")                         
plt.xlabel('Citric Acid')                         
plt.ylabel('Density')
plt.show()


# In[51]:


plt.figure(figsize = (10,6))
sns.countplot(wine['quality'])

plt.title("Count Plot of Quality")                         
plt.xlabel('Quality')                         
plt.ylabel('Count')
plt.show()


# In[52]:


wine['quality'].value_counts()


# In[53]:


wine.head()


# In[59]:


rev_acid = pd.Series(index = ['fixed acidity','volatile acidity','citric acid','quality'],
         data = [wine['fixed acidity'].mean(),wine['volatile acidity'].mean(),wine['citric acid'].mean(),wine['quality'].value_counts().index[0]])


# In[60]:


rev_acid


# # obervations

# In[ ]:


The representative acid for the quality is as follows:

The mean value of the fixed acidity would be 6.854

The mean value of the volatile acidity would be 0.2782

The mean value of citric acid would be 0.3341

The quality would be 6

