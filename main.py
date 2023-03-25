import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import scipy
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
server = app.server

# Dictionaries for Survey Question Values
bago_dict = {1 : "Better Now", 3 : "About The Same", 5 : "Worse Now", 8 : "Don't Know", 9 : "NA"}
bexp_dict = {1 : "Better a Year From Now", 3 : "About The Same", 5 : "Worse a Year From Now", 8 : "Don't Know", 9 : "NA"}
bus12_dict = {1 : "Good Times", 2 : "Good With Qualifications", 3 : "Pro-Con", 4 : "Bad With Qualifications", 5 : "Bad times", 8 : "Don't Know", 9 : "NA"}
bus5_dict = {1 : "Good Times", 2 : "Good With Qualifications", 3 : "Pro-Con", 4 : "Bad With Qualifications", 5 : "Bad times", 98 : "Don't Know", 99 : "NA"}
unemp_dict = {1 : "More Unemployment", 3 : "About The Same", 5 : "Less Unemployment", 8 : "Don't Know", 9 : "NA"}
govt_dict = {1 : "Good Job", 3 : "Only Fair", 5 : "Poor Job", 8 : "Don't Know", 9 : "NA"}
ratex_dict = {1 : "Go Up", 3 : "Stay The Same", 5 : "Go Down", 8 : "Don't Know", 9 : "NA"}


# see https://plotly.com/python/px-arguments/ for more options

# Business Conditions Section from Survey
df1 = pd.read_csv("data/Business_Conditions_Datafile.csv", sep=",", header=0)

# Replace Survey Values with Dictionary Values
df1.replace({"BAGO" : bago_dict}, inplace=True)
df1.replace({"BEXP" : bexp_dict}, inplace=True)
df1.replace({"BUS12" : bus12_dict}, inplace=True)
df1.replace({"BUS5" : bus5_dict}, inplace=True)
df1.replace({"UNEMP" : unemp_dict}, inplace=True)
df1.replace({"GOVT" : govt_dict}, inplace=True)
df1.replace({"RATEX" : ratex_dict}, inplace=True)

print(df1)

# Plot BAGO Values: Would you say that at the present time business conditions are better or worse 
#                   than they were a year ago?
#
fig1 = px.bar(df1, x=df1['BAGO'].value_counts().index, y=df1['BAGO'].value_counts(normalize=True).mul(100).round(1).values,
            color=df1['BAGO'].value_counts().index.astype(str), labels=dict(x='BAGO', y='Frequency'),
            title="ECONOMY BETTER/WORSE YEAR AGO")
fig1.update_xaxes(type='category')
fig1.update_xaxes(categoryorder='category ascending')


# Plot BEXP Values: And how about a year from now, do you expect that in the country as a whole 
#                   business conditions will be better, or worse than they are at present, 
#                   or just about the same?
fig2 = px.bar(df1, x=df1['BEXP'].value_counts().index, y=df1['BEXP'].value_counts(normalize=True).mul(100).round(1).values,
            color=df1['BEXP'].value_counts().index.astype(str), labels=dict(x='BEXP', y='Frequency'),
            title="ECONOMY BETTER/WORSE NEXT YEAR")
fig2.update_xaxes(type='category')
fig2.update_xaxes(categoryorder='category ascending')


# Plot BUS12 Values: Now turning to business conditions in the
#               country as a whole--do you think that during the next 12
#               months we'll have good times financially, or bad times, or what?
fig3 = px.bar(df1, x=df1['BUS12'].value_counts().index, y=df1['BUS12'].value_counts(normalize=True).mul(100).round(1).values,
            color=df1['BUS12'].value_counts().index.astype(str), labels=dict(x='BUS12', y='Frequency'),
            title="ECONOMY GOOD/BAD NEXT YEAR")
fig3.update_xaxes(type='category')
fig3.update_xaxes(categoryorder='category ascending')


# Plot BUS5 Values: Looking ahead, which would you say is more likely -- that
#           in the country as a whole we'll have continuous good times
#           during the next 5 years or so, or that we will have periods
#           of widespread unemployment or depression, or what?
fig4 = px.bar(df1, x=df1['BUS5'].value_counts().index, y=df1['BUS5'].value_counts(normalize=True).mul(100).round(1).values,
            color=df1['BUS5'].value_counts().index.astype(str), labels=dict(x='BUS5', y='Frequency'),
            title="ECONOMY GOOD/BAD NEXT 5 YEARS")
fig4.update_xaxes(type='category')
fig4.update_xaxes(categoryorder='category ascending')


