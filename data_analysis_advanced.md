```python
# Q.1) which location has heighest and lowest sales?

# Q.2) represent sales on a bar chart, also show the market share for each location using pie chart?
```


```python
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('sales.csv')

sales
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Invoice ID</th>
      <th>Date</th>
      <th>Time</th>
      <th>Gender</th>
      <th>Location</th>
      <th>City</th>
      <th>Member</th>
      <th>Category</th>
      <th>Price</th>
      <th>Quantity</th>
      <th>Total</th>
      <th>Payment</th>
      <th>Rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>460489604</td>
      <td>1/25/2018</td>
      <td>16:46</td>
      <td>Male</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>Yes</td>
      <td>Groceries</td>
      <td>30</td>
      <td>1</td>
      <td>30</td>
      <td>Cash</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>471006167</td>
      <td>3/19/2018</td>
      <td>16:48</td>
      <td>Female</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>Yes</td>
      <td>Fashion</td>
      <td>35</td>
      <td>5</td>
      <td>175</td>
      <td>Card</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>411909258</td>
      <td>2/25/2018</td>
      <td>13:33</td>
      <td>Male</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>No</td>
      <td>Clothing</td>
      <td>57</td>
      <td>2</td>
      <td>114</td>
      <td>Cash</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>487313402</td>
      <td>1/22/2018</td>
      <td>13:38</td>
      <td>Female</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>Yes</td>
      <td>Sporting</td>
      <td>89</td>
      <td>4</td>
      <td>356</td>
      <td>Gpay</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>197763430</td>
      <td>2/18/2018</td>
      <td>15:31</td>
      <td>Female</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>No</td>
      <td>Books</td>
      <td>82</td>
      <td>5</td>
      <td>410</td>
      <td>Cash</td>
      <td>4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>995</th>
      <td>818829599</td>
      <td>3/26/2018</td>
      <td>11:19</td>
      <td>Male</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>No</td>
      <td>Groceries</td>
      <td>31</td>
      <td>4</td>
      <td>124</td>
      <td>Card</td>
      <td>3</td>
    </tr>
    <tr>
      <th>996</th>
      <td>556589713</td>
      <td>2/20/2018</td>
      <td>17:17</td>
      <td>Male</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>Yes</td>
      <td>Groceries</td>
      <td>3</td>
      <td>5</td>
      <td>15</td>
      <td>Gpay</td>
      <td>3</td>
    </tr>
    <tr>
      <th>997</th>
      <td>82324424</td>
      <td>2/6/2018</td>
      <td>11:44</td>
      <td>Male</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>No</td>
      <td>Clothing</td>
      <td>71</td>
      <td>5</td>
      <td>355</td>
      <td>Card</td>
      <td>3</td>
    </tr>
    <tr>
      <th>998</th>
      <td>783661702</td>
      <td>1/29/2018</td>
      <td>15:44</td>
      <td>Female</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>No</td>
      <td>Clothing</td>
      <td>89</td>
      <td>7</td>
      <td>623</td>
      <td>Cash</td>
      <td>5</td>
    </tr>
    <tr>
      <th>999</th>
      <td>759171975</td>
      <td>1/31/2018</td>
      <td>10:13</td>
      <td>Female</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>Yes</td>
      <td>Clothing</td>
      <td>31</td>
      <td>7</td>
      <td>217</td>
      <td>Gpay</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
<p>1000 rows × 13 columns</p>
</div>




```python
# which location has heighest and lowest sales?

location_list = sales.groupby('Location')

print("OBJECT: ", location_list)

location = [x for x, y in location_list]

print("LOCATIONS: ", location)

sales_group = sales.groupby('Location').sum()['Total']
```

    OBJECT:  <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001EADDF34160>
    LOCATIONS:  ['Brookfield', 'Park lane', 'Water tower']
    


```python
sales_group
```




    Location
    Brookfield     72141
    Park lane      70432
    Water tower    65215
    Name: Total, dtype: int64




```python
# BAR CHART REPRESENTATION

plt.bar(location, sales_group)
```




    <BarContainer object of 3 artists>




    
![png](output_4_1.png)
    



```python
# PIE CHART REPRESENTATION

