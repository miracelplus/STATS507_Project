import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
from plotly import graph_objects as go
from plotly.subplots import make_subplots
#Before the analysis, I am wondering whether there's a inequlaity between gender and income. Surprisely, women's income is higher that men's.
#Therefore, the second analysis is aim to explain the result. No matter in which education level, the population of women is bigger than men.

def EDA():
    data1 = pd.read_csv("data/Wei/ICE_MARRY_INCOME_EDU.csv", engine='python',on_bad_lines='skip')
    #data1.columns =['CASEID','ICE', 'GOVT','INCOME','AGE','SEX' ,'MARRY', 'EDUC']
    data1['INCOME'] = pd.to_numeric(data1['INCOME'], errors='coerce')

    data1['INCOME2']=data1.loc[:,['INCOME']].round(-4)
    data1['INCOME2']=data1.loc[:,['INCOME2']].clip(upper=100000.0)
    #print(data1.head())
    fig1 = make_subplots(rows=2, cols=1,  subplot_titles=("Male", "Female"))

    fig1.append_trace(go.Histogram(x=data1['INCOME2'].mask(data1['SEX']=='1'),histnorm='percent'), row=1, col=1)
    fig1.append_trace(go.Histogram(x=data1['INCOME2'].mask(data1['SEX']=='2'),histnorm='percent'), row=2, col=1)
    fig1.update_xaxes(title_text="income", row=1, col=1)
    fig1.update_xaxes(title_text="income", row=2, col=1)
    fig1.update_yaxes(title_text="percentage", row=1, col=1)
    fig1.update_yaxes(title_text="percentage", row=2, col=1)
    #fig1.show()

    fig2 = make_subplots(rows=2, cols=3,subplot_titles=("Grade 0-8 no hs diploma", "Grade 9-12 no hs diploma", "Grade 0-12 w/ hs diploma", "Grade 13-17 no col degree", "Grade 13-16 w/ col degree", "Grade 17 W/ col degree"))


    fig2.append_trace(go.Histogram(x=data1['SEX'].mask(data1["EDUC"]=='1'),histnorm='percent'), row=1, col=1)
    fig2.append_trace(go.Histogram(x=data1['SEX'].mask(data1["EDUC"]=='2'),histnorm='percent'), row=1, col=2)
    fig2.append_trace(go.Histogram(x=data1['SEX'].mask(data1["EDUC"]=='3'),histnorm='percent'), row=1, col=3)
    fig2.append_trace(go.Histogram(x=data1['SEX'].mask(data1["EDUC"]=='4'),histnorm='percent'), row=2, col=1)
    fig2.append_trace(go.Histogram(x=data1['SEX'].mask(data1["EDUC"]=='5'),histnorm='percent'), row=2, col=2)
    fig2.append_trace(go.Histogram(x=data1['SEX'].mask(data1["EDUC"]=='6'),histnorm='percent'), row=2, col=3)
    fig2.update_xaxes(title_text="SEX", row=1, col=1)
    fig2.update_xaxes(title_text="SEX", row=2, col=1)
    fig2.update_xaxes(title_text="SEX", row=1, col=2)
    fig2.update_xaxes(title_text="SEX", row=2, col=2)
    fig2.update_xaxes(title_text="SEX", row=1, col=3)
    fig2.update_xaxes(title_text="SEX", row=2, col=3)
    fig2.update_yaxes(title_text="percentage", row=1, col=1)
    fig2.update_yaxes(title_text="percentage", row=2, col=1)
    fig2.update_yaxes(title_text="percentage", row=1, col=2)
    fig2.update_yaxes(title_text="percentage", row=2, col=2)
    fig2.update_yaxes(title_text="percentage", row=1, col=3)
    fig2.update_yaxes(title_text="percentage", row=2, col=3)
    
    return [(fig1,'Relationship between Gender and Income'),(fig2,'Relationship between Gender and EDU')]
   
