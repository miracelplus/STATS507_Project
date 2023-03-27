import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import data_analysis
import data_analysis.Harshang.EDA
import data_analysis.Haowei.EDA
import data_analysis.Runxuan.EDA
import data_analysis.Jingyi.EDA
import data_analysis.Wei.EDA
import data_analysis.Elena.EDA

app = dash.Dash(__name__)
server = app.server

figure_id_list_Harshang = data_analysis.Harshang.EDA.EDA()
figure_id_list_Haowei = data_analysis.Haowei.EDA.EDA()
figure_id_list_Runxuan = data_analysis.Runxuan.EDA.EDA()
figure_id_list_Wei = data_analysis.Wei.EDA.EDA()
figure_id_list_Jingyi = data_analysis.Jingyi.EDA.EDA()
figure_id_list_Elena = data_analysis.Elena.EDA.EDA()

fig1, id1 = figure_id_list_Harshang[0]
fig2, id2 = figure_id_list_Harshang[1]
fig3, id3 = figure_id_list_Harshang[2]
fig4, id4 = figure_id_list_Harshang[3]
fig5, id5 = figure_id_list_Harshang[4]
fig6, id6 = figure_id_list_Harshang[5]
fig7, id7 = figure_id_list_Harshang[6]

fig8, id8 = figure_id_list_Haowei[0]
fig9, id9 = figure_id_list_Haowei[1]
fig10, id10 = figure_id_list_Haowei[2]
fig11, id11 = figure_id_list_Haowei[3]

fig12,id12,bef12,aft12 = figure_id_list_Runxuan[0]
fig13,id13,bef13,aft13 = figure_id_list_Runxuan[1]

fig14, id14 = figure_id_list_Wei[0]
fig15, id15 = figure_id_list_Wei[1]

fig16, id16 = figure_id_list_Jingyi[0]

fig17, id17 = figure_id_list_Elena[0]
fig18, id18 = figure_id_list_Elena[1]
fig19, id19 = figure_id_list_Elena[2]



app.layout = html.Div([

    html.H1('Analytics Dashboard for STATS 507', 
            style={'color': 'black', 
                   'fontSize': 40,
                   'textAlign': 'center'}),
    
    
    html.Div([
        html.H2('Project Goals', style={'color': 'blue'}),
        html.P('''The goal of this project is the create an analytics dashboard application to explore
                  the collected data, and create predictive analysis models to predict the Gross Domestic Product (GDP)
                  of the Unites States of America.   
                  We used Pandas to analyze the datasets, Plotly to graph the data, 
                  Dash to build the application, and Google Cloud Platform (GCP) to host the application.'''
            , style={'fontSize': 18})
    ]),

    html.Div([
        html.H2('Data Collection', style={'color': 'blue'}),
        html.P('Data is collected from following sources: ', style={'fontSize': 18}),
        dcc.Markdown('''
                        1. [_umsurvey_](https://sda.umsurvey.org/sda-public/cgi-bin/hsda2?setupfile=harcsda&datasetname=sca&ui=2&action=subset)
                        2. [_The World Bank_](https://data.worldbank.org/)
                        3. [_FiveThirtyEight_](https://data.fivethirtyeight.com/)'''
                    , style={'fontSize': 18}),
    ]),

    html.Div([
        html.H2('Data Importing', style={'color': 'blue'}),
        html.P('''All the datasets were imported in csv format for easy integration with Pandas dataframe,
                and easy visual validation of the data in the dataset. We collected data throughout the span of the project
                to add most possible datapoints required for the important variables in the EDA stage and predictive analysis stage.'''
            , style={'fontSize': 18})
    ]),

    html.Div([
        html.H2('Data Cleaning', style={'color': 'blue'}),
        html.P('Data cleaning consists of following steps: ', style={'fontSize': 18}),
        dcc.Markdown('''
                        1. Replacing all the empty data cells with `NaN` value.
                        2. Removing all the records with `NaN` values.
                        3. Removing duplicated records.
                        4. **ADD MORE STEPS IF NEEDED**
                    '''
                    , style={'fontSize': 18}),
    ]),

    html.Div([
        html.H2('Exploratory Data Analysis (EDA)', style={'color': 'blue'}),
        dcc.Markdown('''We started by exploring the variables in the [_umsurvey_](https://sda.umsurvey.org/sda-public/cgi-bin/hsda2?setupfile=harcsda&datasetname=sca&ui=2&action=subset)
                        dataset to find the trends within the variables and the correlations between the variables.'''
                    , style={'fontSize': 18}),
        
        # COPY STARTING HERE
        dcc.Markdown('''___'''),
        dcc.Markdown('''__USE THIS AS A TEMPLATE TO INSERT YOUR PLOTS AND RELATED INFORMATION__'''),
        html.Div([
            html.H2('Graph Title HERE', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''**Assumptions and EDA Question HERE**'''
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id1,
                    figure=fig1
                    ),
            dcc.Markdown('''**Actual Findings HERE**'''
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),
        # COPY ENDING HERE
        
        
    ]),

    html.Div([
        html.H2('Predictive Analysis', style={'color': 'blue'}),
        html.P('''After exploring various variables in the datasets and their correlations,
                we chose to build predictive models to predict the GDP of United States.'''
            , style={'fontSize': 18}),
        
        html.P('Here are the models we chose to predict GDP: ', style={'fontSize': 18}),
        dcc.Markdown('''
                        1. Linear Regression
                        2. XG Boost
                        3. Recurrent Neural Network (RNN)
                        4. **EDIT ABOVE MODELS IF NEEDED**
                    '''
                    , style={'fontSize': 18}),
        
        html.P('Here are the variables we used to build the above models: ', style={'fontSize': 18}),
        dcc.Markdown('''
                        1. Spending
                        2. Interest Rates
                        3. Unemployment
                        4. Inflation
                        5. **ADD MORE VARIABLES AS NEEDED**
                    '''
                    , style={'fontSize': 18}),
        
        dcc.Markdown('''**Talk about if some of the above variables are better/worse predictors
                        of the GDP. If so which ones did we end up using in the end**'''
                    , style={'fontSize': 18}),
        
        dcc.Markdown('''**Compare and contrast the 3 predictive models and their training and testing.
                        How did we partition data for testing and testing?
                        Which model has best accuracy among all?
                        Which model did we end up using in the end?**'''
                    , style={'fontSize': 18}),
        
        # COPY STARTING HERE
        dcc.Markdown('''___'''),
        dcc.Markdown('''__USE THIS AS A TEMPLATE TO INSERT THE PREDICTION GRAPH AND RELATED INFORMATION__'''),
        html.Div([
            html.H2('Graph Title HERE', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''**Assumptions and EDA Question HERE**'''
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id2,
                    figure=fig2
                    ),
            dcc.Markdown('''**Actual Findings HERE**'''
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),
        # COPY ENDING HERE

        dcc.Markdown('''**Select the year for which you would like to see the predicted GDP of United States**'''
                    , style={'fontSize': 18}),
        dcc.Dropdown(
            options=[
                {'label': '2013', 'value': '2013'},
                {'label': '2014', 'value': '2014'},
                {'label': '2015', 'value': '2015'},
            ],            
            placeholder="Select a Year",
            id='demo-dropdown'
        ),
        html.Div(id='dd-output-container')



    ]),

    html.Div([
        html.H2('Final Conclusion', style={'color': 'blue'}),
        html.P('Write about the conclusion reached from EDA and Prediction.', style={'fontSize': 18})
    ]),

])

@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)

def update_output(value):
    return f'The GDP of United States in {value} is predicted to be : '




if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
