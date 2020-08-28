# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 22:52:28 2020
@author: pooja.behera
"""
import seaborn as sns
tips= sns.load_dataset('tips')
tips
tips.head()
#Seaborn is built on matplot library
#Seaborn use libraries of Matplolib 
### Dist plot --distributio/Histogram --shows only one variable 
##KDE= kernel density estimation---the curve, if False that it wont appear
sns.distplot(tips['total_bill'], bins=10)
sns.distplot(tips['total_bill'], kde=True, bins=30)
# clubbing to 2 distribution values
sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex' )
sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg' )
sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde' ) 
sns.jointplot(x='total_bill', y='tip', data=tips)   #---scatter plot

## Pairplot
### hue= categorical selection (ex:)---------3*3 = 6 graphs. a is on X axis, b is on Y axis
sns.pairplot(tips, hue='sex')
##gives bar code kind graph. everything is either on X or Y plot (kind of bar code)
sns.rugplot(tips['total_bill'])

##categorical plot
##bar plot---aggregate of categorical data
sns.barplot(x= 'sex', y='total_bill', data=tips)

###count plot ---count no of ocurance
sns.countplot(x= 'sex', data= tips)
sns.boxplot(x='sex', y='total_bill', data=tips)

##Box---shows difference between variables
#take x= categorical, Y = bumeric, in case both categorical choose Histogram, 
sns.boxplot(x='smoker', y='total_bill', data=tips)  #---wrong
sns.boxplot(x='sex', y='total_bill', data=tips)  #---wrong
sns.boxplot(x= 'day', y='total_bill', data= tips)
sns.boxplot(x='day', y='total_bill', data= tips, hue='smoker')

##strp plot ---draw scatter plot where one variable is categorizes 
sns.stripplot(x='day', y='total_bill', data= tips)
sns.stripplot(x='day', y='total_bill', data= tips, jitter= True)

### Factorplot------general