# Plot UNEMP Values: How about people out of work during the coming 12 months --
#            do you think that there will be more unemployment than now,
#            about the same, or less?
fig5 = px.bar(df1, x=df1['UNEMP'].value_counts().index, y=df1['UNEMP'].value_counts(normalize=True).mul(100).round(1).values,
            color=df1['UNEMP'].value_counts().index.astype(str), labels=dict(x='UNEMP', y='Frequency'),
            title="UNEMPLOYMENT MORE/LESS NEXT YEAR")
fig5.update_xaxes(type='category')
fig5.update_xaxes(categoryorder='category ascending')


# Plot GOVT Values: As to the economic policy of the government -- I mean steps
#           taken to fight inflation or unemployment -- would you say the
#           government is doing a good job, only fair, or a poor job?
fig6 = px.bar(df1, x=df1['GOVT'].value_counts().index, y=df1['GOVT'].value_counts(normalize=True).mul(100).round(1).values,
            color=df1['GOVT'].value_counts().index.astype(str), labels=dict(x='GOVT', y='Frequency'),
            title="GOVERNMENT ECONOMIC POLICY")
fig6.update_xaxes(type='category')
fig6.update_xaxes(categoryorder='category ascending')


# Plot RATEX Values: No one can say for sure, but what do you think will happen to
#            interest rates for borrowing money during the next 12
#            months--will they go up, stay the same, or go down?
fig7 = px.bar(df1, x=df1['RATEX'].value_counts().index, y=df1['RATEX'].value_counts(normalize=True).mul(100).round(1).values,
            color=df1['RATEX'].value_counts().index.astype(str), labels=dict(x='RATEX', y='Frequency'),
            title="INTEREST RATES UP/DOWN NEXT YEAR")
fig7.update_xaxes(type='category')
fig7.update_xaxes(categoryorder='category ascending')


app.layout = html.Div([
    html.H1('Business Conditions'),

    html.Div('''
        BAGO: Would you say that at the present time business conditions
              are better or worse than they were a year ago? 
    '''),

    dcc.Graph(
        id='BAGO-graph',
        figure=fig1
    ),

    html.Div('''
        BEXP: And how about a year from now, do you expect that in the
              country as a whole business conditions will be better, or
              worse than they are at present, or just about the same?
    '''),

    dcc.Graph(
        id='BEXP-graph',
        figure=fig2
    ),

    html.Div('''
        BUS12: Now turning to business conditions in the
               country as a whole--do you think that during the next 12
               months we'll have good times financially, or bad times,
               or what?
    '''),

    dcc.Graph(
        id='BUS12-graph',
        figure=fig3
    ),

    html.Div('''
        BUS12: Looking ahead, which would you say is more likely -- that
               in the country as a whole we'll have continuous good times
               during the next 5 years or so, or that we will have periods
               of widespread unemployment or depression, or what?
    '''),

    dcc.Graph(
        id='BUS5-graph',
        figure=fig4
    ),

    html.Div('''
        UNEMP: Looking ahead, which would you say is more likely -- that
               in the country as a whole we'll have continuous good times
               during the next 5 years or so, or that we will have periods
               of widespread unemployment or depression, or what?
    '''),

    dcc.Graph(
        id='UNEMP-graph',
        figure=fig5
    ),

    html.Div('''
        GOVT: As to the economic policy of the government -- I mean steps
              taken to fight inflation or unemployment -- would you say the
              government is doing a good job, only fair, or a poor job?
    '''),

    dcc.Graph(
        id='GOVT-graph',
        figure=fig6
    ),

    html.Div('''
        RATEX: No one can say for sure, but what do you think will happen to
               interest rates for borrowing money during the next 12
               months--will they go up, stay the same, or go down?
    '''),

    dcc.Graph(
        id='RATEX-graph',
        figure=fig7
    )

])

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)

def clean_POLAFF(df):
    df['POLAFF'] = df['POLAFF'].replace(1,'Republican')
    df['POLAFF'] = df['POLAFF'].replace(2,'Democrat')
    df['POLAFF'] = df['POLAFF'].replace(3,'Independent')
    df['POLAFF'] = df['POLAFF'].replace(8,'DontKnow')
    df['POLAFF'] = df['POLAFF'].replace(9,'NA')
    df['POLAFF'] = df['POLAFF'].replace('1','Republican')
    df['POLAFF'] = df['POLAFF'].replace('2','Democrat')
    df['POLAFF'] = df['POLAFF'].replace('3','Independent')
    df['POLAFF'] = df['POLAFF'].replace('8','DontKnow')
    df['POLAFF'] = df['POLAFF'].replace('9','NA')
    return df
def clean_AGE(df):
    df = df.drop(df[df.AGE == '  '].index)
    df["AGE"] = pd.to_numeric(df["AGE"])
    return df

