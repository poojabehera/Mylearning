# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 09:55:06 2020

@author: pooja.behera
"""
import pandas as pd
import numpy as np

loan= pd.read_csv("C:\\Users\\pooja.behera\\Desktop\\Data_science\\Python datasets\\bank_loan.csv")
len(loan)
loan.columns
loan.columns.transpose()
loan.job.unique()
# no. of employees got loan
len(loan[loan.loan=='yes'])
#no. of employees got loan but unemployed
len(loan[loan.loan=='yes'][loan.job== 'unemployed'])
#1

# to know what % of people have loanm but still unemployed
len(loan[loan.loan=='yes'][loan.job== 'unemployed'])/len(loan)*100
#0.2

len(loan[loan.loan=='yes'][loan.job== 'student'])
len(loan[loan.balance <0 ])
len(loan[loan.balance<0][loan.loan== 'yes'])
len(loan[loan.balance<0][loan.job== 'unemployed'])
len(loan[loan.marital=='married'][loan.loan== 'yes']['education']).value_counts()