plt.pie(sales_group)
```




    ([<matplotlib.patches.Wedge at 0x1eade0c0130>,
      <matplotlib.patches.Wedge at 0x1eade0c04f0>,
      <matplotlib.patches.Wedge at 0x1eade0c09d0>],
     [Text(0.5080357843151302, 0.9756534435214743, ''),
      Text(-1.0939745592878725, -0.11497679605427102, ''),
      Text(0.6072323961649048, -0.917207074246502, '')])




    
![png](output_5_1.png)
    



```python
# PIE CHART WITH PERCENTAGE

plt.pie(sales_group, labels=location, autopct='%1.1f%%')
```




    ([<matplotlib.patches.Wedge at 0x1eade103640>,
      <matplotlib.patches.Wedge at 0x1eade103c40>,
      <matplotlib.patches.Wedge at 0x1eade1103a0>],
     [Text(0.5080357843151302, 0.9756534435214743, 'Brookfield'),
      Text(-1.0939745592878725, -0.11497679605427102, 'Park lane'),
      Text(0.6072323961649048, -0.917207074246502, 'Water tower')],
     [Text(0.2771104278082528, 0.5321746055571678, '34.7%'),
      Text(-0.596713395975203, -0.06271461602960236, '33.9%'),
      Text(0.33121767063540253, -0.5002947677708193, '31.4%')])




    
![png](output_6_1.png)
    



```python
# Q.3) which location has more female customers and which location has more male customers

```


```python
# STEP 1:
location_sales = sales.groupby(['Location', 'Gender']).count()['Invoice ID']
print('total sales count - group by Location & Gender: \n\n', location_sales)
```

    total sales count - group by Location & Gender: 
    
     Location     Gender
    Brookfield   Female    179
                 Male      161
    Park lane    Female    179
                 Male      153
    Water tower  Female    143
                 Male      185
    Name: Invoice ID, dtype: int64
    


```python
# STEP 2:
unstacked_sales = location_sales.unstack(level=0)
print('unstacked sales : \n\n', unstacked_sales)
```

    unstacked sales : 
    
     Location  Brookfield  Park lane  Water tower
    Gender                                      
    Female           179        179          143
    Male             161        153          185
    


```python
# STEP 3:
# Unstacked location list with plot()
unstacked_sales.plot()
```




    <AxesSubplot:xlabel='Gender'>




    
![png](output_10_1.png)
    



```python
# bar       x - label : GENDER
unstacked_sales.plot(kind='bar')
```




    <AxesSubplot:xlabel='Gender'>




    
![png](output_11_1.png)
    



```python
# bar : x - label : LOCATION
location_sales_1 = sales.groupby(['Gender', 'Location']).count()['Invoice ID']
unstacked_sales_1 = location_sales_1.unstack(level=0)
unstacked_sales_1.plot(kind='bar')
```




    <AxesSubplot:xlabel='Location'>




    
![png](output_12_1.png)
    



```python
# Q.4) what days of the month make most sales

```


```python
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
```




    0      2018
    1      2018
    2      2018
    3      2018
    4      2018
           ... 
    995    2018
    996    2018
    997    2018
    998    2018
    999    2018
    Name: Date, Length: 1000, dtype: int64




```python
sales.head(1)


