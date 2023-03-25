#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pathlib import Path
import numpy as np


# In[2]:


path = Path('/Users/elenachun/Downloads/STATS507/project/PFinance.csv')
dataset = pd.read_csv(path, index_col=0)
print(dataset.head())


# In[3]:


dataset.replace(r'^\s*$', np.nan, regex=True, inplace=True)
dataset_clean = dataset.dropna()
print(dataset_clean.head())
dataset = dataset.drop_duplicates()
dataset = dataset.reset_index(drop=True)
dataset_clean.to_csv('/Users/elenachun/Downloads/STATS507/project/PFinClean.csv')

