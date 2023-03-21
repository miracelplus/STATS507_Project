import pandas as pd
from pathlib import Path
import plotly.express as px


haowei_path = Path('data/Haowei_cleaned.csv')
dataset = pd.read_csv(haowei_path, index_col=0)

# print the first 5 rows of the dataset
print(dataset.head())

fig = px.histogram(dataset, x="AGE")
# save the figure as a png file
fig.write_image('fig1.png')
