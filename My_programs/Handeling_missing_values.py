# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:08:09 2020

@author: pooja.behera
"""
#Isnull checks each and every null data
#Isna checks all the data containing any NAN/null values

import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

df =pd.DataFrame(np.random.rand(3,5), index=['a','b','e','f','h'], columns=['one', 'two','three'])
df =df.reindex(['a','b','c','d','e'])
df
print(df)
#isnull---------return NAN values if exists
#missing value can be restored in 2 ways
#either taking the whole data through visualization or column wise
df['one'].isnull
df['one'].mean()
missingvalue=df['one'].mean()

#df2= df.fillna(999)
df1= df.fillna(missingvalue)
df['one'].sum()
df['two'].isnull()
df['three'].isnull()
#isna & not null will return True if NAN values exisist
df['one'].isna()
df['one'].notnull()      #fill the empty cells with some number
df2=df.fillna(23)
df2
df2['one'].isnull()    #------now No empty cells fills with no.  so missing value
df1= df.dropna()        #remove the empty cells------ll drop the empty cells 
df1
df.dropna(axis=1)            #Deleting row information, axis= 1
df.drop(axis=0)                #Deleting row information, axis= 0

#replace with specific valus
df= pd.DataFrame({'one':[10,20,30,40,50,300], 'two':[1000, 0, 30, 40, 50, 60]})
#np.random.rand(25)
#Df_obj= pd.DataFrame(np.random.rand(36).reshape.seed(6,6))
#Df_obj

# always press shift and copy teh path...it shoul be procedded with \\
train= pd.read_csv("C:\\Users\\pooja.behera\\Desktop\\Data_science\\titanic-train.csv")
train.head()
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis') 
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='coolwarm')
df = train.dropna()
df.info
#this will replace all NAN values with the mean value of teh non null values
mean_value= train['Age'].mean()
mean_value
train['Age']= train['Age'].fillna(mean_value)
median_value= train['Age'].median()
median_value



