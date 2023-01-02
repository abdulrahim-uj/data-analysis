```python
import pandas as pd

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
# show first 10 rows
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
    </tr>
  </tbody>
</table>
</div>




```python
# show selected coloumn

sales['Invoice ID'].head(5)
```




    0    460489604
    1    471006167
    2    411909258
    3    487313402
    4    197763430
    Name: Invoice ID, dtype: int64




```python
# show unique category types

sales['Category'].unique()
```




    array(['Groceries', 'Fashion', 'Clothing', 'Sporting', 'Books',
           'Furniture'], dtype=object)




```python
# selected index details

sales.iloc[200]
```




    Invoice ID      576523018
    Date            2/15/2018
    Time                12:35
    Gender               Male
    Location      Water tower
    City              Chicago
    Member                 No
    Category        Groceries
    Price                  82
    Quantity                1
    Total                  82
    Payment              Card
    Rating                  4
    Name: 200, dtype: object




```python
# slicing: get detail from a range to next range

sales[200:210]
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
      <th>200</th>
      <td>576523018</td>
      <td>2/15/2018</td>
      <td>12:35</td>
      <td>Male</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>No</td>
      <td>Groceries</td>
      <td>82</td>
      <td>1</td>
      <td>82</td>
      <td>Card</td>
      <td>4</td>
    </tr>
    <tr>
      <th>201</th>
      <td>414119922</td>
      <td>1/30/2018</td>
      <td>11:07</td>
      <td>Male</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>No</td>
      <td>Sporting</td>
      <td>44</td>
      <td>7</td>
      <td>308</td>
      <td>Card</td>
      <td>3</td>
    </tr>
    <tr>
      <th>202</th>
      <td>123247697</td>
      <td>2/8/2018</td>
      <td>20:03</td>
      <td>Male</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>No</td>
      <td>Groceries</td>
      <td>22</td>
      <td>7</td>
      <td>154</td>
      <td>Card</td>
      <td>5</td>
    </tr>
    <tr>
      <th>203</th>
      <td>40419058</td>
      <td>1/26/2018</td>
      <td>14:53</td>
      <td>Male</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>Yes</td>
      <td>Books</td>
      <td>95</td>
      <td>6</td>
      <td>570</td>
      <td>Card</td>
      <td>1</td>
    </tr>
    <tr>
      <th>204</th>
      <td>890497298</td>
      <td>2/25/2018</td>
      <td>18:06</td>
      <td>Female</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>No</td>
      <td>Clothing</td>
      <td>69</td>
      <td>2</td>
      <td>138</td>
      <td>Cash</td>
      <td>2</td>
    </tr>
    <tr>
      <th>205</th>
      <td>885702268</td>
      <td>1/28/2018</td>
      <td>12:45</td>
      <td>Male</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>No</td>
      <td>Groceries</td>
      <td>89</td>
      <td>6</td>
      <td>534</td>
      <td>Card</td>
      <td>1</td>
    </tr>
    <tr>
      <th>206</th>
      <td>172252194</td>
      <td>3/22/2018</td>
      <td>20:10</td>
      <td>Female</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>No</td>
      <td>Books</td>
      <td>41</td>
      <td>6</td>
      <td>246</td>
      <td>Card</td>
      <td>4</td>
    </tr>
    <tr>
      <th>207</th>
      <td>866140211</td>
      <td>2/25/2018</td>
      <td>13:34</td>
      <td>Female</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>No</td>
      <td>Clothing</td>
      <td>54</td>
      <td>6</td>
      <td>324</td>
      <td>Gpay</td>
      <td>4</td>
    </tr>
    <tr>
      <th>208</th>
      <td>597678548</td>
      <td>3/15/2018</td>
      <td>17:35</td>
      <td>Male</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>Yes</td>
      <td>Sporting</td>
      <td>34</td>
      <td>3</td>
      <td>102</td>
      <td>Cash</td>
      <td>1</td>
    </tr>
    <tr>
      <th>209</th>
      <td>428818456</td>
      <td>2/25/2018</td>
      <td>18:50</td>
      <td>Male</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>Yes</td>
      <td>Books</td>
      <td>94</td>
      <td>5</td>
      <td>470</td>
      <td>Cash</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# last 5 datasets

