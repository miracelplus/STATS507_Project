import plotly.express as px
import pandas as pd


def EDA():
    """EDA analysis code

    Returns:
        figure_and_explanation_list: This list contains the figure and the explanation
        [(figure, explanation), (figure, explanation), ...]
        figure should be a plotly figure object, and explanation should be a string
    """
    figure_id_list = []
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
    df1 = pd.read_csv("data/Harshang/Business_Conditions_Datafile.csv", sep=",", header=0)

    # Replace Survey Values with Dictionary Values
    df1.replace({"BAGO" : bago_dict}, inplace=True)
    df1.replace({"BEXP" : bexp_dict}, inplace=True)
    df1.replace({"BUS12" : bus12_dict}, inplace=True)
    df1.replace({"BUS5" : bus5_dict}, inplace=True)
    df1.replace({"UNEMP" : unemp_dict}, inplace=True)
    df1.replace({"GOVT" : govt_dict}, inplace=True)
    df1.replace({"RATEX" : ratex_dict}, inplace=True)

    #print(df1)

    # Plot BAGO Values: Would you say that at the present time business conditions are better or worse 
    #                   than they were a year ago?
    #
    fig1 = px.bar(df1, x=df1['BAGO'].value_counts().index, y=df1['BAGO'].value_counts(normalize=True).mul(100).round(1).values,
                color=df1['BAGO'].value_counts().index.astype(str), labels=dict(x='BAGO', y='Frequency'),
                title="ECONOMY BETTER/WORSE YEAR AGO")
    fig1.update_layout(title_x=0.5)
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
    fig2.update_layout(title_x=0.5)


    # Plot BUS12 Values: Now turning to business conditions in the
    #               country as a whole--do you think that during the next 12
    #               months we'll have good times financially, or bad times, or what?
    fig3 = px.bar(df1, x=df1['BUS12'].value_counts().index, y=df1['BUS12'].value_counts(normalize=True).mul(100).round(1).values,
                color=df1['BUS12'].value_counts().index.astype(str), labels=dict(x='BUS12', y='Frequency'),
                title="ECONOMY GOOD/BAD NEXT YEAR")
    fig3.update_xaxes(type='category')
    fig3.update_xaxes(categoryorder='category ascending')
    fig3.update_layout(title_x=0.5)


    # Plot BUS5 Values: Looking ahead, which would you say is more likely -- that
    #           in the country as a whole we'll have continuous good times
    #           during the next 5 years or so, or that we will have periods
    #           of widespread unemployment or depression, or what?
    fig4 = px.bar(df1, x=df1['BUS5'].value_counts().index, y=df1['BUS5'].value_counts(normalize=True).mul(100).round(1).values,
                color=df1['BUS5'].value_counts().index.astype(str), labels=dict(x='BUS5', y='Frequency'),
                title="ECONOMY GOOD/BAD NEXT 5 YEARS")
    fig4.update_xaxes(type='category')
    fig4.update_xaxes(categoryorder='category ascending')
    fig4.update_layout(title_x=0.5)


    # Plot UNEMP Values: How about people out of work during the coming 12 months --
    #            do you think that there will be more unemployment than now,
    #            about the same, or less?
    fig5 = px.bar(df1, x=df1['UNEMP'].value_counts().index, y=df1['UNEMP'].value_counts(normalize=True).mul(100).round(1).values,
                color=df1['UNEMP'].value_counts().index.astype(str), labels=dict(x='UNEMP', y='Frequency'),
                title="UNEMPLOYMENT MORE/LESS NEXT YEAR")
    fig5.update_xaxes(type='category')
    fig5.update_xaxes(categoryorder='category ascending')
    fig5.update_layout(title_x=0.5)


    # Plot GOVT Values: As to the economic policy of the government -- I mean steps
    #           taken to fight inflation or unemployment -- would you say the
    #           government is doing a good job, only fair, or a poor job?
    fig6 = px.bar(df1, x=df1['GOVT'].value_counts().index, y=df1['GOVT'].value_counts(normalize=True).mul(100).round(1).values,
                color=df1['GOVT'].value_counts().index.astype(str), labels=dict(x='GOVT', y='Frequency'),
                title="GOVERNMENT ECONOMIC POLICY")
    fig6.update_xaxes(type='category')
    fig6.update_xaxes(categoryorder='category ascending')
    fig6.update_layout(title_x=0.5)

    # Plot RATEX Values: No one can say for sure, but what do you think will happen to
    #            interest rates for borrowing money during the next 12
    #            months--will they go up, stay the same, or go down?
    fig7 = px.bar(df1, x=df1['RATEX'].value_counts().index, y=df1['RATEX'].value_counts(normalize=True).mul(100).round(1).values,
                color=df1['RATEX'].value_counts().index.astype(str), labels=dict(x='RATEX', y='Frequency'),
                title="INTEREST RATES UP/DOWN NEXT YEAR")
    fig7.update_xaxes(type='category')
    fig7.update_xaxes(categoryorder='category ascending')
    fig7.update_layout(title_x=0.5)

    return [(fig1, 'BAGO-graph'), (fig2, 'BEXP-graph'), (fig3, 'BUS12-graph'), (fig4, 'BUS5-graph'), (fig5, 'UNEMP-graph'), (fig6, 'GOVT-graph'), (fig7, 'RATEX-graph')]
