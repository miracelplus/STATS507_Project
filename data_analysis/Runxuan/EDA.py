import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

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

def politics_income(df, years, condition=None):
    start_yr = years[0]
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

def business5_age(df, years):
    good_yng = np.zeros(len(years))
    good_mid = np.zeros(len(years))
    good_old = np.zeros(len(years))
    start_yr = years[0]
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

def EDA():
    """EDA analysis code

    Returns:
        figure_and_explanation_list: This list contains the figure and the explanation
        [(figure, explanation), (figure, explanation), ...]
        figure should be a plotly figure object, and explanation should be a string
    """
    df = pd.read_csv("data/Runxuan/df_max.csv")
    df = clean_POLAFF(df)
    df = clean_AGE(df)
    
    start_yr = 1978
    end_yr   = 2022
    years = np.array(np.arange(start_yr,end_yr+1))
    
    RD       = politics_income(df, years)
    RD_bot10 = politics_income(df, years,'bottom10')
    RD_top10 = politics_income(df, years,'top10')
    plotyrs = years[years>2004]
    aa = RD_bot10[years>2004]
    plotRD_bot10 = aa[aa != 0]
    plotyrs = plotyrs[aa != 0]
    plotyrs = plotyrs[plotyrs>2004]
    bb = RD_top10[years>2004]
    plotRD_top10 = bb[aa != 0]
    RDdf = pd.DataFrame({"years":plotyrs,"top10":plotRD_top10,"bot10":plotRD_bot10})
    
    good_yng,good_mid,good_old = business5_age(df,years)
    bizagedf = pd.DataFrame({'years':years,'young':good_yng,'middle aged':good_mid,'senior':good_old})
    
    figure_id_list = []
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=RDdf['years'],y=RDdf['top10'],name="Top 10%"))
    fig1.add_trace(go.Scatter(x=RDdf['years'],y=RDdf['bot10'],name="Bottom 10%"))
    fig1.update_layout(
    title="Level of Partisan for High/Low Income Groups",
    xaxis_title="Year",
    yaxis_title="Fraction of the Population with Partisan Tendency",
    legend_title="Personal Income Percentile", 
    font=dict(family="Times New Roman",size=16,color="Black"))
    fig1.update_xaxes(tickvals = np.arange(RDdf['years'].min(),RDdf['years'].max()+1))
    id1 = "Level of Partisan for High/Low Income Groups"
    bef1 = '''Question: What does the average level of partisan change over time, 
    and do people with high personal income and low personal income exhibit different trends?
    \n We attempt to investigate the level of partisan in a group by using the survey result for the following question:\" 
    Generally speaking, do you usually think of yourself as a Republican, a Democrat, an Independent, or what? \"
    Possible answers include Republican, Democrat, Independent, Don't Know, and N/A. 
    \n We choose to analyze two groups of individuals separately: those who has the top 10% income (high income group) and 
    those who with the bottom 10% income (low income group). We model the level of partisan in a year for each group as 
    the ratio of the number of individuals who answered Republican or Democrat to the size of their respective group in
    that year, plotted as the y axis in the figure below.
    '''
    aft1 = '''Since the survey have mostly empty/too few data for years before 2004, the plot is plotting the partisan level
    from 2004 to 2022. From the data shown above, for both income groups, the partisan tendencies have no drastic flutuating
    since 2004, yet both have a slight overall decreasing trend. There is, however, a difference between the two groups: 
    it is evident that individuals with the highest personal income have a clearer preference for either the Republican or 
    the Democratic party than the individuals with the lowest personal incomes. Further, the difference in partisan level 
    between the two income groups has an increasing trend in recent years, caused mainly by a significant decrease in 
    partisan level among the low-income individuals since 2016.
    '''
    figure_id_list.append((fig1,id1,bef1,aft1))
    
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=bizagedf['years'],y=bizagedf['young'],name="Age Percentile 33% or Lower"))
    fig2.add_trace(go.Scatter(x=bizagedf['years'],y=bizagedf['middle aged'],name="Age Percentile 33% to 67%"))
    fig2.add_trace(go.Scatter(x=bizagedf['years'],y=bizagedf['senior'],name="Age Percentile 67% or higher"))
    fig2.update_layout(
    title="Economic Optimism in 5 Years for Different Age Groups",
    xaxis_title="Year",
    yaxis_title="Fraction of the Population with Economic Optimism",
    legend_title="Age Groups",
    font=dict(family="Times New Roman",size=16,color="Black"))
    fig2.update_xaxes(tickangle=45,tickvals = np.arange(bizagedf['years'].min(),bizagedf['years'].max()+1))
    id2 = "Economic Optimism in 5 Years for Different Age Groups"
    bef2 = ''' \n \n \nQuestion: On average, how optimistic an invdividual is about the economy in the next five years, how this 
    confidence level has changed over the years, and how is this expection for economy differ at different age?
    \n We attempt to investigate the expection of the economy in the contry as whole using the survey result for the question:
    \"Looking ahead, which would you say is more likely -- that in the country as a whole we'll have continuous good times 
    during the next 5 years or so, or that we will have periods of widespread unemployment or depression, or what?\"
    Possible answers include Good times, Good with qualifications, Pro-con, Bad with qualifications, Bad times, Don't Know,
    and N/A (ordered by decreasing level of optimism). We model the level of confidence of a populatoin group on the economy
    by the proportion of the individuals who answered \"Good times\" or \"Good with qualifications\", plotted as the y axis 
    in the figure below. To get a comparable data for people with different ages, we separate each year's indivduals that 
    took the survey into three age groups with roughly the same population (i.e., define the groups via the 33% and 67% 
    percentile in age.)
    '''
    aft2 = '''From the figure above, we conclude that overall, individuals expecetion for the economy do change significantly 
    with time, and all three age groups follow similar time developments. Ignoring small scale fluctuations, there are three
    major peaks in economic expectation from 1978 to 2022, centered approximately at 1984, 2000, and 2015. We further claim 
    that, overall, young people are most likely to have a positive expection for the economy in the next five years, and
    senior people are usually the most pessimistic among the three age groups. However, this claim starts to break down after
    2016, where nearly in the first time since 1983, young people become more pessimistic about the economy than senior
    people, and has been so for recent years ever since 2016.
    '''
    figure_id_list.append((fig2,id2,bef2,aft2))

    return figure_id_list
