# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 08:49:16 2020
@author: pooja.behera
"""

import pandas as pd
stats = pd.read_csv("C:\\Users\\pooja.behera\\Desktop\\Data_science\\Python datasets\\Demographic_Data.csv")

import os
print(os.getcwd)
#chnge work in directory
#file destonation
os.chdir("C:\\Users\\pooja.behera\\.spyder-py3\\Programs")
# No of rows
len(stats)
stats.column 
len(stats.columns)
stats.head()
stats.tail()
stats.info()
#gets stats of the column (it is like summary function in R)
stats.describe()
# function from python gives mean median of every data 
stats.describe().transpose()
# column data changes to Rows and vice versa
#renaming columns
stats.columns= ['countryName','countryCode' ,'Birthrate', 'InternetUsers','IncomeGroup']
stats.head()
# subsetting dataframes - rows, columns, combine teh both





