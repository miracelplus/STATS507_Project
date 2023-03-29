#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
#from xgboost import XGBRegressor
from sklearn.linear_model import SGDRegressor
from plotly import graph_objects as go


# In[2]:


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
gdp = first_row_list[1:]

averages_by_yyyyq = averages_by_yyyyq.iloc[:-1]

averages_by_yyyyq['GDP'] = gdp
gdp = np.array(gdp)
gdp_mean, gdp_std = gdp.mean(), gdp.std()
averages_by_yyyyq['GDP_prev'] = np.concatenate((gdp[0:1],np.roll(gdp,1)[1:]))

scaler = StandardScaler()
gdp_normalized = (averages_by_yyyyq['GDP']-gdp_mean)/gdp_std
INVAMT_normalized = scaler.fit_transform(averages_by_yyyyq['INVAMT'].values.reshape(-1, 1))
YYYY_normalized = scaler.fit_transform(averages_by_yyyyq['YYYY'].values.reshape(-1, 1))
WT_normalized = scaler.fit_transform(averages_by_yyyyq['WT'].values.reshape(-1, 1))

averages_by_yyyyq['GDP_normalized'] = gdp_normalized.values.reshape(-1,1)
averages_by_yyyyq['INVAMT_normalized'] = INVAMT_normalized
averages_by_yyyyq['YYYY_normalized'] = YYYY_normalized
averages_by_yyyyq['WT_normalized'] = WT_normalized

selected_features=['GDP_normalized','WT_normalized','INVAMT_normalized','YYYY_normalized']
selected = averages_by_yyyyq[selected_features]


# In[3]:


X = averages_by_yyyyq[selected_features[1:]]
y = selected['GDP_normalized']

X_train = X.iloc[:-60]
X_vald = X.iloc[-60:-40]
X_test = X.iloc[-40:]

y_train = y.iloc[:-60]
y_vald = y.iloc[-60:-40]
y_test = y.iloc[-40:]


# In[7]:


alphas = np.linspace(0.0005,0.1,num=1000,endpoint=True)
MAEs = []
oks  = []
for i in range(len(alphas)):
    alpha = alphas[i]
    sgd = SGDRegressor(alpha = alpha, learning_rate='optimal')
    sgd.fit(X_train, y_train)
    vald = sgd.predict(X_vald)
    MAEs.append(mean_absolute_error(y_vald,vald))
    oks.append(alphas[i])


# In[8]:


fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=oks,y=MAEs))
fig1.update_yaxes(title_text="Validation_MAE", type="log")
fig1.update_layout(
title="",
xaxis_title="alpha",
yaxis_title="Validation_MAE_normalized",
font=dict(family="Times New Roman",size=16,color="Black"))
fig1.update_layout(title_x=0.5)


# In[9]:


bestalpha = alphas[np.argmin(MAEs)]
print(bestalpha)


# In[10]:


# sgd = SGDRegressor(alpha = bestalpha, learning_rate='optimal')
# sgd.fit(X_train, y_train)
# sgd_train= sgd.predict(X_train)
# sgd_vald = sgd.predict(X_vald)
# sgd_test = sgd.predict(X_test)
# # plt.plot(np.arange(180),np.concatenate((y_train,y_vald,y_test)),label='true')
# # plt.plot(np.concatenate((sgd_train,sgd_vald,sgd_test)),label='sgd')
# # plt.legend()
# # plt.show()


# In[35]:


def get_year_gdp(a):
    i = 0
    b = np.zeros(len(a)//4)
    while i < len(b):
        b[i] = np.sum(a[i:i+4])
        i += 1
    return b

def unnorm(a):
    return gdp_mean+gdp_std*a

sgd = SGDRegressor(alpha = bestalpha, learning_rate='optimal')
sgd.fit(X_train, y_train)
sgd_train= sgd.predict(X_train)
sgd_vald = sgd.predict(X_vald)
sgd_test = sgd.predict(X_test)

years = np.linspace(1978,2023,num=(2023-1978)*4)

gdp_year = gdp
s_train= unnorm(sgd_train)
s_vald = unnorm(sgd_vald)
s_test = unnorm(sgd_test)

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=years,y=gdp_year,name='GDP'))
fig2.add_trace(go.Scatter(x=years,y=np.concatenate((s_train,s_vald,s_test)),name='SGD Regressor Prediction'))
fig2.update_yaxes(title_text="")
fig2.update_layout(
title="GDP Real Values and Predicted Values",
xaxis_title="Year(Quarter)",
yaxis_title="GDP (Million Dollars)",
font=dict(family="Times New Roman",size=16,color="Black"))
fig2.update_layout(title_x=0.5)


# In[36]:


web_years = np.arange(2013,2023)
dic = {}
for i in range(10):
    dic[web_years[i]] = get_year_gdp(s_test)[-10+i]
print(dic)


# In[ ]:




