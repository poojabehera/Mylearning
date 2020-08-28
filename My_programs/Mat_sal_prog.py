# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 01:46:19 2020

@author: pooja.behera
"""
import pandas as pd
import numpy as np
import seaborn as sns

sal= pd.read_csv("C:\\Users\\Pooja.Behera\\Desktop\\Pooja_behera\\Class recordings\\R\\R_Datafiles\\Salaries.csv")
sal
len(sal)
len(sal.columns)
sal.head()
sal.tail()
#interal datastructure
sal.info() 
#mean, median, mode, nan values
sal.describe()
sal.describe().transpose()
sal.columns= [['EmployeeName','JobTitle','Agency']]
# get the data from teh rows
sal[10:20]
#print the data in reverse order
sal[::-1]
sal['EmployeeName']
sal['JobTitle']
sal['Agency']
# renaming the columns, here there is 13 observations so skipping the part
# sal[['EmployeeName','Id','JobTitle','Agency']]
#combinig the data
sal[20:30]['EmployeeName']
sal[20:30][['EmployeeName', 'JobTitle','Agency','BasePay']]
#mapping to other variable
def1= sal[['EmployeeName', 'JobTitle','Agency','BasePay']]
def1
print(def1[4:14])
#mathematical operations
sal.BasePay> 1300   ######?
sal.BasePay == 15000 
len(sal[sal.BasePay == 15000])
result= sal.EmployeeName* sal.JobTitle



#Visualization
sns.distplot(sal['Job_title'], kde= True, bins=40)
sns.jointplot(x='Job_title', y='Base_pay', data=sal, kind='reg' )