# 
sales['Day'] = pd.to_datetime(sales['Date']).dt.day
sales.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Invoice ID</th>
      <th>Date</th>
      <th>Time</th>
      <th>Gender</th>
      <th>Location</th>
      <th>City</th>
      <th>Member</th>
      <th>Category</th>
      <th>Price</th>
      <th>Quantity</th>
      <th>Total</th>
      <th>Payment</th>
      <th>Rating</th>
      <th>Day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>460489604</td>
      <td>1/25/2018</td>
      <td>16:46</td>
      <td>Male</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>Yes</td>
      <td>Groceries</td>
      <td>30</td>
      <td>1</td>
      <td>30</td>
      <td>Cash</td>
      <td>2</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>471006167</td>
      <td>3/19/2018</td>
      <td>16:48</td>
      <td>Female</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>Yes</td>
      <td>Fashion</td>
      <td>35</td>
      <td>5</td>
      <td>175</td>
      <td>Card</td>
      <td>3</td>
      <td>19</td>
    </tr>
    <tr>
      <th>2</th>
      <td>411909258</td>
      <td>2/25/2018</td>
      <td>13:33</td>
      <td>Male</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>No</td>
      <td>Clothing</td>
      <td>57</td>
      <td>2</td>
      <td>114</td>
      <td>Cash</td>
      <td>5</td>
      <td>25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>487313402</td>
      <td>1/22/2018</td>
      <td>13:38</td>
      <td>Female</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>Yes</td>
      <td>Sporting</td>
      <td>89</td>
      <td>4</td>
      <td>356</td>
      <td>Gpay</td>
      <td>1</td>
      <td>22</td>
    </tr>
    <tr>
      <th>4</th>
      <td>197763430</td>
      <td>2/18/2018</td>
      <td>15:31</td>
      <td>Female</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>No</td>
      <td>Books</td>
      <td>82</td>
      <td>5</td>
      <td>410</td>
      <td>Cash</td>
      <td>4</td>
      <td>18</td>
    </tr>
    <tr>
      <th>5</th>
      <td>263634050</td>
      <td>3/9/2018</td>
      <td>17:55</td>
      <td>Male</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>Yes</td>
      <td>Clothing</td>
      <td>52</td>
      <td>4</td>
      <td>208</td>
      <td>Gpay</td>
      <td>3</td>
      <td>9</td>
    </tr>
    <tr>
      <th>6</th>
      <td>99646662</td>
      <td>3/4/2018</td>
      <td>13:21</td>
      <td>Male</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>No</td>
      <td>Clothing</td>
      <td>81</td>
      <td>3</td>
      <td>243</td>
      <td>Cash</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7</th>
      <td>188869875</td>
      <td>3/8/2018</td>
      <td>13:24</td>
      <td>Male</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>No</td>
      <td>Books</td>
      <td>80</td>
      <td>2</td>
      <td>160</td>
      <td>Cash</td>
      <td>3</td>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>325637547</td>
      <td>1/18/2018</td>
      <td>15:33</td>
      <td>Male</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>Yes</td>
      <td>Clothing</td>
      <td>91</td>
      <td>3</td>
      <td>273</td>
      <td>Card</td>
      <td>3</td>
      <td>18</td>
    </tr>
    <tr>
      <th>9</th>
      <td>562942936</td>
      <td>2/24/2018</td>
      <td>16:05</td>
      <td>Female</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>No</td>
      <td>Books</td>
      <td>80</td>
      <td>2</td>
      <td>160</td>
      <td>Cash</td>
      <td>4</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>




```python

day_sales = sales.groupby('Day').sum()['Total']
print(day_sales)
```

    Day
    1     6301
    2     8247
    3     8533
    4     6593
    5     9177
    6     5976
    7     6164
    8     8313
    9     9142
    10    6444
    11    4755
    12    7714
    13    5688
    14    7978
    15    9677
    16    5912
    17    5833
    18    4625
    19    7481
    20    7333
    21    4300
    22    5788
    23    6949
    24    7819
    25    8638
    26    7165
    27    8154
    28    6467
    29    4662
    30    3530
    31    2430
    Name: Total, dtype: int64
    


```python
day_sales.plot()
```




    <AxesSubplot:xlabel='Day'>




    
![png](output_17_1.png)
    



```python
# Q.5) Which branch has more members and which branch has less members
```


