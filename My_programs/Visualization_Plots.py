# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 22:52:28 2020

@author: pooja.behera
"""
import seaborn as sns
tips= sns.load_dataset('tips')
tips
tips.head()
### Dist plot --distribution --shows only one variable 

##KDE= kernel density estimation
sns.distplot(tips['total_bill'], bins=40)
sns.distplot(tips['total_bill'], kde=False, bins=30)
# clubbing to 2 distribution values

sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex' )
sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg' )
sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde' )    

##Pairplot
sns.jointplot(tips, hue='sex' )### hue= categorical selewction (ex:)

sns.rugplot(tips['totalplot'])
##categorical plot
##bar plot---aggregate of categorical data

sns.barplot(x= 'sex', y='total_bill', data=tips)

##count plot- count number occurances



