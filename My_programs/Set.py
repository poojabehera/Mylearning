# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:23:51 2020
@author: pooja.behera
"""
#Set is a collection of Distcint objects
#Do not hold Duplicate values/ Items and is Imutable in nature
age= {23,14, 45, 32,50,14}
print(age)
# stores items in no perticular order
# Based on Hash Table Data structure

Set_var={"Avanegers","Iron man","Frozen","Lion king"}
print(Set_var)
(type(Set_var))

#Add function
Set_var.add("jungle book")
print(Set_var)

# Doenst allow Duplicacy
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

#Return a set that contains the items that only exist in set x, and not in set y:
Set_difference= x.difference(y)
print(Set_difference)

#Discard function--removes matching object from an existing set
Set_var.discard("Frozen")
print(Set_var)

#clear removes all elemets from the existing set
Set_var.clear()
print(Set_var)

#Set operations
# UNION------Return all variables belongs to both sets
Set_var1= {"Bahubali", "Judwa", "Mardani","Avanegers","Frozen" }
Set_Union= Set_var.union(Set_var1)
print(Set_Union)

#Intersection-----Return elements common to SetA and Set B
Set_intersetion= Set_var.intersection(Set_var1)
print(Set_intersetion)

#Difference---------Resturns elements belonging to A but not B
Set_diference= Set_var.difference(Set_var1)
print(Set_diference)

#symmetric_difference----returns elements not common to both the elements 
Set_symm_difference= Set_var.symmetric_difference(Set_var1)
print(Set_symm_difference)

