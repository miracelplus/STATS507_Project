import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from pathlib import Path

def EDA():
    """EDA analysis code
    Returns:
        figure_and_explanation_list: This list contains the figure and the explanation
        [(figure, explanation), (figure, explanation), ...]
        figure should be a plotly figure object, and explanation should be a string
    """
    figure_id_list = []
    zixue_path = Path('data/Zixue/AAO2b05c.csv')

    df1 = pd.read_csv(zixue_path, sep=",", header=0)

    df1['Q'] = df1['YYYYQ'].astype(str).str[-1]

    # Convert the 'Q' column to integers
    df1['Q'] = df1['Q'].astype(int)

    averages_by_yyyyq = df1.groupby('YYYYQ').mean()
    columns_to_remove = [averages_by_yyyyq.columns[0], averages_by_yyyyq.columns[1], averages_by_yyyyq.columns[3]]
    averages_by_yyyyq = averages_by_yyyyq.drop(columns_to_remove, axis=1)
    zixue_path_gdp = Path('data/Zixue/gdp.xlsx')

    data = pd.read_excel(zixue_path_gdp, engine='openpyxl')

    data = data.dropna(axis=1, how='all')

    first_row_list = data.iloc[0].tolist()
    gdp = first_row_list[1:]

    averages_by_yyyyq = averages_by_yyyyq.iloc[:-1]

    averages_by_yyyyq['GDP'] = gdp

    correlation_matrix = averages_by_yyyyq.corr()

    heatmap = go.Figure(go.Heatmap(z=correlation_matrix, x=correlation_matrix.columns, y=correlation_matrix.columns,
                                   colorscale='Viridis'))

    # Update the layout to adjust the height, width, and title of the heatmap
    heatmap.update_layout(
        height=800,
        #width=850,
        title="Correlation plot of GDP and surveys of consumer variables"
    )
    id1 = "Correlation plot of GDP and surveys of consumer variables"
    bef1 = '''__Question__: What variable is highly correlated with GDP? 
    We would like to build machine learning model to do prediction based on the covariates the survey of customers provided and the time variables. 
    The covariates that is either positively correlated with GDP or negatively correlated with GDP will be selected to be the input of the machine learning model.
    '''
    aft1 = '''Based on the correlation plot above, we observed that GDP is highely correlated with YYYY (0.99, the year), INVAMT (-0.93 investment value) and WT (0.95, household head weight).
    Based on these finding, these three covariates are highly recommanded to be selected as input for machine learning model. However, other covariates with high absolute value
    of correlation can also be selected.
    '''
    figure_id_list.append((heatmap,id1,bef1,aft1))

    # Create a line plot of GDP versus YYYYQ
    gdp_line_plot = go.Figure(
        go.Scatter(x=list(range(len(averages_by_yyyyq.index))), y=averages_by_yyyyq['GDP'], mode='lines+markers'))

    # Update the layout to adjust the title of the line plot
    gdp_line_plot.update_layout(title="US GDP compared with time")

    # Set the x-axis to have equal distance between each value
    gdp_line_plot.update_xaxes(tickmode='array', tickvals=list(range(len(averages_by_yyyyq.index))),
                               ticktext=averages_by_yyyyq.index)

    id2 = "US GDP compared with time"
    bef2 = '''__Question__: What is general trend of US GDO according to different time period? Our group were considering about exploratory analysis of GDP trend first, to evaluate whether 
    GDP are expnentially increased or linearly increased according to time.
    '''
    aft2 = '''It seems that according to the plot above, the increase of GDP is more likely to be linear according to time. The reason could be the US is a developed nation, so its GDP
    is solely influenced by population growth and technology progress, and all of the two factors above are increase linearly. In this case, we do not need to do log transform on GDP to do 
    prediction based on machine learning model. Additionally, economists usually suggest that GDP has quarterly cycle because people living in the US tend to spend more on winter (Chrismas)
    and spend less on summer (summmer term). But according to the plot, we did not observed any clear cycle of GDP according to different quarter. 
    '''
    figure_id_list.append((gdp_line_plot,id2,bef2,aft2))


    box_plot_except_two = go.Figure()

    for column in averages_by_yyyyq.columns:
        if column not in ['HOMEAMT', 'INVAMT', 'GDP', 'YYYY', 'ICS', 'ICC', 'ICE', 'PAGOR1', 'NEWS1', 'NEWS2', 'PX1',
                          'PAGOR2', 'BUS5']:
            box_plot_except_two.add_trace(
                go.Box(y=averages_by_yyyyq[column], name=column, boxpoints='outliers', jitter=0.3, pointpos=-1.8))

    # Update the layout to adjust the title of the box plot
    box_plot_except_two.update_layout(title="Box Plots of Variables that range from 0 to 5")

    id3 = "Box Plots of Variables that range from 0 to 5"
    bef3 = '''__Question__: What are the mean and dispersion of each covariates? Through boxplot, our group would compare the mean, standard deviation, 25% quantile, 75% quantile and 
    outliers of each covariates. Because some covariates have large scale, we only select the covoariate that range from 0 to 5. All variables included for this plot are from
    survey of customers, and the clear definition for each variables are available at https://sda.umsurvey.org/sca/Doc/scax01.htm#1.HEADING. 
    '''
    aft3 = '''According to the plot, most of the covariates like CAR and HOM have more outliers than other covariates. Some of the covariates like WT has low standard deviation. 
    '''
    figure_id_list.append((box_plot_except_two,id3,bef3,aft3))
    # Create a box plot for HOMEAMT and INVAMT
    box_plot_two = go.Figure()

    gdp_vs_invamt = go.Figure(go.Scatter(x=averages_by_yyyyq['GDP'], y=averages_by_yyyyq['INVAMT'], mode='markers'))

    # Update the layout to adjust the title of the scatter plot
    gdp_vs_invamt.update_layout(title="Scatter plot of GDP vs INVAMT", xaxis_title="GDP", yaxis_title="INVAMT")

    id4 = "Scatter plot of GDP vs INVAMT"
    bef4 = '''__Question__: What is the relationship between GDP and INVAMT? Because the model are highly likely to select INVAMT as covariates, we would like to explore whether 
    WT are positively correlated or negatively correlated with GDP.
    
    '''
    aft4 = '''According to the plot, It seems that with higher GDO, the INVAMT tend to be lower. This is true because one of the GDP component is investment, so if family's investment
    worth more, it would mean the GDP would be higher. 
    '''
    figure_id_list.append((gdp_vs_invamt,id4,bef4,aft4))


    return figure_id_list
