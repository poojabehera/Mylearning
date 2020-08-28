# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:02:41 2020

@author: Pooja.Behera
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_excel("C:\\Users\\Pooja.Behera\\.spyder-py3\\Programs\\houseprice.py")

#forming linear model
#plotting by scatter plot
plt.xlabel("Area")
plt.ylabel("Prices")
#plt.scatter(X, Y)  showsdatapoint
plt.scatter(df.Area, df.Prices)
plt.scatter(df.Area, df.Prices, color="red")
#optional
plt.scatter(df.Area, df.Prices, color="red", marker='+')
#creating instance in Python 

new_df= df.drop('Prices', axis='columns')
new_df
#Model training & creation...fit() is used because linear regression model takes 2-D modelpresentation

from sklearn import linear_model
model= linear_model.LinearRegression()
model.fit(new_df, df.Prices)

#keep it 2-D predection
model.predict([[3300]])
#slope
model.coef_

#intercept
model.intercept_