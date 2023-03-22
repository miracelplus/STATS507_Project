import pandas as pd
from pathlib import Path
import plotly.express as px
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

haowei_path = Path('data/Haowei_cleaned.csv')
dataset = pd.read_csv(haowei_path, index_col=0)

# rewrite the code using plotly
fig = px.histogram(dataset, x='AGE', nbins=20)
fig.show()


# get different age groups
AGE_group = dataset.groupby('AGE')

# calculate the mean ICS score for each age group
AGE_ICS_mean = AGE_group['ICS'].mean()

# calculate the mean ICC score for each age group
AGE_ICC_mean = AGE_group['ICC'].mean()

# calculate the mean ICE score for each age group
AGE_ICE_mean = AGE_group['ICE'].mean()

# plot the mean ICS score for each age group using plotly
fig = px.bar(AGE_ICS_mean, x=AGE_ICS_mean.index, y='ICS')
fig.show()

# plot the mean ICC score for each age group using plotly
fig = px.bar(AGE_ICC_mean, x=AGE_ICC_mean.index, y='ICC')
fig.show()

# plot the mean ICE score for each age group using plotly
fig = px.bar(AGE_ICE_mean, x=AGE_ICE_mean.index, y='ICE')
fig.show()