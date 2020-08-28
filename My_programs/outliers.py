# -*- coding: utf-8 -*-
"""
Created on Sat May 16 10:33:29 2020

@author: pooja.behera
"""

import pandas as pd
import numpy as np
import matplotlib. pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston
boston= load_boston()
x= boston.data
x
y= boston.target
y
#from data set mapping to variable
columns = boston.feature_names
columns
#create the Data frame
boston_df= pd.DataFrame(boston.data)
#mapping the data to the column
boston_df.columns= columns
boston_df.columns
boston_df.head()
##Box plot
sns.boxplot(boston_df[DIS])
## Z score function defined
from scipi import stats
import numpy as np
z= np.abs(stats.zscore(boston_df))
z
# formula for z score= (observation/ mean )/ standard deviation
# z table alwasys the threashold -3 and 3 
# print (np.where(z>3))
print(z[50][6])
# Data pont where have false that means 
# True indiacte presence of Outliers
boston_df= boston_df[(z<3).all(axis= 1)]
boston_df.shape
##The first array contains the row number and second array respectivecolumn number
Q1= boston_df.quantile(0.25)
Q3= boston_df.quantile(0.75)
IQR= Q3- Q1
print(IQR)

#Pivot table using Python
import seaborn as sns
flights= sns.load_dataset('flights')
flights.head()
flights.pivot_table(index='month', columns= 'year', values='passengers')
fp= flights.pivot_table(index='month', columns= 'year', values='passengers')
sns.heatmap(fp, cmap= 'magma', linecolor= 'white', linewidth= 3, annot= True)
sns.heatmap(fp, cmap= 'magma', linecolor= 'white', linewidth= 3)
#Cluster map- hirarichal clustering
sns.clustermap(fp, cmap= 'coolwarm', standard_scale= 1)