sales.tail()
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
</div>




```python
# last 10 rows

sales.tail(10)
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
      <th>990</th>
      <td>752407865</td>
      <td>1/15/2018</td>
      <td>10:01</td>
      <td>Male</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>Yes</td>
      <td>Clothing</td>
      <td>25</td>
      <td>4</td>
      <td>100</td>
      <td>Cash</td>
      <td>5</td>
    </tr>
    <tr>
      <th>991</th>
      <td>699906043</td>
      <td>2/15/2018</td>
      <td>12:58</td>
      <td>Male</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>Yes</td>
      <td>Furniture</td>
      <td>96</td>
      <td>7</td>
      <td>672</td>
      <td>Card</td>
      <td>3</td>
    </tr>
    <tr>
      <th>992</th>
      <td>927909627</td>
      <td>3/2/2018</td>
      <td>13:35</td>
      <td>Male</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>No</td>
      <td>Books</td>
      <td>54</td>
      <td>1</td>
      <td>54</td>
      <td>Card</td>
      <td>1</td>
    </tr>
    <tr>
      <th>993</th>
      <td>455112063</td>
      <td>3/19/2018</td>
      <td>17:30</td>
      <td>Female</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>Yes</td>
      <td>Clothing</td>
      <td>3</td>
      <td>3</td>
      <td>9</td>
      <td>Cash</td>
      <td>2</td>
    </tr>
    <tr>
      <th>994</th>
      <td>446582560</td>
      <td>1/31/2018</td>
      <td>19:00</td>
      <td>Male</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>No</td>
      <td>Fashion</td>
      <td>29</td>
      <td>5</td>
      <td>145</td>
      <td>Cash</td>
      <td>4</td>
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
</div>




```python
# view gender == male

sales[sales['Gender'] == 'Male']
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
      <th>992</th>
      <td>927909627</td>
      <td>3/2/2018</td>
      <td>13:35</td>
      <td>Male</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>No</td>
      <td>Books</td>
      <td>54</td>
      <td>1</td>
      <td>54</td>
      <td>Card</td>
      <td>1</td>
    </tr>
    <tr>
      <th>994</th>
      <td>446582560</td>
      <td>1/31/2018</td>
      <td>19:00</td>
      <td>Male</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>No</td>
      <td>Fashion</td>
      <td>29</td>
      <td>5</td>
      <td>145</td>
      <td>Cash</td>
      <td>4</td>
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
  </tbody>
</table>
<p>499 rows × 13 columns</p>
</div>




