"""
Created on Sun Mar 29 16:51:48 2020
@author: pooja.behera
"""
#Strig of Arrays


#Specify a Variable Type
#There may be times when you want to specify a type on to a variable.
#This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types,

# type casting to intiger type
x= int(1)
y= int(2.8)
z= int("5")


# type casting to float type
a= float(2.5)
b= float(5)
c= float("5.0")

# type casting to string type

p= str("A1")
q= str("5")
r= str("5.0")

#String
#Python does not have a character data type, a single character is simply a string with a length of 1.

x= "Hello world"
print(x[3])

#String Slicing
#You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.

b = "This world is beautiful"
print(b[0:7])

print(len(b))

#The strip() method removes any whitespace from the beginning or the end:
print(b.strip())
print(b.lstrip())
print(b.rstrip())


#The lower() method returns the string in lower case:
print(b.lower)