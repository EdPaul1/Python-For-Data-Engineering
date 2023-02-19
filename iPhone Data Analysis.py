#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("apple_products.csv")


# In[3]:


df.head()


# In[4]:


df.count()


# In[6]:


df['Mrp'].max()


# In[7]:


df['Mrp'].min()


# ###  Finding out which iPhone is priced at 149900

# In[9]:


df[df['Mrp']==149900]


# ### Finding the cheapest iPhone available in out data

# In[11]:


df[df['Mrp']==39900]


# ### Extracting the iPhone model from the product name column

# In[22]:


list(df['Product Name'])[21][6:15].upper().strip()


# In[23]:


df['Model Name'] = df['Product Name'].str[6:15]


# In[24]:


df.head()


# ### Sorting the iPhones by the Star Rating

# In[27]:


df.sort_values(by=['Star Rating'], ascending = False)


# In[ ]:




