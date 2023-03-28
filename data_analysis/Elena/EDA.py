import pandas as pd
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sn

def EDA():
    """EDA analysis code

    Returns:
        figure_and_explanation_list: This list contains the figure and the explanation
        [(figure, explanation), (figure, explanation), ...]
        figure should be a plotly figure object, and explanation should be a string
    """
    figure_id_list = []
    path = Path('data/Elena/PFinClean.csv')
    pfin = pd.read_csv(path, index_col=0)

    fig2 = go.Figure()
    fig2.add_trace(go.Histogram(x=pfin['PAGO5'], name="PAGO5"))
    fig2.add_trace(go.Histogram(x=pfin['PEXP5'], name="PEXP5"))
    fig2.update_layout(title="Personal Finance Histogram", 
                       xaxis_title="Data", 
                       yaxis_title="Count")
    fig2.update_traces(opacity=0.75)
    # fig2.show()
    AGE_group = pfin.groupby('AGE')
    AGE_mean = AGE_group[['PAGO5','PEXP5']].mean()
    fig3 = px.bar(AGE_mean, x=AGE_mean.index, y=['PAGO5', 'PEXP5'])
    fig3.update_layout(title="Average Personal Finance for each age group")
    # fig3.show()
    KID_group = pfin.groupby('NUMKID')
    KID_mean = KID_group[['PAGO5','PEXP5']].mean()
    fig4 = px.bar(KID_mean, x=KID_mean.index, y=['PAGO5', 'PEXP5'])
    fig4.update_layout(title="Average Personal Finance for each number of kid group")
    # fig4.show()
    return [(fig2, 'Personal Finance Histogram'), (fig3, 'Average Personal Finance for each age group'), (fig4, 'Average Personal Finance for each number of kid group')]
