from keras.models import load_model
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, SimpleRNN
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from keras.optimizers import Adam
import statistics
from sklearn.metrics import mean_absolute_error

df1 = pd.read_csv("AAO2b05c.csv", sep=",", header=0)

df1['Q'] = df1['YYYYQ'].astype(str).str[-1]

# Convert the 'Q' column to integers
df1['Q'] = df1['Q'].astype(int)

averages_by_yyyyq = df1.groupby('YYYYQ').mean()
columns_to_remove = [averages_by_yyyyq.columns[0], averages_by_yyyyq.columns[1], averages_by_yyyyq.columns[3]]
averages_by_yyyyq = averages_by_yyyyq.drop(columns_to_remove, axis=1)

data = pd.read_excel('gdp.xlsx', engine='openpyxl')

data = data.dropna(axis=1, how='all')

first_row_list = data.iloc[0].tolist()
gdp = pd.to_numeric(first_row_list[1:], errors='coerce')

averages_by_yyyyq = averages_by_yyyyq.iloc[:-1]

averages_by_yyyyq['GDP'] = gdp
scaler = StandardScaler()

mean = statistics.mean(gdp)  # Calculate the mean
std_dev = statistics.stdev(gdp)  # Calculate the standard deviation

gdp_normalized = (averages_by_yyyyq['GDP']-mean)/std_dev
INVAMT_normalized = scaler.fit_transform(averages_by_yyyyq['INVAMT'].values.reshape(-1, 1))
YYYY_normalized = scaler.fit_transform(averages_by_yyyyq['YYYY'].values.reshape(-1, 1))
WT_normalized = scaler.fit_transform(averages_by_yyyyq['WT'].values.reshape(-1, 1))

averages_by_yyyyq['GDP_normalized'] = gdp_normalized
averages_by_yyyyq['INVAMT_normalized'] = INVAMT_normalized
averages_by_yyyyq['YYYY_normalized'] = YYYY_normalized
averages_by_yyyyq['WT_normalized'] = WT_normalized

X = averages_by_yyyyq[['INVAMT_normalized', 'YYYY_normalized', 'WT_normalized']]
y = averages_by_yyyyq['GDP_normalized']

X_train = X.iloc[:-40]
X_test = X.iloc[-40:]
y_train = y.iloc[:-40]
y_test = y.iloc[-40:]

# Reshape the input data for the RNN
X_train_rnn = X_train.values.reshape((X_train.shape[0], 1, X_train.shape[1]))
X_test_rnn = X_test.values.reshape((X_test.shape[0], 1, X_test.shape[1]))

# Load the model
model = load_model('my_model1.h5')


y_pred = model.predict(X_test_rnn)

# Calculate the Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred)

# Print the MAE
print("Mean Absolute Error (MAE) on the testing dataset:", mae)

# Flatten the y_pred array
y_pred_flat = y_pred.flatten()

# Create sequential integer indices for x-axis
x_train = np.arange(len(y_train))
x_test = np.arange(len(y_train), len(y_train) + len(y_test))

y_train = y_train *std_dev +mean
y_test = y_test *std_dev+mean
y_pred_flat = y_pred_flat*std_dev+mean
# Create x-axis ticks and labels for every 4th year starting from 1978
years = np.arange(1978, 2023, 4)
ticks = np.arange(0, len(x_train)+len(x_test), 16)
labels = [str(year) for year in years]

# Create the line plot with modified x-axis
plt.figure(figsize=(12, 6))
plt.plot(x_train, y_train, label='GDP before 2012 (include 2012)')
plt.plot(x_test, y_test, label='True GDP after 2012')
plt.plot(x_test, y_pred_flat, label='Predicted GDP after 2012')

# Set the x-axis ticks and labels
plt.xticks(ticks=ticks, labels=labels)

# Add title, labels, and legend
plt.title('Comparision of Model prediction of GDP and true GDP')
plt.xlabel('Year')
plt.ylabel('GDP')
plt.legend()

# Show the plot
plt.show()

pred_results_dict = {'2012': 0.9812531, '2013': 1.0452406, '2014': 1.1253386, '2015': 1.1949261, 
'2016': 1.2582558, '2017': 1.325577, '2018': 1.3971158, '2019': 1.4603425, 
'2020': 1.553108, '2021': 1.6295736}

