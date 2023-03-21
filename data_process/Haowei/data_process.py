import pandas as pd
from pathlib import Path
import numpy as np


haowei_path = Path('data/Haowei.csv')
dataset = pd.read_csv(haowei_path, index_col=0)
print(dataset.head())
# replace all elements with whitespace cells with NaN
dataset.replace(r'^\s*$', np.nan, regex=True, inplace=True)
dataset_clean = dataset.dropna()
print(dataset_clean.head())
dataset = dataset.drop_duplicates()
dataset = dataset.reset_index(drop=True)
dataset_clean.to_csv('data/Haowei_cleaned.csv')






