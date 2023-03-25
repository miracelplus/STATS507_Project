import pandas as pd
from pathlib import Path
import plotly.express as px
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
    corr_matrix = pfin.corr()
    print(corr_matrix)
    sn.heatmap(corr_matrix, annot=True)
    plt.show()
    pfin_df = pd.DataFrame(pfin)
    pago = pfin_df['PAGO5']
    pexp = pfin_df['PEXP5']
    #plt.figure(figsize=(10,7))
    plt.hist(pago, alpha=0.5, label="PAGO5")
    plt.hist(pexp, alpha=0.5, label="PEXP5")
    plt.xlabel("Data")
    plt.ylabel("Count")
    plt.title("Personal Finance Histogram")
    plt.legend(loc="upper right")
    plt.show()
    AGE_group = pfin.groupby('AGE')
    AGE_PAGO5_mean = AGE_group['PAGO5'].mean()
    AGE_PEXP5_mean = AGE_group['PEXP5'].mean()
    fig = px.bar(AGE_PAGO5_mean, x=AGE_PAGO5_mean.index, y='PAGO5')
    fig.show()
    fig = px.bar(AGE_PEXP5_mean, x=AGE_PEXP5_mean.index, y='PEXP5')
    fig.show()
    KID_group = pfin.groupby('NUMKID')
    KID_PAGO5_mean = KID_group['PAGO5'].mean()
    KID_PEXP5_mean = KID_group['PEXP5'].mean()
    fig = px.bar(KID_PAGO5_mean, x=KID_PAGO5_mean.index, y='PAGO5')
    fig.show()
    fig = px.bar(KID_PEXP5_mean, x=KID_PEXP5_mean.index, y='PEXP5')
    fig.show()
    return figure_id_list