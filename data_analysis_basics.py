#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd

sales = pd.read_csv('sales.csv')

sales


# In[34]:


# show first 10 rows
sales.head(10)


# In[35]:


# show selected coloumn

sales['Invoice ID'].head(5)


# In[36]:


# show unique category types

sales['Category'].unique()


# In[37]:


# selected index details

sales.iloc[200]


# In[38]:


# slicing: get detail from a range to next range

sales[200:210]


# In[39]:


# last 5 datasets

sales.tail()


# In[40]:


# last 10 rows

sales.tail(10)


# In[41]:


# view gender == male

sales[sales['Gender'] == 'Male']


# In[42]:


# view gender == female from first 10

sales[sales['Gender'] == 'Female'].head(10)


# In[43]:


# total > 200

sales[sales['Total'] > 200]


# In[44]:


# total < 50 from last 5 rows

sales[sales['Total'] < 50].tail(5)


# In[45]:


# city == NewYork

sales[sales['City'] == 'NewYork']


# In[46]:


# unique categories

sales['Category'].unique()


# In[47]:


# total in between 100 & 200

# data = sales[sales['Total'] > 100]
# data = data[data['Total'] < 200]
# data

# Simplified
sales[(sales['Total'] > 100) & (sales['Total'] < 200)]


# In[48]:


# With Arithmatic 

sales.sum()['Total']


# In[49]:


sales.sum()['Quantity']


# In[50]:


sales.max()


# In[51]:


sales.max()['Total']


# In[52]:


sales[sales['Total'] == sales.max()['Total']]


# In[53]:


sales.min()


# In[54]:


sales[sales['Total'] == sales.min()['Total']]


# In[55]:


sales.mean()['Total']


# In[56]:


sales['Total'].mean()


# In[57]:


# Group by
sales.groupby('City').sum()['Total']


# In[58]:


sales.groupby('Date').sum()['Total']


# In[59]:


sales.groupby('Category').sum()['Total']


# In[60]:


sales.groupby('Member').sum()['Total']


# In[61]:


# Group by gender base total

sales.groupby('Gender').sum()['Total']


# In[62]:


# Group by two coloumns base total
sales.groupby(['Payment', 'Gender']).sum()['Total']


# In[63]:



sales.groupby(['City', 'Payment']).sum()['Total']


# In[ ]:




