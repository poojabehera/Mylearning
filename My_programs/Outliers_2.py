# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:31:21 2020

@author: pooja.behera
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston
#boston is an inbuilt dataset present in SKlearn
#like boston any other data can be loaded using load function
#boston contain 4 distributions
# data & target are mapped indiidually
boston= load_boston()
x= boston.data
x
y= boston.target
y
columns= boston.feature_names
columns
boston
##creating the dataframe
boston_df= pd.DataFrame(boston.data)
boston_df.columns= columns
boston_df.head()
###Box plot
#Now converting the data frame in proper dataforamt
#DIS is the column name
sns.boxplot(x= boston_df['DIS'])
## Zscore function defined
from scipy import stats
#check why we define numpy here
import numpy as np
##Zscore remove the oultliers
z= np.abs(stats.zscore(boston_df))
z
# formula for z score= (observation- Mean)/ Standard deviation
# Z table always have the threshold value between -3 to 3 
## print(np.where(z>3))

print(z[29][8])

## Datapoint where 
#Ture indicates presence of outliers
boston_df= boston_df[(z<3).all(axis= 1)]
boston_df.shape
#practise the same with Bikeshare, titanic

