import pandas as pd
from pathlib import Path
import plotly.express as px
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def EDA():
    """EDA analysis code

    Returns:
        figure_and_explanation_list: This list contains the figure and the explanation
        [(figure, explanation), (figure, explanation), ...]
        figure should be a plotly figure object, and explanation should be a string
    """
    figure_id_list = []
    haowei_path = Path('data/Haowei/Haowei_cleaned.csv')
    dataset = pd.read_csv(haowei_path, index_col=0)

    # rewrite the code using plotly
    fig1 = px.histogram(dataset, x='AGE', nbins=20)
    fig1.update_layout(title_text='Distribution of age')

    # get different age groups
    AGE_group = dataset.groupby('AGE')

    # calculate the mean ICS score for each age group
    AGE_ICS_mean = AGE_group['ICS'].mean()

    # calculate the mean ICC score for each age group
    AGE_ICC_mean = AGE_group['ICC'].mean()

    # calculate the mean ICE score for each age group
    AGE_ICE_mean = AGE_group['ICE'].mean()

    # plot the mean ICS score for each age group using plotly
    fig2 = px.bar(AGE_ICS_mean, x=AGE_ICS_mean.index, y='ICS')
    fig2.update_layout(title_text='Average ICS (Index of Consumer Sentiment) for each age group')

    # plot the mean ICC score for each age group using plotly
    fig3 = px.bar(AGE_ICC_mean, x=AGE_ICC_mean.index, y='ICC')
    fig3.update_layout(title_text='Average ICC (Index of Consumer Condition) for each age group')

    # plot the mean ICE score for each age group using plotly
    fig4 = px.bar(AGE_ICE_mean, x=AGE_ICE_mean.index, y='ICE')
    fig4.update_layout(title_text='Average ICE (Index of Consumer Expectation) for each age group')

    return [(fig1, 'Age distribution'), (fig2, 'Average ICS (Index of Consumer Sentiment) for each age group'), (fig3, 'Average ICC (Index of Consumer Condition) for each age group'), (fig4, 'Average ICE (Index of Consumer Expectation) for each age group')]

