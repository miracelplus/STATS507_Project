import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
from pathlib import Path

def EDA():
    """EDA analysis code

    Returns:
        figure_and_explanation_list: This list contains the figure and the explanation
        [(figure, explanation), (figure, explanation), ...]
        figure should be a plotly figure object, and explanation should be a string
    """
    figure_id_list = []
    data = pd.read_csv(Path('data/Jingyi/yjy_data.csv'), index_col=0)

    # data cleaning
    # Drop empty data & drop duplicates
    data = data.replace(r'^\s*$', pd.np.nan, regex=True)
    data.dropna(how="any", inplace=True)

    data = data.drop_duplicates()
    data = data.reset_index(drop=True)
    data = data.astype(float)

    # Drop DK/NA data
    data.replace({'PJOB': 998}, pd.np.nan, inplace=True)
    data.replace({'PJOB': 999}, pd.np.nan, inplace=True)
    data.dropna(how="any", inplace=True)

    # plot a scatterplot of income v pjob
    plt.scatter(data['INCOME'], data['PJOB'])

    # add labels and title
    plt.xlabel('Income')
    plt.ylabel('Expectation of Unemployment chance')
    plt.title('"Expectation of Unemployment chance vs Income"')

    # EDA Findings: There exists a weak correlation. People with lower household income tend to think of their unemployment 
    # chance to be lower. I infer the reason behind it might be that lower income jobs are more stable. 

    return figure_id_list