# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 00:09:29 2020
z`
@author: pooja.behera
"""
import numpy as np

#Array operations & function
# Array creation using arange and reshape
a= np.array([[1,2],[3,4]])
#Shape()-------Returns Dimensions of Array
a.shape
print(a)
b=np.arange(start=11, stop=15).reshape(2,2)
print(b)

#Add 2 Array
c=np.add(a,b)
print(c)

#Multiply
c=np.multiply(a,b)
print(c)

#Subtract
c=np.subtract(b,a)
print(c)

#Divide--------returns quorient
c=np.divide(b,a)
print(c)

#Remainder----------returns remaider
c=np.remainder(b,a)
print(c)

# Array element extraction
arr= np.array([[2,3,8], [4,5,9], [6,7,10]])
print(arr)
arr[:]
#access 2nd element of 1st row
arr[:,1]
arr[0,1]
arr[1,1]
arr[2,1]
arr[0,3]

# access elements from 2nd and 3rd row of the array
arr[1:3]    #In Python Indexing starts from n- n-1

#extract elements from 1st col
arr[:,0]

#extract elements from 3nd col
arr[:,2]
#extract elemets from 1st row
arr[0,:]
#extract elemets from 2nd row
arr[1,:]
#extract elemets from 3rd row
arr[2,:]

#Array Subset 
#extracting subset of array i.e extracting elemets from two row & two col
a_sub=arr[:2,:2]
print(a_sub)

#update the 1st element of the Sub_set Array
a_sub[0,0]=24
print(a_sub)

#update the 4th element of the Sub_set Array
a_sub[1, 1]=25
print(a_sub)

#Modify the Array using Transpose()
b_trans= np.transpose(b)
print(b)

a_trans= np.transpose(a)
print(a)

arr_trans= np.transpose(arr)
print(arr_trans)

#Modify the Array using append()
# Syntax-------np.append(array, axis)
#axis= 0 ---------for row , axis=1 ------for column
b_append= np.append(b,[[15,16]],axis=0)
print(b_append)

# To update the Array column wise,  we ll create new col and reshape it, then will appned 
col= np.array([15, 16]).reshape(2,1)
b_append2= np.append(b, col, axis=1)
print(b_append2)

a_append= np.append(a,col, axis=1)
print(a_append)

#Modify array using Insert()
#Adds value at a given position and axis in an array
#Syntax
#numpy.insert(array, obj, values, axis)
#array----input array
#obj------index position
#values---array of values needs to be inserted 
#axis----axis along which values should be inserted

a_ins= np.insert(a,0, [0,0], axis=0)
a_ins1= np.insert(a,1, [20,30], axis=0)
print(a_ins)
print(a_ins1)

#Modify array using Delete()
a_del= np.delete(a_ins,0,axis=0)
print(a_del)