```python
# view gender == female from first 10

sales[sales['Gender'] == 'Female'].head(10)
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
    </tr>
    <tr>
      <th>10</th>
      <td>388412668</td>
      <td>2/26/2018</td>
      <td>11:32</td>
      <td>Female</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>No</td>
      <td>Furniture</td>
      <td>35</td>
      <td>4</td>
      <td>140</td>
      <td>Gpay</td>
      <td>4</td>
    </tr>
    <tr>
      <th>13</th>
      <td>942406749</td>
      <td>1/18/2018</td>
      <td>15:20</td>
      <td>Female</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>Yes</td>
      <td>Clothing</td>
      <td>9</td>
      <td>6</td>
      <td>54</td>
      <td>Gpay</td>
      <td>5</td>
    </tr>
    <tr>
      <th>14</th>
      <td>547572603</td>
      <td>3/21/2018</td>
      <td>13:23</td>
      <td>Female</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>No</td>
      <td>Fashion</td>
      <td>98</td>
      <td>7</td>
      <td>686</td>
      <td>Gpay</td>
      <td>3</td>
    </tr>
    <tr>
      <th>15</th>
      <td>355981315</td>
      <td>2/15/2018</td>
      <td>15:47</td>
      <td>Female</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>Yes</td>
      <td>Clothing</td>
      <td>78</td>
      <td>5</td>
      <td>390</td>
      <td>Card</td>
      <td>5</td>
    </tr>
    <tr>
      <th>16</th>
      <td>397754805</td>
      <td>2/9/2018</td>
      <td>15:59</td>
      <td>Female</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>Yes</td>
      <td>Sporting</td>
      <td>35</td>
      <td>7</td>
      <td>245</td>
      <td>Gpay</td>
      <td>1</td>
    </tr>
    <tr>
      <th>18</th>
      <td>542144906</td>
      <td>2/6/2018</td>
      <td>10:58</td>
      <td>Female</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>Yes</td>
      <td>Fashion</td>
      <td>33</td>
      <td>5</td>
      <td>165</td>
      <td>Gpay</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# total > 200

sales[sales['Total'] > 200]
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
      <th>987</th>
      <td>245049016</td>
      <td>1/20/2018</td>
      <td>10:03</td>
      <td>Female</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>No</td>
      <td>Furniture</td>
      <td>74</td>
      <td>4</td>
      <td>296</td>
      <td>Card</td>
      <td>4</td>
    </tr>
    <tr>
      <th>991</th>
      <td>699906043</td>
      <td>2/15/2018</td>
      <td>12:58</td>
      <td>Male</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>Yes</td>
      <td>Furniture</td>
      <td>96</td>
      <td>7</td>
      <td>672</td>
      <td>Card</td>
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
<p>419 rows × 13 columns</p>
</div>




```python
# total < 50 from last 5 rows

sales[sales['Total'] < 50].tail(5)
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
      <th>976</th>
      <td>497734676</td>
      <td>2/9/2018</td>
      <td>14:14</td>
      <td>Male</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>No</td>
      <td>Sporting</td>
      <td>5</td>
      <td>4</td>
      <td>20</td>
      <td>Cash</td>
      <td>3</td>
    </tr>
    <tr>
      <th>978</th>
      <td>158012185</td>
      <td>3/9/2018</td>
      <td>11:46</td>
      <td>Male</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>No</td>
      <td>Books</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>Gpay</td>
      <td>2</td>
    </tr>
    <tr>
      <th>983</th>
      <td>169440268</td>
      <td>2/17/2018</td>
      <td>14:42</td>
      <td>Female</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>No</td>
      <td>Groceries</td>
      <td>4</td>
      <td>7</td>
      <td>28</td>
      <td>Gpay</td>
      <td>5</td>
    </tr>
    <tr>
      <th>993</th>
      <td>455112063</td>
      <td>3/19/2018</td>
      <td>17:30</td>
      <td>Female</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>Yes</td>
      <td>Clothing</td>
      <td>3</td>
      <td>3</td>
      <td>9</td>
      <td>Cash</td>
      <td>2</td>
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
  </tbody>
</table>
</div>




