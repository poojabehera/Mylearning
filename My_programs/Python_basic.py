
"""
Created on Sat Mar 28 13:25:54 2020
@author: pooja.behera
"""
#Operator
#Legal variable names:
var="Jhon"
var_type="Jhon"
_var_type="Jhon"
varType="Jhon"
Vartype="Jhon"
vartype2= 'Jhon'

#Assign values to multiple variables

x, y, z, k= 'Jhon', 'rita', 'nita', 'Jollie'

# Alternate case

x= y= "Jhon"
print(x)
print(y)
#Output Variables
#The Python print statement is often used to output variables.
#To combine both text and a variable, Python uses the + character:
var1 ="I am beautiful"
print("Pooja says:"+ var1 )

varx= " this is wonderful "
vary=" this is waste "
print(varx + vary)

#For Numbers  Python uses the + as mathematical operator:

m=10
n=10
print(m+n)

#Error
m1= "Jhon is a sweet boy"
n1= 25
print(m1 + n1)
#TypeError: can only concatenate str (not "int") to str
res="John is a sweet and he is of{}"
print(res.format(n1))
    
#Data conversion
x="10"
type(x)
int(x)
y= int(x)
y
type(y)
#or type int
x= int(4)
y= int(4.5)
z= int("4")

#type float
x= float(4.5)
y= float(4)
z= float('4')

#type string
x= str("S1")
y= str(2)
z= str(3.0)
#********************Escape characters******************
##\n new line
##\t new tab
##\b back space
x= "the\nwhite\nhouse"
print(x)
y="the\twhite\thouse"
print(y)



