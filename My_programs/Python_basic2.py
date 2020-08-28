"""Created on Sun Mar 29 16:27:02 2020
@author: pooja.behera
# setting data type
# Data type conversio
# random Number using rand buolt in function



"""
#Setting the Specific Data Type

x= int(5)
print(type(x))
y= 2.5
k=-2.5
print(type(y))
print(type(k))
z= 1j
z1= 3+1j
z2= -5j
print(type(z))
print(type(z1))
print(type(z2))

y= str("Pooja")
z= float(2.0)
a= complex(1j)
print(a)
print(type(a))
x= list(("apple","rose"))
y=tuple(("apple","rose"))
z= dict(name="Pooja", age=25, Domain="Data scientist")
z= set(("apple", "Banana", "Pinapple"))
print(type(z))


#Type Conversion

x= 5      #int
y= 5.5    #float
z= 1+5j   #complex

a=float(x)
print(a)

b=int(z)
print(b)

c=complex(x)
print(c)

#Random Number
#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
import random
print(random.randrange(1, 10))