```python
sales.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Invoice ID</th>
      <th>Date</th>
      <th>Time</th>
      <th>Gender</th>
      <th>Location</th>
      <th>City</th>
      <th>Member</th>
      <th>Category</th>
      <th>Price</th>
      <th>Quantity</th>
      <th>Total</th>
      <th>Payment</th>
      <th>Rating</th>
      <th>Day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>460489604</td>
      <td>1/25/2018</td>
      <td>16:46</td>
      <td>Male</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>Yes</td>
      <td>Groceries</td>
      <td>30</td>
      <td>1</td>
      <td>30</td>
      <td>Cash</td>
      <td>2</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>471006167</td>
      <td>3/19/2018</td>
      <td>16:48</td>
      <td>Female</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>Yes</td>
      <td>Fashion</td>
      <td>35</td>
      <td>5</td>
      <td>175</td>
      <td>Card</td>
      <td>3</td>
      <td>19</td>
    </tr>
    <tr>
      <th>2</th>
      <td>411909258</td>
      <td>2/25/2018</td>
      <td>13:33</td>
      <td>Male</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>No</td>
      <td>Clothing</td>
      <td>57</td>
      <td>2</td>
      <td>114</td>
      <td>Cash</td>
      <td>5</td>
      <td>25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>487313402</td>
      <td>1/22/2018</td>
      <td>13:38</td>
      <td>Female</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>Yes</td>
      <td>Sporting</td>
      <td>89</td>
      <td>4</td>
      <td>356</td>
      <td>Gpay</td>
      <td>1</td>
      <td>22</td>
    </tr>
    <tr>
      <th>4</th>
      <td>197763430</td>
      <td>2/18/2018</td>
      <td>15:31</td>
      <td>Female</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>No</td>
      <td>Books</td>
      <td>82</td>
      <td>5</td>
      <td>410</td>
      <td>Cash</td>
      <td>4</td>
      <td>18</td>
    </tr>
    <tr>
      <th>5</th>
      <td>263634050</td>
      <td>3/9/2018</td>
      <td>17:55</td>
      <td>Male</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>Yes</td>
      <td>Clothing</td>
      <td>52</td>
      <td>4</td>
      <td>208</td>
      <td>Gpay</td>
      <td>3</td>
      <td>9</td>
    </tr>
    <tr>
      <th>6</th>
      <td>99646662</td>
      <td>3/4/2018</td>
      <td>13:21</td>
      <td>Male</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>No</td>
      <td>Clothing</td>
      <td>81</td>
      <td>3</td>
      <td>243</td>
      <td>Cash</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7</th>
      <td>188869875</td>
      <td>3/8/2018</td>
      <td>13:24</td>
      <td>Male</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>No</td>
      <td>Books</td>
      <td>80</td>
      <td>2</td>
      <td>160</td>
      <td>Cash</td>
      <td>3</td>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>325637547</td>
      <td>1/18/2018</td>
      <td>15:33</td>
      <td>Male</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>Yes</td>
      <td>Clothing</td>
      <td>91</td>
      <td>3</td>
      <td>273</td>
      <td>Card</td>
      <td>3</td>
      <td>18</td>
    </tr>
    <tr>
      <th>9</th>
      <td>562942936</td>
      <td>2/24/2018</td>
      <td>16:05</td>
      <td>Female</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>No</td>
      <td>Books</td>
      <td>80</td>
      <td>2</td>
      <td>160</td>
      <td>Cash</td>
      <td>4</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>




```python
members = sales.groupby(['Member', 'Location']).count()['Invoice ID']
members
```




    Member  Location   
    No      Brookfield     173
            Park lane      167
            Water tower    159
    Yes     Brookfield     167
            Park lane      165
            Water tower    169
    Name: Invoice ID, dtype: int64




```python
members.unstack(level=0)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Member</th>
      <th>No</th>
      <th>Yes</th>
    </tr>
    <tr>
      <th>Location</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Brookfield</th>
      <td>173</td>
      <td>167</td>
    </tr>
    <tr>
      <th>Park lane</th>
      <td>167</td>
      <td>165</td>
    </tr>
    <tr>
      <th>Water tower</th>
      <td>159</td>
      <td>169</td>
    </tr>
  </tbody>
</table>
</div>




```python
members.unstack(level=0).plot(kind='bar')
```




    <AxesSubplot:xlabel='Location'>




    
![png](output_22_1.png)
    



```python
# Q.6) Which branch has highest rating and which branch has lowest

```


