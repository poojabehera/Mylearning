# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:53:16 2020

@author: pooja.behera
"""

#Tuples are ordered collection list of objects
#Immutabe----once created cannot be modified
#enclosed with in ()

employee_details=('EMP011', "Daniel", 35, 50000)
print(employee_details)

#Accessing Tuple componenets
print(employee_details[0])
print(employee_details[3])
#throw error Tuple index out of Range
print(employee_details[7])

#Accessing Tuple range
employee_details=('EMP011', "Daniel", 35, 50000, "Indian","White")
print(employee_details[-3])

#Slicing
#Use to access set of elements from a Tuple by creating a range of index numbers
print(employee_details[2:5])
print(employee_details[0:3])
print(employee_details[:3])
print(employee_details[0:])

#Length of the Tuple
len(employee_details)

#To find min, max of  Tuple its should follow one data type else it will throw error
stud_marks=(100, 99, 80, 50, 70, 30)
min(stud_marks)
max(stud_marks)
#combining two Tuples ---Tuple1+ Tuple2
Fruit_tuple = ("apple", "banana", "cherry", "orange")
Price_tuple= (120, 60, 140, 90)
Tuplecombo= Fruit_tuple + Price_tuple
print(Tuplecombo)
employee_details2= ("B.Tech","Data scientist")
print(employee_details + employee_details2)




