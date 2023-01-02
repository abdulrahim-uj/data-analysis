#!/usr/bin/env python
# coding: utf-8

# In[155]:


# Q.1) which location has heighest and lowest sales?

# Q.2) represent sales on a bar chart, also show the market share for each location using pie chart?


# In[156]:


import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('sales.csv')

sales


# In[157]:


# which location has heighest and lowest sales?

location_list = sales.groupby('Location')

print("OBJECT: ", location_list)

location = [x for x, y in location_list]

print("LOCATIONS: ", location)

sales_group = sales.groupby('Location').sum()['Total']


# In[158]:


sales_group


# In[159]:


# BAR CHART REPRESENTATION

plt.bar(location, sales_group)


# In[160]:


# PIE CHART REPRESENTATION

plt.pie(sales_group)


# In[161]:


# PIE CHART WITH PERCENTAGE

plt.pie(sales_group, labels=location, autopct='%1.1f%%')


# In[162]:


# Q.3) which location has more female customers and which location has more male customers


# In[163]:


# STEP 1:
location_sales = sales.groupby(['Location', 'Gender']).count()['Invoice ID']
print('total sales count - group by Location & Gender: \n\n', location_sales)


# In[164]:


# STEP 2:
unstacked_sales = location_sales.unstack(level=0)
print('unstacked sales : \n\n', unstacked_sales)


# In[165]:


# STEP 3:
# Unstacked location list with plot()
unstacked_sales.plot()


# In[166]:


# bar       x - label : GENDER
unstacked_sales.plot(kind='bar')


# In[167]:


# bar : x - label : LOCATION
location_sales_1 = sales.groupby(['Gender', 'Location']).count()['Invoice ID']
unstacked_sales_1 = location_sales_1.unstack(level=0)
unstacked_sales_1.plot(kind='bar')


# In[168]:


# Q.4) what days of the month make most sales


# In[169]:


# EXTRACT DATE

# Default
sales['Date']

# Date yyyy-mm-dd
pd.to_datetime(sales['Date'])

# Date dd
pd.to_datetime(sales['Date']).dt.day

# Date mm
pd.to_datetime(sales['Date']).dt.month

# Date yyyy
pd.to_datetime(sales['Date']).dt.year


# In[170]:


sales.head(1)


# 
sales['Day'] = pd.to_datetime(sales['Date']).dt.day
sales.head(10)


# In[171]:



day_sales = sales.groupby('Day').sum()['Total']
print(day_sales)


# In[172]:


day_sales.plot()


# In[173]:


# Q.5) Which branch has more members and which branch has less members


# In[174]:


sales.head(10)


# In[175]:


members = sales.groupby(['Member', 'Location']).count()['Invoice ID']
members


# In[176]:


members.unstack(level=0)


# In[177]:


members.unstack(level=0).plot(kind='bar')


# In[178]:


# Q.6) Which branch has highest rating and which branch has lowest


# In[179]:


rating = sales.groupby(['Location']).mean()['Rating']
rating


# In[180]:


rating.plot(kind='bar')


# In[181]:


# Q.7) Which city has more female shopping


# In[182]:


female_shoppers = sales.groupby(['City', 'Gender']).count()['Invoice ID']
female_shoppers


# In[183]:


unstack_female_shoppers = female_shoppers.unstack(level=0)
unstack_female_shoppers


# In[184]:


# Categorized by gender
unstack_female_shoppers.plot(kind='bar')


# In[185]:


# categorized by city
female_shoppers_1 = sales.groupby(['Gender', 'City']).count()['Invoice ID']
print(female_shoppers_1.unstack(level=0))

female_shoppers_1.unstack(level=0).plot(kind='bar')


# In[186]:


# Q.8) Who spends more men / women


# In[187]:


spend = sales.groupby('Gender').sum()['Total']
print(spend)

spend.plot(kind='bar')


# In[188]:


# Q.9) Which type of customer spends more memeber or non-member


# In[189]:


member_spends = sales.groupby('Member').sum()['Total']
print(member_spends)

member_spends.plot(kind='bar')


# In[190]:


# Q.10) Which product line sells more


# In[191]:


most_sell = sales.groupby('Category').count()['Invoice ID']
print(most_sell)

most_sell.plot(kind='bar')


# In[192]:


# Q.11) Which product line is popular among men vs women


# In[193]:


most_sell_gender = sales.groupby(['Gender', 'Category']).count()['Invoice ID']
print(most_sell_gender)

unstack_most_sell_gender = most_sell_gender.unstack(level=0)
print('\n\n', unstack_most_sell_gender)

unstack_most_sell_gender.plot(kind='bar')


# In[194]:


# Q.12) Which month may makes more sales


# In[195]:


sales.head(1)


# In[196]:


sales['Month'] = pd.to_datetime(sales['Date']).dt.month
sales.head(10)


# In[197]:


month_sales = sales.groupby('Month').sum()['Total']
month_sales


# In[198]:


month_sales.plot(kind='bar')


# In[199]:


plt.grid(month_sales.plot(kind='bar'))


# In[ ]:




