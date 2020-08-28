# -*- coding: utf-8 -*-
"""
Created on Sat May 16 09:31:05 2020

@author: pooja.behera
"""
import pandas as pd
import numpy as np
import matplotlib as plt

loan_data= pd.read_csv("C:\\Users\\Pooja.Behera\\Desktop\\Pooja_behera\\Class recordings\\R\\R_Datafiles\\bankloan.csv")
print(loan_data)

#******************* Explortory data analysis*************************
#no.of rows
len(loan_data)
loan_data.columns
loan_data.head()
loan_data.tail()

#to get intenal data structure
loan_data.info()

#to get summary of the data
loan_data.describe()
loan_data.mean()
loan_data.median()

#to get all jobs and their count
loan_data.job
loan_data.education
#to get total no. of job type
loan_data.job.unique()
loan_data.education.unique()
loan_data.marital.unique()

#In Python, len() is used to count occurnaces, 
#IN R, we use aggregate to count total no. of occurances of variables
#No. of employees who have got loan
len(loan_data[loan_data.loan=='yes'])
#people who are unemployed but still have loan
len(loan_data[loan_data.loan=='yes'][loan_data.job=='unemployed'])

#people with loan & job count.  In R instead value_count, we use aggregate
(loan_data[loan_data.loan=='yes']['job']).value_counts()

#people whose education are unknown and have loan  
len(loan_data[loan_data.loan=='yes'][loan_data.education=='unknown'])

# percentage of uneducated people getting loan
len(loan_data[loan_data.loan=='yes'][loan_data.education=='unknown'])/len(loan_data)*100
#percentage of unemployed getting loan
len(loan_data[loan_data.loan=='yes'][loan_data.job=='unemployed'])/len(loan_data)*100 

#Student got a loan whose age is 22 and Single
len(loan_data[loan_data.loan=='yes'][loan_data.job=='student'])

# records with negative balance. 366 Records found with Negative Balance
len(loan_data[loan_data.balance<0])
#people with 0 balance
len(loan_data[loan_data.balance<=0])

#103Persons got loan even if they are maintaining Negative balance
len(loan_data[loan_data.balance<0][loan_data.loan=='yes'])

# people having negative balance, loan qualified, have job
(loan_data[loan_data.balance<0][loan_data.loan=='yes']['job']).value_counts()    

# people married, loan qualified, educated
(loan_data[loan_data.loan=='yes'][loan_data.marital=='married']['education']).value_counts()

#married people with loan....# 453 records
len(loan_data[loan_data.marital=='married'][loan_data.loan=='yes'])

#people married with no lon and have job
(loan_data[loan_data.loan=='no'][loan_data.marital=='married']['job']).value_counts()

#(loan_data[loan_data.marital=='married'][loan_data.loan=='no']['job']).value_counts()

# people with non-marital status but have loan...238
len(loan_data[loan_data.marital!='married'][loan_data.loan=='yes'])
#3830 records
len(loan_data[loan_data.marital!='maried'][loan_data.loan!='yes'])

#people who are not married, not having loan , having job
(loan_data[loan_data.marital!='maried'][loan_data.loan!='yes']['job']).value_counts()

# 71 people whose education is secondary, married status, blue-collar job, have loan
len(loan_data[loan_data.education=='secondary'][loan_data.marital=='married'][loan_data.job=='blue-collar'][loan_data.loan=='yes'])

# 355 people with married status, have >0 balance , have loan

len(loan_data[loan_data.marital=='married'][loan_data.balance>0][loan_data.loan=='yes'])

#people with no loan, married, educated
(loan_data[loan_data.loan!='yes'][loan_data.marital=='married']['education']).value_counts()

#people with housing loan  ##2559

len(loan_data[loan_data.housing=='yes'])

#people with no housing loan      ##1962
len(loan_data[loan_data.housing!='yes'])

#records with housing, loan, job, age,education 
len(loan_data[loan_data.housing=='yes'][loan_data.loan=='yes'][['job','age','education']])

#Jobs got loan
(loan_data[loan_data.loan=='yes']['job']).value_counts() 
          
#jobs dont got loan
(loan_data[loan_data.loan!='yes']['job']).value_counts()

 #education got loan
(loan_data[loan_data.loan=='yes']['education']).value_counts()

#education dont got loan
(loan_data[loan_data.loan!='yes']['education']).value_counts()   