#raw = pd.read_csv("~/507/alldata.csv")
#df = raw[['YYYY','POLAFF','AGE','YTL10','YTL90','BUS5']].copy()
#df.to_csv('data/df_max.csv')

df = pd.read_csv("data/df_max.csv")
df = clean_POLAFF(df)
df = clean_AGE(df)

start_yr = 1978
end_yr   = 2022
years = np.array(np.arange(start_yr,end_yr+1))

def politics_income(df, condition=None):
    RD = np.zeros(len(years))
    for yr in years:
        #print('\n', yr)
        thisdf = df[df['YYYY']==yr]
        thisdf = thisdf.drop(thisdf[thisdf.POLAFF == ' '].index)
        if condition == 'bottom10':
            thisdf = thisdf[thisdf['YTL10']=="1"]
        elif condition == 'top10':
            thisdf = thisdf[thisdf['YTL90']=="1"]
        if len(thisdf['POLAFF']) < 50:
            continue
        population = thisdf.shape[0]
        #print('population:', population)
        counts = thisdf['POLAFF'].value_counts()
        #print(counts)
        demo = counts['Democrat']
        repb = counts['Republican']
        indp = counts['Independent']
        #print((demo+repb)/population)
        RD[yr-start_yr] = (demo+repb)/population
    return RD

RD       = politics_income(df)
RD_bot10 = politics_income(df,'bottom10')
RD_top10 = politics_income(df,'top10')

plotyrs = years[years>2004]
aa = RD_bot10[years>2004]
plotRD_bot10 = aa[aa != 0]
plotyrs = plotyrs[aa != 0]
plotyrs = plotyrs[plotyrs>2004]
bb = RD_top10[years>2004]
plotRD_top10 = bb[aa != 0]

RDdf = pd.DataFrame({"years":plotyrs,"top10":plotRD_top10,"bot10":plotRD_bot10})
plt.figure()
plt.plot(plotyrs,plotRD_top10,'o-',label='top10%')
plt.plot(plotyrs,plotRD_bot10,'o-',label='bottom10%')
plt.ylabel('(Demo+Repub)/All')
plt.xlabel('year')
plt.legend()
plt.savefig("graphs/politics_income.png")


def business5_age(df):
    good_yng = np.zeros(len(years))
    good_mid = np.zeros(len(years))
    good_old = np.zeros(len(years))
    for yr in range(1978,2023):
        thisdf = df[df['YYYY']==yr]
        age1, age2 = thisdf['AGE'].quantile(0.33), thisdf['AGE'].quantile(0.67)
        dfyng = thisdf[thisdf['AGE'] <= age1]
        dfmid = thisdf[thisdf['AGE'].between(age1, age2)]
        dfold = thisdf[thisdf['AGE'] >= age2]
        #print(dfyng.shape[0])
        #print(dfmid.shape[0])
        #print(dfold.shape[0])
        counts_yng = dfyng['BUS5'].value_counts()
        counts_mid = dfmid['BUS5'].value_counts()
        counts_old = dfold['BUS5'].value_counts()
        population = thisdf.shape[0]
        good_yng[yr-start_yr] = (counts_yng[1]+counts_yng[2])/population
        good_mid[yr-start_yr] = (counts_mid[1]+counts_mid[2])/population
        good_old[yr-start_yr] = (counts_old[1]+counts_old[2])/population
    return good_yng,good_mid,good_old

good_yng,good_mid,good_old = business5_age(df)
bizagedf = pd.DataFrame({'years':years,'young':good_yng,'middle aged':good_mid,'senior':good_old})
plt.figure()
plt.plot(years,good_yng,label='young')
plt.plot(years,good_mid,label='middle aged')
plt.plot(years,good_old,label='senior')
plt.xlabel('year')
plt.ylabel('Fraction of Being Opstimistic')
plt.legend()
plt.savefig('graphs/business5_age.png')




app = dash.Dash(__name__)
server = app.server
pd.options.plotting.backend = "plotly"

fig = RDdf.plot(x='years', y=['top10', 'bot10'])
#fig.set_ylabel("Fraction of the Population with a Political Preference")

fig2 = bizagedf.plot(x='years',y=['young','middle aged','senior'])

app.layout = html.Div([
    html.H1('Hello Dash'),

    html.Div('''
        Dash: A web application framework for your data. 
    '''),

    dcc.Graph(
        id='Fraction of the Population with a Political Preference',
        figure=fig
    ),

    html.Div('''
        Dash: Another example for chart
    '''),

    dcc.Graph(
        id='Fraction of the Population Optimistic about the Business Condition in Five Years',
        figure=fig2
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
