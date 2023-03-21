import pandas as pd
from pathlib import Path



haowei_path = Path('data/Haowei.csv')
dataset = pd.read_csv(haowei_path, index_col=0)
dataset = dataset.dropna()
dataset = dataset.drop_duplicates()
dataset = dataset.reset_index(drop=True)
dataset.to_csv('data/Haowei_cleaned.csv')




