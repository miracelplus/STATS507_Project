import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


data1 = pd.read_csv("ICE_MARRY_INCOME_EDU.csv", engine='python',on_bad_lines='skip')
#data1.columns =['CASEID','ICE', 'GOVT','INCOME','AGE','SEX' ,'MARRY', 'EDUC']
data1['INCOME'] = pd.to_numeric(data1['INCOME'], errors='coerce')
data1['INCOME2']=data1.loc[:,['INCOME']].round(-4)
data1['INCOME2']=data1.loc[:,['INCOME2']].clip(upper=100000.0)
print(data1.iloc[[4]])
#print(data1.dtypes)
#,col_order=['0.0','10000.0','20000.0','30000.0','40000.0','50000.0','60000.0','70000.0','80000','90000.0','100000.0']
grid = sns.FacetGrid(data1[['MARRY', 'INCOME2']],col='INCOME2',col_wrap=4,col_order=[0.0,10000.0,20000.0,30000.0,40000.0,50000.0,60000.0,70000.0,80000.0,90000.0,100000.0])
_=grid.map_dataframe(sns.histplot,x='MARRY',stat='percent',binwidth=0.5)

#In figure 1, we would like to discuss the relationship between 'Income' and 'Married Status'. 
#Therefore, we utilized seaborn function to separate data into different income categories and applied Histogram method to show the distribution of different married status 

plt.figure(1)

grid = sns.FacetGrid(data1[['INCOME2', 'EDUC']],col='INCOME2',col_wrap=4,col_order=[0.0,10000.0,20000.0,30000.0,40000.0,50000.0,60000.0,70000.0,80000.0,90000.0,100000.0])
_=grid.map_dataframe(sns.histplot,x='EDUC',stat='percent',binwidth=0.5)

#In figure 2, we would like to discuss the relationship between 'Income' and 'Education'. 
#Therefore, we utilized seaborn function to separate data into different income categories and applied Histogram method to show the distribution of different Education level. 

plt.figure(2)

grid = sns.FacetGrid(data1[['INCOME2', 'SEX']],col='INCOME2',col_wrap=4,col_order=[0.0,10000.0,20000.0,30000.0,40000.0,50000.0,60000.0,70000.0,80000.0,90000.0,100000.0])
_=grid.map_dataframe(sns.histplot,x='SEX',stat='percent',binwidth=0.5)
#for axes in grid.axes.flat:
#    _ = axes.set_xticklabels(axes.get_xticklabels(), rotation=90)

#In figure 3, we would like to discuss the relationship between 'Income' and 'Sex'. 
#Therefore, we utilized seaborn function to separate data into different income categories and applied Histogram method to show the distribution of different gender. 

plt.figure(3)

'''
plt.figure(4)
data1[['INCOME2']].value_counts().loc[[0.0,10000.0,20000.0,30000.0,40000.0,50000.0,60000.0,70000.0,80000.0,90000.0,100000.0]].plot.bar()
#plt.hist(data1[['INCOME2']],bins=[10000,20000])'''



plt.show()
