

import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import data_analysis
import data_analysis.Harshang.EDA
import data_analysis.Haowei.EDA

app = dash.Dash(__name__)
server = app.server



figure_id_list_Harshang = data_analysis.Harshang.EDA.EDA()
figure_id_list_Haowei = data_analysis.Haowei.EDA.EDA()
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



app.layout = html.Div([
    html.H1('Business Conditions'),

    html.Div('''
        BAGO: Would you say that at the present time business conditions
              are better or worse than they were a year ago? 
    '''),

    dcc.Graph(
        id=id1,
        figure=fig1
    ),

    html.Div('''
        BEXP: And how about a year from now, do you expect that in the
              country as a whole business conditions will be better, or
              worse than they are at present, or just about the same?
    '''),

    dcc.Graph(
        id=id2,
        figure=fig2
    ),

    html.Div('''
        BUS12: Now turning to business conditions in the
               country as a whole--do you think that during the next 12
               months we'll have good times financially, or bad times,
               or what?
    '''),

    dcc.Graph(
        id=id3,
        figure=fig3
    ),

    html.Div('''
        BUS12: Looking ahead, which would you say is more likely -- that
               in the country as a whole we'll have continuous good times
               during the next 5 years or so, or that we will have periods
               of widespread unemployment or depression, or what?
    '''),

    dcc.Graph(
        id=id4,
        figure=fig4
    ),

    html.Div('''
        UNEMP: Looking ahead, which would you say is more likely -- that
               in the country as a whole we'll have continuous good times
               during the next 5 years or so, or that we will have periods
               of widespread unemployment or depression, or what?
    '''),

    dcc.Graph(
        id=id5,
        figure=fig5
    ),

    html.Div('''
        GOVT: As to the economic policy of the government -- I mean steps
              taken to fight inflation or unemployment -- would you say the
              government is doing a good job, only fair, or a poor job?
    '''),

    dcc.Graph(
        id=id6,
        figure=fig6
    ),

    html.Div('''
        RATEX: No one can say for sure, but what do you think will happen to
               interest rates for borrowing money during the next 12
               months--will they go up, stay the same, or go down?
    '''),

    dcc.Graph(
        id=id7,
        figure=fig7
    ),

    html.Div('''
        AGE: Age distribution
    '''),

    dcc.Graph(
        id=id8,
        figure=fig8
    ),

    html.Div('''

    '''),
    
    dcc.Graph(
        id=id9,
        figure=fig9
    ),

    html.Div('''

    '''),

    dcc.Graph(
        id=id10,
        figure=fig10
    ),

    html.Div('''

    '''),
    
    dcc.Graph(
        id=id11,
        figure=fig11
    )


])

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)