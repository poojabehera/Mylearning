# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 21:08:05 2020

@author: Pooja.Behera
"""
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

traindata= pd.read_csv("C:\\Users\\Pooja.Behera\\Downloads\\titanic_train (1).csv")
traindata.head()
traindata.tail()
traindata.columns
len(traindata)
#internal data structure
traindata.info()
# finding summary of data
traindata.describe()
traindata['Name'].isnull()
traindata['Age'].isnull()
traindata['Age'].isna()

#isnull returns individual column true/false value
traindata['Cabin'].isnull()
traindata['Cabin'].isna()

#this will replace all NAN values with the mean value of teh non null values
mean_value= traindata['Age'].mean()
mean_value
traindata['Age']= traindata['Age'].fillna(mean_value)
median_value= traindata['Age'].median()
median_value

sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis') 
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='coolwarm')
df = train.dropna()
df.info
