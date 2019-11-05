#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[17]:


df=pd.read_csv("https://raw.githubusercontent.com/bernardoalbz/minist-rio/master/AB_NYC_2019.csv",sep=',',encoding = "ISO-8859-1")


# In[18]:


df.head()


# In[19]:


df


# In[24]:


df.drop("host_name", axis=1)


# In[41]:





# In[ ]:




