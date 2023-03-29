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

    # plot a scatterplot of income v pjob, add labels and title
    fig = px.scatter(data, x='INCOME', y='PJOB', 
                     labels={'INCOME': 'Income', 'PJOB': 'Expectation of Unemployment Chance'})

    fig.update_layout(title={'text': 'Expectation of Unemployment chance vs Income', 'x': 0.5},
                      xaxis_title='Income',
                      yaxis_title='Expectation of Unemployment Chance')

    # fig.show()

    # EDA Findings: There exists a weak correlation. People with lower household income tend to think of their unemployment 
    # chance to be lower. I infer the reason behind it might be that lower income jobs are more stable. 

    return [(fig, 'Expectation of Unemployment Chance vs Income')]

