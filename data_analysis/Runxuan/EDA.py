import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import scipy
import dash
from dash import dcc
from dash import html
import plotly.express as px


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



df = pd.read_csv("data/df_max.csv")
df = clean_POLAFF(df)
df = clean_AGE(df)

start_yr = 1978
end_yr   = 2022
years = np.array(np.arange(start_yr,end_yr+1))

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

def EDA():
    """EDA analysis code

    Returns:
        figure_and_explanation_list: This list contains the figure and the explanation
        [(figure, explanation), (figure, explanation), ...]
        figure should be a plotly figure object, and explanation should be a string
    """
    figure_id_list = []
    RDdf = pd.DataFrame({"years":plotyrs,"top10":plotRD_top10,"bot10":plotRD_bot10})
    plt.figure()
    plt.plot(plotyrs,plotRD_top10,'o-',label='top10%')
    plt.plot(plotyrs,plotRD_bot10,'o-',label='bottom10%')
    plt.ylabel('(Demo+Repub)/All')
    plt.xlabel('year')
    plt.legend()
    plt.savefig("graphs/politics_income.png")

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
    return figure_id_list