```python
rating = sales.groupby(['Location']).mean()['Rating']
rating
```




    Location
    Brookfield     2.782353
    Park lane      3.021084
    Water tower    3.118902
    Name: Rating, dtype: float64




```python
rating.plot(kind='bar')
```




    <AxesSubplot:xlabel='Location'>




    
![png](output_25_1.png)
    



```python
# Q.7) Which city has more female shopping

```


```python
female_shoppers = sales.groupby(['City', 'Gender']).count()['Invoice ID']
female_shoppers
```




    City     Gender
    Chicago  Female    143
             Male      185
    Dallas   Female    179
             Male      153
    NewYork  Female    179
             Male      161
    Name: Invoice ID, dtype: int64




```python
unstack_female_shoppers = female_shoppers.unstack(level=0)
unstack_female_shoppers
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>City</th>
      <th>Chicago</th>
      <th>Dallas</th>
      <th>NewYork</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>143</td>
      <td>179</td>
      <td>179</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>185</td>
      <td>153</td>
      <td>161</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Categorized by gender
unstack_female_shoppers.plot(kind='bar')
```




    <AxesSubplot:xlabel='Gender'>




    
![png](output_29_1.png)
    



```python
# categorized by city
female_shoppers_1 = sales.groupby(['Gender', 'City']).count()['Invoice ID']
print(female_shoppers_1.unstack(level=0))

female_shoppers_1.unstack(level=0).plot(kind='bar')
```

    Gender   Female  Male
    City                 
    Chicago     143   185
    Dallas      179   153
    NewYork     179   161
    




    <AxesSubplot:xlabel='City'>




    
![png](output_30_2.png)
    



```python
# Q.8) Who spends more men / women
```


```python
spend = sales.groupby('Gender').sum()['Total']
print(spend)

spend.plot(kind='bar')
```

    Gender
    Female    106452
    Male      101336
    Name: Total, dtype: int64
    




    <AxesSubplot:xlabel='Gender'>




    
![png](output_32_2.png)
    



```python
# Q.9) Which type of customer spends more memeber or non-member
```


```python
member_spends = sales.groupby('Member').sum()['Total']
print(member_spends)

member_spends.plot(kind='bar')
```

    Member
    No     100245
    Yes    107543
    Name: Total, dtype: int64
    




    <AxesSubplot:xlabel='Member'>




    
![png](output_34_2.png)
    



```python
# Q.10) Which product line sells more
```


```python
most_sell = sales.groupby('Category').count()['Invoice ID']
print(most_sell)

most_sell.plot(kind='bar')
```

    Category
    Books        165
    Clothing     170
    Fashion      153
    Furniture    160
    Groceries    174
    Sporting     178
    Name: Invoice ID, dtype: int64
    




    <AxesSubplot:xlabel='Category'>




    
![png](output_36_2.png)
    



```python
# Q.11) Which product line is popular among men vs women
```


```python
most_sell_gender = sales.groupby(['Gender', 'Category']).count()['Invoice ID']
print(most_sell_gender)

unstack_most_sell_gender = most_sell_gender.unstack(level=0)
print('\n\n', unstack_most_sell_gender)

unstack_most_sell_gender.plot(kind='bar')
```

    Gender  Category 
    Female  Books        88
            Clothing     81
            Fashion      81
            Furniture    78
            Groceries    87
            Sporting     86
    Male    Books        77
            Clothing     89
            Fashion      72
            Furniture    82
            Groceries    87
            Sporting     92
    Name: Invoice ID, dtype: int64
    
    
     Gender     Female  Male
    Category               
    Books          88    77
    Clothing       81    89
    Fashion        81    72
    Furniture      78    82
    Groceries      87    87
    Sporting       86    92
    




    <AxesSubplot:xlabel='Category'>




    
![png](output_38_2.png)
    



```python
# Q.12) Which month may makes more sales
```


