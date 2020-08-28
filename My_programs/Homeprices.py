# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:02:41 2020

@author: Pooja.Behera
"""
import pandas as pd
import numpy as np
import matplotlib. pyplot as plt 
from sklearn import linear_model

df= pd.read_csv("C:\\Users\\Pooja.Behera\\.spyder-py3\\Programs\\Python_exercise\\Homeprices.csv")
print(len(df))

df.head()
df.describe()
df.columns


