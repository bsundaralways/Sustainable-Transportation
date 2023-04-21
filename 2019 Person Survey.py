#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

# set the file path
file_path = "Citywide_Mobility_Survey_-_Person_Survey_2019.csv"

# use pandas to read the csv file
df = pd.read_csv(file_path)

# print the first few rows of the data
print(df.head())


# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


df.head()


# In[8]:


df.shape


# In[9]:


unique_values = df["hh_id"].unique()


# In[10]:


unique_values


# In[13]:


# check for null values in the 'age' column
null_values = df['hh_id'].isnull().sum()
print(f"Number of null values in the 'hh_id' column: {null_values}")


# In[15]:


df.info()


# In[17]:


df.dtypes


# In[18]:


#Checking Null values
df.isnull().sum()*100/df.shape[0]


# In[20]:


df.describe()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




