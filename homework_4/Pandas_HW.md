

```python
import pandas as pd
import numpy as np
```


```python
game_df = pd.read_json("purchase_data.json")
```


```python
game_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Total numbers of players

# ????? why put [] into the funtion?

pd.DataFrame({"Total numbers of players" : [len(game_df["SN"].unique())]})


```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total numbers of players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




```python
distinct_df = game_df[["Age", "Gender", "SN"]].drop_duplicates()

distinct_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Purchasing Analysis (Total)

pd.DataFrame({"Number of Unique Items": [len(game_df["Item Name"].unique())],
              "Average Purchase Price": game_df["Price"].mean(),
              "Total Number of Purchases": game_df["Item ID"].count(),
              "Total Revenue": game_df["Price"].sum()

             })

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Number of Unique Items</th>
      <th>Total Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.931192</td>
      <td>179</td>
      <td>780</td>
      <td>2286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Gender Demographics

pd.DataFrame({ "Total Count": distinct_df["Gender"].value_counts(),
              "Percentage": distinct_df["Gender"].value_counts(" ")
         })
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>0.811518</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>0.174520</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>0.013962</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
groupby_gender_df = game_df.groupby("Gender")

#????? what is normalized totals#####

# ???? why here put gender into the funtion instead of using [] to refer this column, like last step did? 
#when use [] to refer a column, when to put it into a ()???#

pd.DataFrame({
        "Purchase Count": groupby_gender_df["Item ID"].count(),
        "Average Purchase Price":groupby_gender_df["Price"].mean(),
        "Total Purchase Value":groupby_gender_df["Price"].sum()
    })

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
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
      <td>2.815515</td>
      <td>136</td>
      <td>382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>2.950521</td>
      <td>633</td>
      <td>1867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>3.249091</td>
      <td>11</td>
      <td>35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
#bins

# Age Demographics

# The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)



bins = range(4, 60, 4)

game_df["age range"] = pd.cut(game_df["Age"], bins)

groupby_agerange_df = game_df.groupby("age range")


age_range_df = pd.DataFrame({
        
        "Purchase Count": groupby_agerange_df["Item ID"].count(),
        "Average Purchase Price" : groupby_agerange_df["Price"].mean(),
        "Total Purchase Value":groupby_agerange_df["Price"].sum()
    })



age_range_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>age range</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>(4, 8]</th>
      <td>2.788182</td>
      <td>22</td>
      <td>61.34</td>
    </tr>
    <tr>
      <th>(8, 12]</th>
      <td>3.385417</td>
      <td>24</td>
      <td>81.25</td>
    </tr>
    <tr>
      <th>(12, 16]</th>
      <td>2.745862</td>
      <td>87</td>
      <td>238.89</td>
    </tr>
    <tr>
      <th>(16, 20]</th>
      <td>2.907019</td>
      <td>161</td>
      <td>468.03</td>
    </tr>
    <tr>
      <th>(20, 24]</th>
      <td>2.924748</td>
      <td>238</td>
      <td>696.09</td>
    </tr>
    <tr>
      <th>(24, 28]</th>
      <td>2.974712</td>
      <td>104</td>
      <td>309.37</td>
    </tr>
    <tr>
      <th>(28, 32]</th>
      <td>3.061970</td>
      <td>66</td>
      <td>202.09</td>
    </tr>
    <tr>
      <th>(32, 36]</th>
      <td>2.981053</td>
      <td>38</td>
      <td>113.28</td>
    </tr>
    <tr>
      <th>(36, 40]</th>
      <td>2.901351</td>
      <td>37</td>
      <td>107.35</td>
    </tr>
    <tr>
      <th>(40, 44]</th>
      <td>2.960000</td>
      <td>2</td>
      <td>5.92</td>
    </tr>
    <tr>
      <th>(44, 48]</th>
      <td>2.720000</td>
      <td>1</td>
      <td>2.72</td>
    </tr>
    <tr>
      <th>(48, 52]</th>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>(52, 56]</th>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Top Spenders

orderby_price_df = game_df.sort_values("Price", ascending = False)

top5_df = orderby_price_df.iloc[0:5 , :]

merge_table = pd.merge(top5_df, game_df, on = "SN")

merge_table

########################################################################################
groupby_username = merge_table.groupby("SN")

#Purchase Count : 
groupby_username["Item ID_y"].count()

#Average Purchase Price:
groupby_username["Price_y"].mean()

# Total Purchase Value
groupby_username["Price_y"].sum()

top_spender_df = pd.DataFrame({"Purchase Count": groupby_username["Item ID_y"].count(),
                               "Average Purchase Price": groupby_username["Price_y"].mean(), 
                               "Total Purchase Value": groupby_username["Price_y"].sum()       
    })


top_spender_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Frichaststa61</th>
      <td>4.95</td>
      <td>1</td>
      <td>4.95</td>
    </tr>
    <tr>
      <th>Palurrian69</th>
      <td>4.95</td>
      <td>1</td>
      <td>4.95</td>
    </tr>
    <tr>
      <th>Qiluard68</th>
      <td>4.95</td>
      <td>1</td>
      <td>4.95</td>
    </tr>
    <tr>
      <th>Saistyphos30</th>
      <td>2.99</td>
      <td>2</td>
      <td>5.98</td>
    </tr>
    <tr>
      <th>Tyarithn67</th>
      <td>4.95</td>
      <td>1</td>
      <td>4.95</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Most Popular Items

# Identify the 5 most popular items by purchase count, then list (in a table):
# Item ID
# Item Name
# Purchase Count
# Item Price
# Total Purchase Value

top_game_df = game_df["Item ID"].value_counts().sort_values(ascending = False).iloc[0:5]



new_df = pd.DataFrame({"purchase count": top_game_df})

new_df.index.names = ['Item ID']

new_df



```




    84     11
    39     11
    31      9
    34      9
    175     9
    Name: Item ID, dtype: int64




```python
###### why cannot I join??????

merge_table = pd.merge(new_df, game_df, on = "Item ID")
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    C:\Users\jiliu\AppData\Local\Continuum\Anaconda3\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
       2441             try:
    -> 2442                 return self._engine.get_loc(key)
       2443             except KeyError:
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    KeyError: 'Item ID'

    
    During handling of the above exception, another exception occurred:
    

    KeyError                                  Traceback (most recent call last)

    <ipython-input-93-a77f84d4f94a> in <module>()
          1 ###### why cannot I join??????
          2 
    ----> 3 merge_table = pd.merge(new_df, game_df, on = "Item ID")
    

    C:\Users\jiliu\AppData\Local\Continuum\Anaconda3\lib\site-packages\pandas\core\reshape\merge.py in merge(left, right, how, on, left_on, right_on, left_index, right_index, sort, suffixes, copy, indicator)
         51                          right_on=right_on, left_index=left_index,
         52                          right_index=right_index, sort=sort, suffixes=suffixes,
    ---> 53                          copy=copy, indicator=indicator)
         54     return op.get_result()
         55 
    

    C:\Users\jiliu\AppData\Local\Continuum\Anaconda3\lib\site-packages\pandas\core\reshape\merge.py in __init__(self, left, right, how, on, left_on, right_on, axis, left_index, right_index, sort, suffixes, copy, indicator)
        556         (self.left_join_keys,
        557          self.right_join_keys,
    --> 558          self.join_names) = self._get_merge_keys()
        559 
        560         # validate the merge keys dtypes. We may need to coerce
    

    C:\Users\jiliu\AppData\Local\Continuum\Anaconda3\lib\site-packages\pandas\core\reshape\merge.py in _get_merge_keys(self)
        821                         right_keys.append(rk)
        822                     if lk is not None:
    --> 823                         left_keys.append(left[lk]._values)
        824                         join_names.append(lk)
        825                     else:
    

    C:\Users\jiliu\AppData\Local\Continuum\Anaconda3\lib\site-packages\pandas\core\frame.py in __getitem__(self, key)
       1962             return self._getitem_multilevel(key)
       1963         else:
    -> 1964             return self._getitem_column(key)
       1965 
       1966     def _getitem_column(self, key):
    

    C:\Users\jiliu\AppData\Local\Continuum\Anaconda3\lib\site-packages\pandas\core\frame.py in _getitem_column(self, key)
       1969         # get column
       1970         if self.columns.is_unique:
    -> 1971             return self._get_item_cache(key)
       1972 
       1973         # duplicate columns & possible reduce dimensionality
    

    C:\Users\jiliu\AppData\Local\Continuum\Anaconda3\lib\site-packages\pandas\core\generic.py in _get_item_cache(self, item)
       1643         res = cache.get(item)
       1644         if res is None:
    -> 1645             values = self._data.get(item)
       1646             res = self._box_item_values(item, values)
       1647             cache[item] = res
    

    C:\Users\jiliu\AppData\Local\Continuum\Anaconda3\lib\site-packages\pandas\core\internals.py in get(self, item, fastpath)
       3588 
       3589             if not isnull(item):
    -> 3590                 loc = self.items.get_loc(item)
       3591             else:
       3592                 indexer = np.arange(len(self.items))[isnull(self.items)]
    

    C:\Users\jiliu\AppData\Local\Continuum\Anaconda3\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
       2442                 return self._engine.get_loc(key)
       2443             except KeyError:
    -> 2444                 return self._engine.get_loc(self._maybe_cast_indexer(key))
       2445 
       2446         indexer = self.get_indexer([key], method=method, tolerance=tolerance)
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    KeyError: 'Item ID'