```python
# city == NewYork

sales[sales['City'] == 'NewYork']
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
    </tr>
    <tr>
      <th>10</th>
      <td>388412668</td>
      <td>2/26/2018</td>
      <td>11:32</td>
      <td>Female</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>No</td>
      <td>Furniture</td>
      <td>35</td>
      <td>4</td>
      <td>140</td>
      <td>Gpay</td>
      <td>4</td>
    </tr>
    <tr>
      <th>14</th>
      <td>547572603</td>
      <td>3/21/2018</td>
      <td>13:23</td>
      <td>Female</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>No</td>
      <td>Fashion</td>
      <td>98</td>
      <td>7</td>
      <td>686</td>
      <td>Gpay</td>
      <td>3</td>
    </tr>
    <tr>
      <th>15</th>
      <td>355981315</td>
      <td>2/15/2018</td>
      <td>15:47</td>
      <td>Female</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>Yes</td>
      <td>Clothing</td>
      <td>78</td>
      <td>5</td>
      <td>390</td>
      <td>Card</td>
      <td>5</td>
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
      <th>991</th>
      <td>699906043</td>
      <td>2/15/2018</td>
      <td>12:58</td>
      <td>Male</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>Yes</td>
      <td>Furniture</td>
      <td>96</td>
      <td>7</td>
      <td>672</td>
      <td>Card</td>
      <td>3</td>
    </tr>
    <tr>
      <th>992</th>
      <td>927909627</td>
      <td>3/2/2018</td>
      <td>13:35</td>
      <td>Male</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>No</td>
      <td>Books</td>
      <td>54</td>
      <td>1</td>
      <td>54</td>
      <td>Card</td>
      <td>1</td>
    </tr>
    <tr>
      <th>993</th>
      <td>455112063</td>
      <td>3/19/2018</td>
      <td>17:30</td>
      <td>Female</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>Yes</td>
      <td>Clothing</td>
      <td>3</td>
      <td>3</td>
      <td>9</td>
      <td>Cash</td>
      <td>2</td>
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
  </tbody>
</table>
<p>340 rows × 13 columns</p>
</div>




```python
# unique categories

sales['Category'].unique()
```




    array(['Groceries', 'Fashion', 'Clothing', 'Sporting', 'Books',
           'Furniture'], dtype=object)




```python
# total in between 100 & 200

# data = sales[sales['Total'] > 100]
# data = data[data['Total'] < 200]
# data

# Simplified
sales[(sales['Total'] > 100) & (sales['Total'] < 200)]
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
    </tr>
    <tr>
      <th>10</th>
      <td>388412668</td>
      <td>2/26/2018</td>
      <td>11:32</td>
      <td>Female</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>No</td>
      <td>Furniture</td>
      <td>35</td>
      <td>4</td>
      <td>140</td>
      <td>Gpay</td>
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
      <th>977</th>
      <td>614557665</td>
      <td>3/22/2018</td>
      <td>17:16</td>
      <td>Female</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>No</td>
      <td>Clothing</td>
      <td>49</td>
      <td>3</td>
      <td>147</td>
      <td>Cash</td>
      <td>5</td>
    </tr>
    <tr>
      <th>981</th>
      <td>418253101</td>
      <td>3/14/2018</td>
      <td>12:25</td>
      <td>Female</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>No</td>
      <td>Fashion</td>
      <td>81</td>
      <td>2</td>
      <td>162</td>
      <td>Gpay</td>
      <td>5</td>
    </tr>
    <tr>
      <th>989</th>
      <td>941364541</td>
      <td>3/13/2018</td>
      <td>14:53</td>
      <td>Female</td>
      <td>Brookfield</td>
      <td>NewYork</td>
      <td>No</td>
      <td>Sporting</td>
      <td>19</td>
      <td>7</td>
      <td>133</td>
      <td>Cash</td>
      <td>1</td>
    </tr>
    <tr>
      <th>994</th>
      <td>446582560</td>
      <td>1/31/2018</td>
      <td>19:00</td>
      <td>Male</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>No</td>
      <td>Fashion</td>
      <td>29</td>
      <td>5</td>
      <td>145</td>
      <td>Cash</td>
      <td>4</td>
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
  </tbody>
</table>
<p>231 rows × 13 columns</p>
</div>




```python
# With Arithmatic 

sales.sum()['Total']
```




    207788




```python
sales.sum()['Quantity']
```




    4059




```python
sales.max()
```




    Invoice ID      999665753
    Date             3/9/2018
    Time                20:59
    Gender               Male
    Location      Water tower
    City              NewYork
    Member                Yes
    Category         Sporting
    Price                 100
    Quantity                7
    Total                 693
    Payment              Gpay
    Rating                  5
    dtype: object




