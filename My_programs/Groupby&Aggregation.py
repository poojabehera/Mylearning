# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:21:59 2020

@author: pooja.behera
"""
import pandas as pd
import numpy as np

#provide input to the Dataframe
data= {"Company":['FB', 'GOOGLE','MICROSOFT','AMAZON','NETFLIX'],
 "Employee":['Richard','Richard','Alex','Sundar','Murthy'],
            "Sale":[550, 120,350,150,450]}

df =pd.DataFrame(data)
print(df)
#df.transpose()
ByComp=df.groupby('Company')
ByComp.mean()
# resulting NAN values***?????????
df.groupby('Company').std()
ByComp=df.groupby('Employee')
ByComp.mean()
ByComp.sum()

ByComp.sum().loc['FB']
ByComp.sum().loc['AMAZON']

df.groupby('Company').max()
df.groupby('Sale').min()
#wil group based on categories not all together in the column
df.groupby('Company').min()
df.groupby('Company').describe()
df.groupby('Company').describe().transpose()
df.groupby('Company').describe().transpose()['FB']


#****************************GROUPBY--OPERATION-2***********************************************

Sales= pd.DataFrame({"Weekday":['Sun','Mon', 'Sun','Mon'],
      "City":['Austin','Dallas','Austin','Dallas'],
      "Bread":[139, 237,350,450],
      "Butter":[20, 50, 65, 98]
      })

Sales
#GroupBy and Count
Sales.groupby('Weekday')['Butter'].sum().count()
#GroupBY
Sales.groupby('City')['Butter'].sum()
Sales.groupby('City')['Bread'].sum()
Sales.groupby('City')['Bread'].min()
Sales.groupby('City')['Butter'].max()
Sales.groupby('City')['Bread'].mean()
Sales.groupby('City')['Bread'].describe().transpose()

#Aggregation
Sales.groupby('City')['Bread'].agg(['max'],['min'])
Sales.groupby('Weekday')['City'].agg(['max'],['min'])
Sales.groupby('Weekday')[['Bread','Butter']].sum()
Sales.groupby('Weekday')[['Bread','Butter']].max()
Sales.groupby('City')[['Bread','Butter']].max()
Sales.groupby('Weekday')[['Bread','Butter']].min()
Sales.groupby('Weekday')[['Bread','Butter']].agg(['max'],['min'])
