#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt


# In[3]:


df = pd.read_csv('Car_sales.csv')
df


# In[4]:


df.describe()


# In[13]:


manufacturer = df['Manufacturer']
sales = df['Sales_in_thousands']


# In[19]:


plt.figure(figsize=(15, 10))
plt.barh(manufacturer , sales)
plt.xlabel('Car Manufacturers')
plt.ylabel('Sales in 1000s')
plt.title('Car Sales')
plt.show()


# In[ ]:


(

