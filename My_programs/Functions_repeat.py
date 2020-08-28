# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:40:31 2020
@author: pooja.behera
"""
#Function, Loops, conditions are used while working with cleaning the missing data
#In Python always define the fucntion by def Function name(arg)

def square(num):
    return num  **2
output= square(5)
print(output)

def my_function(country="Norway"):
    print("I am a resident of "  + country)
my_function()
my_function("America")
my_function("Bulgaria")
my_function("California")
my_function("Delhi")



def my_function(x):
    return 5 * x
print(my_function(3))
my_function(2)
my_function(5)
my_function(10)


#**********************Methods*******************************
#June 3 2020
#Methods are functions which belongs to perticular object
#Based on object data type different methods are aviliable

#List
a_list=[10,20,30,40,10,30,50,60,70]
a_list.count(10)


#add 100 to list
a_list.append(100)
a_list
#insert
a_list.insert(2, 200)

a_list.remove(10)
a_list

a_list.sort()

a_list.reverse()

#Regular expression using re
#example match phone number
import re
pattern= re.compile('\d{3}--\d{3}--d{4}')
rs= pattern.match('123-535-1264')
#or
rs= pattern.match('111-222-4444')
bool(rs)

#Example convert $
pattern= re.compile('\$/d*-\d{2}')
rs= pattern.match('$100.35')
bool(rs)