#!/usr/bin/env python
# coding: utf-8

# In[89]:


import pandas as pd
from pathlib import Path
import numpy as np


# Data Cleaning for the original dataset:

path = Path('AAkvMtwz.csv')
dataset = pd.read_csv(path, index_col=0, low_memory=False)
print(dataset.head())

dataset.replace(r'^\s*$', np.nan, regex=True, inplace=True)

for i in dataset.columns:
    dataset=dataset.dropna(subset=[i])
print(dataset.head())
#dataset = dataset.drop_duplicates()
#dataset = dataset.reset_index(drop=True)
dataset.to_csv('SDAdata_clean.csv')


# Data Aggregation for the original dataset:

dataset_agg=dataset.groupby('YYYY', as_index=False).agg({"ICE":"mean",
                                                           "UNEMP":"mean",
                                                           "GOVT":"mean",
                                                           "RATEX":"mean",
                                                           "INCOME":"median",
                                                           "INVAMT":"mean",
                                                           "STL5":"median"}).reset_index()
print(dataset_agg)
dataset_agg.to_csv('SDAagg.csv')

# Data Aggregation for the World Bank dataset:

path_WB = Path('WorldBank_Data.csv')
dataset_WB = pd.read_csv(path_WB, index_col=0, low_memory=False)
print(dataset_WB.head())

final = pd.merge(dataset_agg, dataset_WB, on='YYYY', how='inner')
final.to_csv('FINALagg.csv')
