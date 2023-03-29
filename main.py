import dash
from dash import dcc, html, Input, Output
from dash.exceptions import PreventUpdate
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import data_analysis
import base64
import data_analysis.Harshang.EDA
import data_analysis.Haowei.EDA
import data_analysis.Runxuan.EDA
import data_analysis.Zixue.EDA
import data_analysis.Jingyi.EDA
import data_analysis.Wei.EDA
import data_analysis.Elena.EDA
#import prediction.ploting


# Final prediction results obtained from the RNN Model
pred_results_dict = {'2013': 16.79052825, '2014': 17.0549630, '2015': 17.3859760, 
                     '2016': 17.6735540, '2017': 17.9352710, '2018': 18.2134825, 
                     '2019': 18.5091240, '2020': 18.7704145, '2021': 19.1537770, 
                     '2022': 19.4697795}

app = dash.Dash(__name__)
server = app.server

figure_id_list_Harshang = data_analysis.Harshang.EDA.EDA()
figure_id_list_Haowei = data_analysis.Haowei.EDA.EDA()
figure_id_list_Runxuan = data_analysis.Runxuan.EDA.EDA()
figure_id_list_Wei = data_analysis.Wei.EDA.EDA()
figure_id_list_Jingyi = data_analysis.Jingyi.EDA.EDA()
figure_id_list_Elena = data_analysis.Elena.EDA.EDA()
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

fig14, id14 = figure_id_list_Wei[0]
fig15, id15 = figure_id_list_Wei[1]

fig16, id16 = figure_id_list_Jingyi[0]

fig17, id17 = figure_id_list_Elena[0]
fig18, id18 = figure_id_list_Elena[1]
fig19, id19 = figure_id_list_Elena[2]

fig20, id20, bef20, aft20 = figure_id_list_Zixue[0]
fig21, id21, bef21, aft21 = figure_id_list_Zixue[1]
fig22, id22, bef22, aft22 = figure_id_list_Zixue[2]
fig23, id23, bef23, aft23 = figure_id_list_Zixue[3]


image_filename = 'data/GDP_prediction.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

image_filename2 = 'data/GDP_consumer_pred.png'
encoded_image2 = base64.b64encode(open(image_filename2, 'rb').read())

image_filename3 = 'data/GDP_worldbank_pred.png'
encoded_image3 = base64.b64encode(open(image_filename3, 'rb').read())

