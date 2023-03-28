import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import data_analysis
import base64
import data_analysis.Harshang.EDA
import data_analysis.Haowei.EDA
import data_analysis.Runxuan.EDA
import data_analysis.Zixue.EDA
# import data_analysis.Jingyi.EDA
# import data_analysis.Wei.EDA
# import data_analysis.Elena.EDA

app = dash.Dash(__name__)
server = app.server

figure_id_list_Harshang = data_analysis.Harshang.EDA.EDA()
figure_id_list_Haowei = data_analysis.Haowei.EDA.EDA()
figure_id_list_Runxuan = data_analysis.Runxuan.EDA.EDA()
# figure_id_list_Wei = data_analysis.Wei.EDA.EDA()
# figure_id_list_Jingyi = data_analysis.Jingyi.EDA.EDA()
# figure_id_list_Elena = data_analysis.Elena.EDA.EDA()
figure_id_list_Zixue = data_analysis.Zixue.EDA.EDA()

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

# fig14, id14 = figure_id_list_Wei[0]
# fig15, id15 = figure_id_list_Wei[1]

# fig16, id16 = figure_id_list_Jingyi[0]

# fig17, id17 = figure_id_list_Elena[0]
# fig18, id18 = figure_id_list_Elena[1]
# fig19, id19 = figure_id_list_Elena[2]

fig20, id20, bef20, aft20 = figure_id_list_Zixue[0]
fig21, id21, bef21, aft21 = figure_id_list_Zixue[1]
fig22, id22, bef22, aft22 = figure_id_list_Zixue[2]
fig23, id23, bef23, aft23 = figure_id_list_Zixue[3]


image_filename = 'data/GDP_prediction.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

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

        # Fig 8
        dcc.Markdown('''___'''),
        html.Div([
            html.H2('Consumer Age Distribution', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''This graph shows the distribution of consumer age in the United States.'''
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id8,
                    figure=fig8
                    ),
            dcc.Markdown('''The majority of the consumers are between 35 and 54 years old. However, we still have enough consumer data from other age groups to show the correlation in the next graph.'''
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),

        dcc.Markdown('''The economic condition, expectation, and sentiment of consumer should be influenced by their age. Also, they will be good indicators of the economic condition of the country. We want to see if there is any correlation between the age of the consumer and their economic sentiment.''', style={'fontSize': 18}),

        # Fig 9
        dcc.Markdown('''___'''),
        html.Div([
            html.H2('Average Index of Consumer Sentiment (ICS) for each age group', style={'color': 'green', 'fontSize': 22}),
            dcc.Graph(
                    id=id9,
                    figure=fig9
                    ),
        ]),
        dcc.Markdown('''___'''),
        
        # Fig 10
        dcc.Markdown('''___'''),
        html.Div([
            html.H2('Average Index of Consumer Condition (ICC) for each age group', style={'color': 'green', 'fontSize': 22}),
            dcc.Graph(
                    id=id10,
                    figure=fig10
                    ),
        ]),
        dcc.Markdown('''___'''),

        # Fig 11
        dcc.Markdown('''___'''),
        html.Div([
            html.H2('Average Index of Consumer Expectation (ICE) for each age group', style={'color': 'green', 'fontSize': 22}),
            dcc.Graph(
                    id=id11,
                    figure=fig11
                    ),
        ]),
        dcc.Markdown('''From the ICS, ICC, ICE figures above, we can see that all three indexes (which is highly correlated with the economic condition) decend with the increase of age, which may indicate the young people are generally more optimistic compared with the elder ones. Secondly, with the increase of age.''', style={'fontSize': 18}),

        # Fig 12 
        dcc.Markdown('''___'''),
        html.Div([
            html.H2('Level of Partisan for High and Low Income Groups', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown(bef12
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id12,
                    figure=fig12
                    ),
            dcc.Markdown(aft12
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),
        
        # Fig 13
        dcc.Markdown('''___'''),
        html.Div([
            html.H2('Economic Optimism in 5 Years for Different Age Groups', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown(bef13
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id13,
                    figure=fig13
                    ),
            dcc.Markdown(aft13
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),

        # Fig 20
        dcc.Markdown('''___'''),
        html.Div([
            html.H2('Correlation Between GDP and Consumer Survey Variables', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown(str(bef20)
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id20,
                    figure=fig20
                    ),
            dcc.Markdown(str(aft20)
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),

        # Fig 21
        dcc.Markdown('''___'''),
        html.Div([
            html.H2('US GDP for different years', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown(str(bef21)
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id21,
                    figure=fig21
                    ),
            dcc.Markdown(str(aft21)
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),

        # Fig 22
        dcc.Markdown('''___'''),
        html.Div([
            html.H2('Box Plot of Different Variables', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown(str(bef22)
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id22,
                    figure=fig22
                    ),
            dcc.Markdown(str(aft22)
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),

        # Fig 23
        dcc.Markdown('''___'''),
        html.Div([
            html.H2('GDP and INVAMT Scatter Plot', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown(str(bef23)
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id23,
                    figure=fig23
                    ),
            dcc.Markdown(str(aft23)
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),
        
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

        dcc.Markdown('''**Finally, We implemented recurrent neural network (RNN) with only one Simple RNN layer to predict GDP values based on input variables INVAMT (investment value), YYYY (the year), and WT (household head weight). The model is trained using a dataset of quarterly averages for these variables from survey of customers and seasonal unadjusted, real GDP obtained from IMF website. The dataset is preprocessed to normalize the GDP and input variable. Then the dataset is split in to three parts, training dataset to be all samples before and include 2002, validation dataset to be all samples from 2003 to 2012, testing dataset to be all samples from 2013 to 2022.**''', style={'fontSize': 18}),

        dcc.Markdown('''**After hyperparameter tuning, we train our model with 50 epochs using Adam (learning rate = 0.005) optimizer with mean square error as loss function.  The MAE value for our model on testing dataset is 0.075, indicating good performance of the model in predicting GDP values.**''', style={'fontSize': 18}),

        dcc.Markdown('''**Finally, a line plot is created to compare the true and predicted GDP values. The x-axis is year and y-axis are GDP. The plot shows that the model predictions closely follow the true values for testing sets. Because we did not implement warm-up approach, the model performs badly on the starting point of the testing dataset (year 2013). 
        **''', style={'fontSize': 18}),
        
        # COPY STARTING HERE
        dcc.Markdown('''___'''),
        html.Div([
            html.H2('GDP prediction using RNN', style={'color': 'green', 'fontSize': 22}),
            html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode())),
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
