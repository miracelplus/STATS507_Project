#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sn


# In[42]:


path = Path('/Users/elenachun/Downloads/STATS507/project/PFinClean.csv')
pfin = pd.read_csv(path, index_col=0)


# In[61]:


def EDA():
    """EDA analysis code
    Returns:
        figure_and_explanation_list: This list contains the figure and the explanation
        [(figure, explanation), (figure, explanation), ...]
        figure should be a plotly figure object, and explanation should be a string
    """
    figure_id_list = []
    path = Path('/Users/elenachun/Downloads/STATS507/project/PFinClean.csv')
    pfin = pd.read_csv(path, index_col=0)
    
    corr_matrix = pfin.corr()
    print(corr_matrix)
    fig1 = sn.heatmap(corr_matrix, annot=True)
    print(fig1)
    
    fig2 = go.Figure()
    fig2.add_trace(go.Histogram(x=pfin['PAGO5'], name="PAGO5"))
    fig2.add_trace(go.Histogram(x=pfin['PEXP5'], name="PEXP5"))
    fig2.update_layout(title="Personal Finance", 
                       xaxis_title="Data", 
                       yaxis_title="Count")
    fig2.update_traces(opacity=0.75)
    fig2.show()
    
    AGE_group = pfin.groupby('AGE')
    AGE_mean = AGE_group[['PAGO5','PEXP5']].mean()
    fig3 = px.bar(AGE_mean, x=AGE_mean.index, y=['PAGO5', 'PEXP5'])
    fig3.update_layout(title="Personal Finance by AGE")
    fig3.show()

    KID_group = pfin.groupby('NUMKID')
    KID_mean = KID_group[['PAGO5','PEXP5']].mean()
    fig4 = px.bar(KID_mean, x=KID_mean.index, y=['PAGO5', 'PEXP5'])
    fig4.update_layout(title="Personal Finance by NUMKID")
    fig4.show()

    return figure_id_list