```python
sales.max()['Total']
```




    693




```python
sales[sales['Total'] == sales.max()['Total']]
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
      <th>47</th>
      <td>315624039</td>
      <td>3/30/2018</td>
      <td>19:45</td>
      <td>Female</td>
      <td>Water tower</td>
      <td>Chicago</td>
      <td>Yes</td>
      <td>Groceries</td>
      <td>99</td>
      <td>7</td>
      <td>693</td>
      <td>Gpay</td>
      <td>3</td>
    </tr>
    <tr>
      <th>679</th>
      <td>270918350</td>
      <td>3/27/2018</td>
      <td>13:21</td>
      <td>Female</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>Yes</td>
      <td>Groceries</td>
      <td>99</td>
      <td>7</td>
      <td>693</td>
      <td>Gpay</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
sales.min()
```




    Invoice ID        661405
    Date            1/1/2018
    Time               10:00
    Gender            Female
    Location      Brookfield
    City             Chicago
    Member                No
    Category           Books
    Price                  1
    Quantity               1
    Total                  1
    Payment             Card
    Rating                 1
    dtype: object




```python
sales[sales['Total'] == sales.min()['Total']]
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
      <th>184</th>
      <td>801334050</td>
      <td>1/21/2018</td>
      <td>20:18</td>
      <td>Female</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>No</td>
      <td>Furniture</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Gpay</td>
      <td>2</td>
    </tr>
    <tr>
      <th>587</th>
      <td>646176653</td>
      <td>3/10/2018</td>
      <td>19:39</td>
      <td>Male</td>
      <td>Park lane</td>
      <td>Dallas</td>
      <td>Yes</td>
      <td>Sporting</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Cash</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
sales.mean()['Total']
```

    C:\Users\abdul\AppData\Local\Temp\ipykernel_14056\1945902060.py:1: FutureWarning: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated; in a future version this will raise TypeError.  Select only valid columns before calling the reduction.
      sales.mean()['Total']
    




    207.788




```python
sales['Total'].mean()
```




    207.788




```python
# Group by
sales.groupby('City').sum()['Total']
```




    City
    Chicago    65215
    Dallas     70432
    NewYork    72141
    Name: Total, dtype: int64




```python
sales.groupby('Date').sum()['Total']
```




    Date
    1/1/2018     2649
    1/10/2018    1116
    1/11/2018    1562
    1/12/2018    2625
    1/13/2018    2340
                 ... 
    3/5/2018     4616
    3/6/2018     1915
    3/7/2018     1048
    3/8/2018     2638
    3/9/2018     4300
    Name: Total, Length: 89, dtype: int64




```python
sales.groupby('Category').sum()['Total']
```




    Category
    Books        36103
    Clothing     35925
    Fashion      32778
    Furniture    34141
    Groceries    31236
    Sporting     37605
    Name: Total, dtype: int64




```python
sales.groupby('Member').sum()['Total']
```




    Member
    No     100245
    Yes    107543
    Name: Total, dtype: int64




```python
# Group by gender base total

sales.groupby('Gender').sum()['Total']
```




    Gender
    Female    106452
    Male      101336
    Name: Total, dtype: int64




```python
# Group by two coloumns base total
sales.groupby(['Payment', 'Gender']).sum()['Total']
```




    Payment  Gender
    Card     Female    31137
             Male      33127
    Cash     Female    35298
             Male      37345
    Gpay     Female    40017
             Male      30864
    Name: Total, dtype: int64




```python

sales.groupby(['City', 'Payment']).sum()['Total']
```




    City     Payment
    Chicago  Card       18213
             Cash       26164
             Gpay       20838
    Dallas   Card       22851
             Cash       22341
             Gpay       25240
    NewYork  Card       23200
             Cash       24138
             Gpay       24803
    Name: Total, dtype: int64




```python

```
