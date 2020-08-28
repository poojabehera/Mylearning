# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 09:31:34 2020

@author: Pooja.Behera
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as pnp
import seaborn as sns
USAhousing= pd.read_csv("C:\\Users\\Pooja.Behera\\Desktop\\Pooja_behera\\Class recordings\\Python\\USA_Housing.csv")
USAhousing.describe()
USAhousing.head()
USAhousing.columns
#pd.isany(USAhousing)
pd.isnull(USAhousing)
#lets create some plots to plots to checkout the data
sns.pairplot(USAhousing)
sns.distplot(USAhousing['Price'])
y= sns.USAhousing['Price']
sns.heatmap(USAhousing.corr(),annot=True)
USAhousing.corr()
#Training a Linear Regression Model
#Before Train out the model we need to spilt the data
#Data into X array conatins features to Train and Y contains the Target variable
#No. of independent variables are more, so multiniear regression is choosen

X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
y = USAhousing['Price']

##########Train Test Split
from sklearn.cross_validation import train_test_split
#from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

######Creating and Training the Model
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train,y_train)

### Model Evaluation
#valuating the model by checking it's coefficients and 
##how we can interpret them.
# print the intercept
lm.coef_
X_train.columns
coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
coeff_df

#### Predictions from our Model
  
predictions = lm.predict(X_test)
predictions[9]
y_test
plt.scatter(y_test,predictions)

print("R^2:{}".format(lm.score(X_test, y_test))) # Accuracy 

from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))




