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

#This file is used for the training and validation of the RNN model.
#Notice that the y_test and x_test are accually validation dataset.

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

X_train = X.iloc[:-80]
X_test = X.iloc[-80:-40]
y_train = y.iloc[:-80]
y_test = y.iloc[-80:-40]

# Reshape the input data for the RNN
X_train_rnn = X_train.values.reshape((X_train.shape[0], 1, X_train.shape[1]))
X_test_rnn = X_test.values.reshape((X_test.shape[0], 1, X_test.shape[1]))

# Create a simple RNN model
model = Sequential()
model.add(SimpleRNN(32, input_shape=(1, X_train.shape[1]), activation='relu'))
model.add(Dense(1))


optimizer = Adam(lr=0.005)

# Compile the model
model.compile(optimizer=optimizer, loss='mean_squared_error')

# Train the model
model.fit(X_train_rnn, y_train, epochs=50, batch_size=1, verbose=0)

# Make predictions on the test set
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

# Create the line plot
plt.figure(figsize=(12, 6))
plt.plot(x_train, y_train, label='True Training Labels')
plt.plot(x_test, y_test, label='True Testing Labels')
plt.plot(x_test, y_pred_flat, label='Predicted Testing Labels')

# Add title, labels, and legend
plt.title('True vs. Predicted Labels')
plt.xlabel('Sequential Integer')
plt.ylabel('Normalized GDP')
plt.legend()

# Show the plot
plt.show()

# Save the model
model.save('my_model1.h5')