```python
sales.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Invoice ID</th>
      <th>Date</th>
      <th>Time</th>
      <th>Gender</th>
      <th>Location</th>
      <th>City</th>
      <th>Member</th>
      <th>Category</th>
      <th>Price</th>
      <th>Quantity</th>
      <th>Total</th>
      <th>Payment</th>
      <th>Rating</th>
      <th>Day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>460489604</td>
      <td>1/25/2018</td>
      <td>16:46</td>
      <td>Male</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>Yes</td>
      <td>Groceries</td>
      <td>30</td>
      <td>1</td>
      <td>30</td>
      <td>Cash</td>
      <td>2</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>




```python
sales['Month'] = pd.to_datetime(sales['Date']).dt.month
sales.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Invoice ID</th>
      <th>Date</th>
      <th>Time</th>
      <th>Gender</th>
      <th>Location</th>
      <th>City</th>
      <th>Member</th>
      <th>Category</th>
      <th>Price</th>
      <th>Quantity</th>
      <th>Total</th>
      <th>Payment</th>
      <th>Rating</th>
      <th>Day</th>
      <th>Month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>460489604</td>
      <td>1/25/2018</td>
      <td>16:46</td>
      <td>Male</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>Yes</td>
      <td>Groceries</td>
      <td>30</td>
      <td>1</td>
      <td>30</td>
      <td>Cash</td>
      <td>2</td>
      <td>25</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>471006167</td>
      <td>3/19/2018</td>
      <td>16:48</td>
      <td>Female</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>Yes</td>
      <td>Fashion</td>
      <td>35</td>
      <td>5</td>
      <td>175</td>
      <td>Card</td>
      <td>3</td>
      <td>19</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>411909258</td>
      <td>2/25/2018</td>
      <td>13:33</td>
      <td>Male</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>No</td>
      <td>Clothing</td>
      <td>57</td>
      <td>2</td>
      <td>114</td>
      <td>Cash</td>
      <td>5</td>
      <td>25</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>487313402</td>
      <td>1/22/2018</td>
      <td>13:38</td>
      <td>Female</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>Yes</td>
      <td>Sporting</td>
      <td>89</td>
      <td>4</td>
      <td>356</td>
      <td>Gpay</td>
      <td>1</td>
      <td>22</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>197763430</td>
      <td>2/18/2018</td>
      <td>15:31</td>
      <td>Female</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>No</td>
      <td>Books</td>
      <td>82</td>
      <td>5</td>
      <td>410</td>
      <td>Cash</td>
      <td>4</td>
      <td>18</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>263634050</td>
      <td>3/9/2018</td>
      <td>17:55</td>
      <td>Male</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>Yes</td>
      <td>Clothing</td>
      <td>52</td>
      <td>4</td>
      <td>208</td>
      <td>Gpay</td>
      <td>3</td>
      <td>9</td>
      <td>3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>99646662</td>
      <td>3/4/2018</td>
      <td>13:21</td>
      <td>Male</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>No</td>
      <td>Clothing</td>
      <td>81</td>
      <td>3</td>
      <td>243</td>
      <td>Cash</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>188869875</td>
      <td>3/8/2018</td>
      <td>13:24</td>
      <td>Male</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>No</td>
      <td>Books</td>
      <td>80</td>
      <td>2</td>
      <td>160</td>
      <td>Cash</td>
      <td>3</td>
      <td>8</td>
      <td>3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>325637547</td>
      <td>1/18/2018</td>
      <td>15:33</td>
      <td>Male</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>Yes</td>
      <td>Clothing</td>
      <td>91</td>
      <td>3</td>
      <td>273</td>
      <td>Card</td>
      <td>3</td>
      <td>18</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>562942936</td>
      <td>2/24/2018</td>
      <td>16:05</td>
      <td>Female</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>No</td>
      <td>Books</td>
      <td>80</td>
      <td>2</td>
      <td>160</td>
      <td>Cash</td>
      <td>4</td>
      <td>24</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
month_sales = sales.groupby('Month').sum()['Total']
month_sales
```




    Month
    1    71652
    2    63850
    3    72286
    Name: Total, dtype: int64




```python
month_sales.plot(kind='bar')
```




    <AxesSubplot:xlabel='Month'>




    
![png](output_43_1.png)
    



```python
plt.grid(month_sales.plot(kind='bar'))
```


    
![png](output_44_0.png)
    



```python

```
