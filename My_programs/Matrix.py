# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 01:12:35 2020
@author: pooja.behera
"""
#Matrix is a 2-Dimensional array consisting Rows and cols 
#Syntax---numpy.matrix(data)

import pandas as pd
import numpy as np
import seaborn as sns

x= np.matrix("13,1,2,3;14,5,6,7;15,9,10,11; 16,8,9,7")
print(x)
#to print 1st row
x[0]
#print 1st col
x[:,1]
#print last col
x[:,3]
# to print till 2nd row it takes n-1. i., 2-1=1= 0th & 1st row 
x[0:2]
# to print from first 2 rows, print 3rd column
x[0:2,2]
# to print from first 2 rows, print only till 3rd column
x[0:2, 0:3]
#print specific elements
x[1:3,2:3 ]
x[1:4,1:3 ]

#Shape---return no. of Rows and Columns of the Matrix
#Shape[0]---return no. of rows
#Shape[1]---return no. cols
#size---no. of elements
print(x.shape)
print(x.shape[0])
print(x.shape[1])
print(x.size)

#Modifying Matrix using insert()
#insert--adds value at a given position & axis in a Matrix
#Syntax: np.matrix(matrix, obj,values,axis)
#matrix--input matrix
#obj--index position
#values--matrix of values to be inserted
#axis-axis along which the values needs to be inserted

col_new=np.matrix("13,14,15,20")
a= np.insert(x,1,col_new,axis=1)
print(a)

row_new=np.matrix("13,14,15")
a= np.insert(x,1,row_new,axis=0)
print(a)

#Modify the Matrix using Index no
#specify the index position
#14 value should be updated to -3
a[1,1]= -3
print(a)
#Extract elements from 2nd & 4th row of a Matrix
a[1,:]
a[3,:]
#Extract elements from 1st & 3rd column of a Matrix
a[:,0]
a[:,2]
#Extractspecific elements of a Matrix
a[0,1]
a[1,1]
#Matrix Addition------will add two Matrices
A= np.matrix(np.arange(1,5)).reshape(2,2)
print(A)
B=np.matrix(np.arange(6,10)).reshape(2,2)
print(B)
new_mat= np.add(A,B)
print(new_mat)
#Matrix Subtraction------performs element wise  
new_mat= np.subtract(A,B)
new_mat= np.subtract(B,A)
print(new_mat)
#Matrix Multiplication------performs elements wise multipliaction of two Matrices(Both Matrix dimension must be same)
new_mat=np.multiply(A,B)
print(new_mat)

#Using Dot vector/ matmul------will return Dot product of the Matrix
new_map=np.dot(A,B)
print(new_map)
new_mat= np.matmul(A,B)
print(new_mat)

#Matric division
new_mat= np.divide(B,A)
print(new_mat)
         
# import demographic data
dataset= pd.read_csv("C:\\Users\\pooja.behera\\Desktop\\Data_science\\Python datasets\\DemographicData.csv")
print(dataset)
#length of rows
len(dataset)
dataset.columns
#length of columns
len(dataset.columns)
dataset.head()
dataset.tail()
# data structure
dataset.info()

#summary
dataset.describe()
dataset.describe().transpose()
#renaming columns
dataset.columns=['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']
dataset.head()
#get the data from rows
dataset[21:26]
dataset[21:26].transpose()
#reverse the dataframes

#?
dataset[::-1]
#Part2
dataset['InternetUsers']
dataset['IncomeGroup']
dataset['CountryCode']
dataset[['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup', ]]
dataset.Birthrate
#Part 3 combine
dataset[4:8][['CountryName','IncomeGroup']]
dataset[['CountryName', 'CountryCode','InternetUsers']][4:8]
#mapping to other variable
def1= dataset[['CountryName', 'InternetUsers']]
print(def1)
def1[4:8]
#basic operations with dataframe
#mathematical operations
result= dataset.BirthRate*dataset.InternetUsers
result.head()
#adding column
dataset.BirthRate* InternetUsers
dataset.CountryName + dataset.CountryCode
dataset['Mycal']= dataset.CountryName +dataset.CountryCode
dataset['Mycal']= dataset.CountryName + dataset.CountryCode
#dataset['Mycal']= dataset.BirthRate* InternetUsers
dataset.head()
#remove column
ds1= dataset.drop('Mycal', axis= 1)
ds2= dataset.derop(['BirthRate', 'InternetUsers'], axis= 1)
#will result only as True/ False
dataset.InternetUsers<2
#data[data] will return nos. of data satisfying condition
dataset[dataset.InternetUsers<2]
#mapping to variable
filter1=dataset.InternetUsers<20
dataset[filter1]
dataset[dataset.BirthRate>40]
filter2= dataset.BirthRate> 40
filter2
filter & filter2
dataset[filter & filter2]
#Extracting 2 datarecords together
dataset[(dataset.BirthRate> 40) & (dataset.InternetUsers<2)]
#dataset.IncomeGroup == Lowincome

#Visualization
sns.distplot(dataset['BirthRate'],kde=True, bins= 40)
sns.jointplot(x='CountryName', y='BirthRate', data=filter1, kind='hex')
sns.jointplot(x='CountryName', y='BirthRate', data=dataset, kind='reg' )