image_filename4 = 'data/GDP.png'
encoded_image4 = base64.b64encode(open(image_filename4, 'rb').read())

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
                        3. [_FiveThirtyEight_](https://data.fivethirtyeight.com/)
                        4. [_IMF_](https://data.imf.org/?sk=388dfa60-1d26-4ade-b505-a05a558d9a42)'''
                        
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
                    '''
                    , style={'fontSize': 18}),
    ]),

    html.Div([
        html.H2('Exploratory Data Analysis (EDA)', style={'color': 'blue'}),
        dcc.Markdown('''We started by exploring the variables in the [_umsurvey_](https://sda.umsurvey.org/sda-public/cgi-bin/hsda2?setupfile=harcsda&datasetname=sca&ui=2&action=subset)
                        dataset to find the trends within the variables and the correlations between the variables.'''
                    , style={'fontSize': 18}),
        
        # COPY STARTING HERE
        #dcc.Markdown('''___'''),
        #dcc.Markdown('''__USE THIS AS A TEMPLATE TO INSERT YOUR PLOTS AND RELATED INFORMATION__'''),
        #html.Div([
        #    html.H2('Graph Title HERE', style={'color': 'green', 'fontSize': 22}),
        #    dcc.Markdown('''**Assumptions and EDA Question HERE**'''
        #    , style={'fontSize': 18}),
        #    dcc.Graph(
        #            id=id1,
        #            figure=fig1
        #            ),
        #    dcc.Markdown('''**Actual Findings HERE**'''
        #    , style={'fontSize': 18}),
        #]),
        #dcc.Markdown('''___'''),
        # COPY ENDING HERE

        # Fig 1
        dcc.Markdown('''___'''),
        html.Div([
            html.H2('Business Conditions Now Compared to A Year Ago', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''The graph shows consumer sentiment about business conditions now compared to one year ago.'''
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id1,
                    figure=fig1
                    ),
            dcc.Markdown('''On average, every year consumers have mixed feeling on how the economy is doing compared to 
                            the previous year. Because they are split between better now and worse now, we could analysize
                            how this is related to their income, age, education etc.'''
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),

        # Fig 2
        #dcc.Markdown('''___'''),
        html.Div([
            html.H2('Business Conditions A Year From Now', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''The graph shows consumer sentiment about business conditions after one year.'''
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id2,
                    figure=fig2
                    ),
            dcc.Markdown('''Overall, every year consumers are more hopeful that the economy will improve or remain same
                            in the  future.'''
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),

        # Fig 3
        #dcc.Markdown('''___'''),
        html.Div([
            html.H2('Business Conditions A Year From Now with Qualifications', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''The graph shows consumer sentiment about business conditions after one year with qualifications.'''
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id3,
                    figure=fig3
                    ),
            dcc.Markdown('''It is interesting to see that getting some qualifications within the year does not seem to influence
                            consumer sentiment about economic conditions in the next year. Consumers are again split between good times
                            and bad times. More analysis is need to gain useful insight.'''
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),

        # Fig 4
        #dcc.Markdown('''___'''),
        html.Div([
            html.H2('Business Conditions 5 Years From Now with Qualifications', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''The graph shows consumer sentiment about business conditions after five years with qualifications.'''
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id4,
                    figure=fig4
                    ),
            dcc.Markdown('''Qualifications seems to matter more to the overall economic conditions after 5 years. But, the consumer
                            sentiment is still mainly split between good time and bad times.'''
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),

        # Fig 5
        #dcc.Markdown('''___'''),
        html.Div([
            html.H2('Unemployment A Year From Now', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''The graph shows consumer sentiment about unemployment in the next year.'''
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id5,
                    figure=fig5
                    ),
            dcc.Markdown('''Every year, consumers are less hopeful about the employment opportunities in the next year.
                            It would be interesting to see this distribution with respect to year, income, education, government policy etc.'''
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),

        # Fig 6
        #dcc.Markdown('''___'''),
        html.Div([
            html.H2('Government Economic Policy Perception', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''The graph shows consumer sentiment about government economic policy to fight inflation and unemployment, year after year.'''
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id6,
                    figure=fig6
                    ),
            dcc.Markdown('''Overall, consumers are hopeful that the government is doing fair/good job at fighting inflation and unemployment.
                            '''
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),

        # Fig 7
        #dcc.Markdown('''___'''),
        html.Div([
            html.H2('Interest Rates A Year From Now', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''The graph shows consumer sentiment about interest rates in the next year.'''
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id7,
                    figure=fig7
                    ),
            dcc.Markdown('''Every year the consumers feel that the interest rates will go up or stay the same.'''
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),
        

        # Fig 8
        #dcc.Markdown('''___'''),
        html.Div([
            html.H2('Consumer Age Distribution', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''This graph shows the distribution of consumer age in the United States.'''
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id8,
                    figure=fig8
                    ),
            dcc.Markdown('''The majority of the consumers are between 35 and 54 years old. However, we still have 
                            enough consumer data from other age groups to show the correlation in the next graph.'''
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),

        dcc.Markdown('''The economic condition, expectation, and sentiment of consumer should be influenced by their age. 
                        Also, they will be good indicators of the economic condition of the country. We want to see if there 
                        is any correlation between the age of the consumer and their economic sentiment.'''
                , style={'fontSize': 18}),

        # Fig 9
        dcc.Markdown('''___'''),
        html.Div([
            html.H2('Average Index of Consumer Sentiment (ICS) for each age group', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''Consumer sentiment refers to the overall attitude or outlook that consumers have towards the economy
                             and their personal financial situation. It is typically measured through surveys that ask consumers about
                             their current and future expectations for things like job security, income growth, and the overall state
                             of the economy.'''
                , style={'fontSize': 18}),
            dcc.Graph(
                    id=id9,
                    figure=fig9
                    ),
        ]),
        dcc.Markdown('''___'''),
        
        # Fig 10
        #dcc.Markdown('''___'''),
        html.Div([
            html.H2('Average Index of Consumer Condition (ICC) for each age group', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''Consumer conditions refer to the current state of the economy and how it is affecting consumers.
                            This includes factors like employment rates, inflation, and overall economic growth.'''
                , style={'fontSize': 18}),
            dcc.Graph(
                    id=id10,
                    figure=fig10
                    ),
        ]),
        dcc.Markdown('''___'''),

        # Fig 11
        #dcc.Markdown('''___'''),
        html.Div([
            html.H2('Average Index of Consumer Expectation (ICE) for each age group', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''Consumer expectations, on the other hand, refer to consumers' predictions for how the economy will perform
                            in the future. This includes things like their expectations for future job prospects, income growth,
                            and overall economic conditions.'''
                , style={'fontSize': 18}),
            dcc.Graph(
                    id=id11,
                    figure=fig11
                    ),
        ]),
        dcc.Markdown('''All of these factors are important for businesses and policymakers to consider when making decisions about things like pricing,
                        investment, and economic policy. By understanding consumer sentiment, conditions, and expectations, they can better anticipate
                        how consumers are likely to behave and adjust their strategies accordingly. 
                        ''', style={'fontSize': 18}),
        dcc.Markdown('''From the ICS, ICC, ICE figures above, we can see that all three indexes (which is highly correlated with the economic condition) 
                        decreases with the increase of age, which may indicate the young people are generally more optimistic compared with the elder ones. 
                        ''', style={'fontSize': 18}),

        # Fig 12 
        dcc.Markdown('''___'''),
        html.Div([
            html.H2('Level of Partisanship for High and Low Income Groups', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown(bef12, style={'fontSize': 18}),
            dcc.Graph(
                    id=id12,
                    figure=fig12
                    ),
            dcc.Markdown(aft12
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),
        
        # Fig 13
        #dcc.Markdown('''___'''),
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
        
        
        # Fig 14 
        dcc.Markdown('''Next two graphs are aimed to find out whether there's any inequality between gender when it comes to the distribution of income.'''
            , style={'fontSize': 18}),
        html.Div([
            html.H2('The Comparision of the income distribution between male and female', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''It is assumed that in most job categories males tend to earn more than females for the same job.
                            In the graph, we can compare the distribution of sex for a given income range.'''
                    , style={'fontSize': 18}),
            dcc.Graph(
                    id=id14,
                    figure=fig14
                    ),
        ]),
        dcc.Markdown('''From the graphs, we can see that for imcome range between $0 - $50000, males earn more than female whereas
                        for imcome range between $50000 - $100000, females earn more than males. Therefore, Women's income is higher that men's.''', style={'fontSize': 18}),
        
        # Fig 15 
        
        html.Div([
            html.H2('The Comparision of the income distribution between different education level', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''Now let's look at a possible reason for the above result.''', style={'fontSize': 18}),
            dcc.Graph(
                    id=id15,
                    figure=fig15
                    ),
        ]),
        dcc.Markdown('''No matter in which education level, the population of women is larger than men. Hence, Receiving higher education attributes to females earning more income than males.''', style={'fontSize': 18}),

        # fig 16
        dcc.Markdown('''___'''),
        html.Div([
            html.H2('Expectation of Unemployment Chance vs Income', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''Does there exist a correlation between people's expectation of unemployment chance over the next 5 years and their household income in the previous year?'''
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id16,
                    figure=fig16
                    ),
            dcc.Markdown('''There exists a weak correlation. People with lower household income tend to think of their unemployment chance to be lower. I infer the reason behind it might be that lower income jobs are more stable. '''
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),
        
        # fig 17
        #dcc.Markdown('''___'''),
        html.Div([
            html.H2('Personal Finance Histogram', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''This histogram shows whether current personal finance has gotten better or worse than 5 years ago and whether it is expected to be better or worse 5 years from now.'''
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id17,
                    figure=fig17
                    ),
            dcc.Markdown('''The majority of the people have lower responses, meaning that they believe that their current personal finance has gotten better than 5 years ago and they expect it to become better 5 years in the future.'''
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),
        
        # fig 18
        #dcc.Markdown('''___'''),
        html.Div([
            html.H2('Average Personal Finance by Age Group', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''This bar graph shows the average response to whether current personal finance has gotten better or worse than 5 years ago and whether it is expected to be better or worse 5 years from now for each age group.'''
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id18,
                    figure=fig18
                    ),
            dcc.Markdown('''For each age group, the average response of comparing current personal finance to that of 5 years ago is correlated to the average response of comparing current personal finance to that of 5 years in the future. The average response is lower for younger age groups, meaning that the personal finance of young adults has gotten better and they expect it to be better in the future, compared to older adults.'''
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),
        
        # fig 19
        #dcc.Markdown('''___'''),
        html.Div([
            html.H2('Average Personal Finance by number of kids group', style={'color': 'green', 'fontSize': 22}),
            dcc.Markdown('''This bar graph shows the average response to whether current personal finance has gotten better or worse than 5 years ago and whether it is expected to be better or worse 5 years from now for each number of kids group.'''
            , style={'fontSize': 18}),
            dcc.Graph(
                    id=id19,
                    figure=fig19
                    ),
            dcc.Markdown('''For each number of kids group, the average response of comparing current personal finance to that of 5 years ago is correlated to the average response of comparing current personal finance to that of 5 years in the future. The average response is higher for households with no kids, meaning that the personal finance of these households has not gotten better and they expect it to be the same in the future, compared to households with children.'''
            , style={'fontSize': 18}),
        ]),
        dcc.Markdown('''___'''),

        # Fig 20
        #dcc.Markdown('''___'''),
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
        #dcc.Markdown('''___'''),
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
        #dcc.Markdown('''___'''),
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
        #dcc.Markdown('''___'''),
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
        
        dcc.Markdown('''In this section, we would like to build model to predict real, seasonal unadjusted gdp based on variables provided from Survey of Customers.
        The reason for choose gdp as our predictor is because it is pre-assumed that customer behavior would influence GDP natioally because GDP approximately equal to 
        Consumption + Investment + Government Spending. We choose real GDP (in million dolars) mainly because we would like our data to be adjusted from inflation, since government behavior
        like monetary policy is unpredictable. We choose YYYY (the year), INVAMT (investment value), WT (household head weight), PAGOR1 (REASONS: FINANCES B/W YR AGO (1))
        and HOMEAMT (market value of home) as our covariates mainly because for those variables they are highly correlated with GDP (>0.80 or <-0.80 for correlation coefficient). 
        
                    '''
                    , style={'fontSize': 18}),
        
        html.P('Here are the models we chose to predict GDP: ', style={'fontSize': 18}),
        dcc.Markdown('''
                        1. Linear Regression (Ordinary least square)
                        2. XG Boost
                        3. Random Forest
                        4. Linear Regression (SGD)
                        5. Recurrent Neural Network (RNN)
                    '''
                    , style={'fontSize': 18}),
        dcc.Markdown('''We started with the first three model first. Parameters for linear regression model are optimized through OLS (ordinary least square). We choose the number of 
        estimators to be 5 and random state to be 5 for both XG Boost model and Random Forest model. We select YYYY (the year), INVAMT (investment value), WT (household head weight), PAGOR1 (REASONS: FINANCES B/W YR AGO (1))
        and HOMEAMT (market value of home) as covariates for model training. The dataset is divided into three parts: training dataset to be year before 2003, validation dataset 
        to be from year 2003 and year 2012, and testing dataset to be year after 2012. 
        
        ''', style={'fontSize': 18}),

        html.Div([
            html.H2('GDP Prediction using Consumer Report Dataset', style={'color': 'green', 'fontSize': 22}),
            html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode()), style={'height':'100%', 'width':'100%'}),
        ]),
        
        dcc.Markdown('''Fit result: ''', style={'fontSize': 18}),
        dcc.Markdown('''
            * Linear regression test MSE:0.012
            * Random forest test MSE: 0.36
            * XGBoost test MSE: 0.43
        '''
                    , style={'fontSize': 18}),
        
        dcc.Markdown('''Based on the plot above, The Random Forest model and XG boost model are not able to learn from the training dataset and output decent prediction.
        This could be attributed to the fact that these two model are not designed to treat sequential data. Linear regression model with OLS perform good on predicting the
        upward trend of GDP. The prediction is very close to the true gdp value from 2013 to 2022'''
                    , style={'fontSize': 18}),

        
        # COPY STARTING HERE
        dcc.Markdown('''___'''),
        html.Div([
            html.H2('GDP Prediction using Linear Regression (SGD)', style={'color': 'green', 'fontSize': 22}),

            dcc.Markdown('''We also tried to get a linear regression model using stochastic gradient descent method to predict the U.S. GDP (in million dollars) 
                            from 2013 to 2022. The motivation for choosing the SGD method is to look for potential improvement on the linear model presented in 
                            the section above, via (a) using a larger dataset and (b) using SGD instead of direct fitting.
                            This model is trained on the same dataset and using the same three features (investment, year, and household head weight),
                            quarterly averaged in the same way as the RNN model introduced in the next section.
                            Data spiting: training set: 1978 to 2008; validation set: 2008 to 2012; testing set: 2013 to 2022
                        ''', style={'fontSize': 18}),
            dcc.Markdown('''Hyperparameter tuning: we scan the parameter alpha (the multiplier that controls the L2 regularization) in some range and select the value
                            , alpha = 0.096, that gives the best performance on the validation set.
                        ''', style={'fontSize': 18}),
            
            html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()), style={'height':'100%', 'width':'100%'}),
            
            dcc.Markdown('''Fit result: ''', style={'fontSize': 18}),
            dcc.Markdown('''
                            * Mean Absolute Error: 163931 million dollars
                            * Root Mean Squared Error: 195413 million dollars
                            * Mean Squared Error:38186424205 million dollars
                        '''
                    , style={'fontSize': 18}),
            
            dcc.Markdown('''The figure above shows the model's prediction for the U.S. GDP from 1978 to 2022, where the first few decades until
                            2008 is the training set. The graph indicates that the model can predict the large increasing trend of GDP, but failed to predict 
                            short-term fluctuations such as the sudden decrease of GDP in 2008 and 2022.'''
                    , style={'fontSize': 18}),

            
        ]),
        dcc.Markdown('''___'''),
        # COPY ENDING HERE


        # COPY STARTING HERE
        #dcc.Markdown('''___'''),
        html.Div([
            html.H2('GDP Prediction using RNN', style={'color': 'green', 'fontSize': 22}),

            dcc.Markdown('''Additionally, We implemented recurrent neural network (RNN) with only one Simple RNN layer to predict GDP values
                        based on input variables INVAMT (investment value), YYYY (the year), and WT (household head weight).
                        The dataset is preprocessed to normalize the
                        GDP and input variable. Then the dataset is split in to three parts, training dataset to be all samples
                        before and include 2002, validation dataset to be all samples from 2003 to 2012, testing dataset to be all
                        samples from 2013 to 2022.''', style={'fontSize': 18}),

            dcc.Markdown('''After hyperparameter tuning, we train our model with 50 epochs using Adam (learning rate = 0.005) optimizer
                        with mean square error as loss function.  The MSE value for our model on testing dataset is 0.075, indicating
                        good performance of the model in predicting GDP values.''', style={'fontSize': 18}),

            dcc.Markdown('''Finally, a line plot is created to compare the true and predicted GDP values. The x-axis is year and y-axis are
                        GDP. The plot shows that the model predictions closely follow the true values for testing sets. Because we
                        did not implement warm-up approach, the model performs badly on the starting point of the testing dataset
                        (year 2013).'''
                    , style={'fontSize': 18}),

            html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'height':'100%', 'width':'100%'}),
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
                {'label': '2016', 'value': '2016'},
                {'label': '2017', 'value': '2017'},
                {'label': '2018', 'value': '2018'},
                {'label': '2019', 'value': '2019'},
                {'label': '2020', 'value': '2020'},
                {'label': '2021', 'value': '2021'},
            ],            
            placeholder="Select a Year",
            #value=2013,
            id='prediction-year'
        ),
        html.Div(id='dd-output-container', style={'fontSize': 18})



    ]),

    html.Div([
        html.H2('Final Conclusion', style={'color': 'blue'}),
        html.P('''The prediction result shows that linear regression model maintains a higher performance than random forest model and XG boost model. However, 
        with larger sample sizes, RNN model seems to have better performance compared with linear regression model. The machine learning model is able to 
        predict general upward trend of GDP increase for the US. However, the temporary recession caused by events like covid-19 is still unpredictable.''', style={'fontSize': 18})
    ]),

])

@app.callback(
    Output('dd-output-container', 'children'),
    Input('prediction-year', 'value'), prevent_initial_call=True
)

def update_output(value):
    if value is None:
        raise PreventUpdate
    else:
        return f'The GDP of United States in {value} is predicted to be : ${pred_results_dict[value]} trillion'




if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
