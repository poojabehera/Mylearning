# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 00:15:28 2020

@author: pooja.behera
"""
#Linear Algebra Operations in Python
#Matrix determination----Syntax------np.linalg.det(matrix)
#Rank of Matrix
#Inverse of Matrix
#Solving system of equation
import numpy as np
A= np.matrix("1,2,3; 2,4,6; 6,8,10")
print(A)
Det_mat= np.linalg.det(A)
print(Det_mat)
B= np.matrix("2,4,6; 6,8,1; 2,4,6")
Det_mat= np.linalg.det(B)
print(Det_mat)

#Matrix Rank
#Shows independent Rows and cols
Rank_mat= np.linalg.matrix_rank(A)
print(Rank_mat)

#Inverse of a Matrix                                        
#np.matrix.inv()--returns multiplicative inverse of a matrix
A= np.matrix("1,2,3; 2,4,6; 6,8,10")
Inv_matrix= np.linalg.inv(A)
print(Inv_matrix)
#Condition to find Inverse of Matrix is Determinanat should not be = 0
# it showing "Singular matrix" error that means its determinant is 0
Det_matrix= np.linalg.det(A)
print(Det_matrix)

#System of Linear equation
#solve two matrices together 
a=np.matrix("3,1,2; 3,2,5; 6,7,8")
print(a)
b= np.matrix("1,2,3")
print(b)
b= np.matrix("1,2,3").transpose()
print(b)

#In Python np.linalg.solve()--return sol to system of linear equation in form of Ax= b
Sol_linear= np.linalg.solve(a,b)
print(Sol_linear)

#**********************MASS BALANCE Operation*******************************
A= np.matrix("0.24,0.15,0.18,0.07; 0.65,0.10,0.24,0.04;\
             0.10,0.54,0.42, 0.54; 0.01,0.21,,0.18,0.35")
print(A)
B=np.matrix("75,125,200,100").transpose()
print(B)
Sol_linear= np.linalg.solve(A,B)
print(Sol_linear)
