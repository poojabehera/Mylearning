# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:31:53 2020

@author: pooja.behera
"""
#Dictionary----it is an example of Hash table data structure.
#work like key- value pairs, where the keys are mapped to values
#Dictionaris are enclosed by curly braces{}
#it is Mutuable data structure....we can modify teh items 

fuel_type={'Petrol':80, 'Diseal': 50,'CNG':26}
print(fuel_type)
fuel_type.values()
fuel_type.keys()

for x in fuel_type:
     print(x)
     
#Accessing the keys from values--------------Dictionary_names.keys()
fuel_type.keys()

#to acess both keys & values simlutaneously
fuel_type.items()

#the price of petrol is Rs 100
txt="the price of {} has been raised to {}"
Rs=100
item='petrol'
print(txt.format(item, Rs))
#Accessing componenets 
#to know the value of Keys
print(fuel_type['Petrol'])
print(fuel_type['Diseal'])
print(fuel_type['CNG'])

#Updating the Dictionary with index value
fuel_type['H2o']=1

#Updating the Dictionary by using update()
fuel_type.update({'Nitrogen': 750})
print(fuel_type)
fuel_type['Petrol']="Hydrogen peroxide"
print(fuel_type)

#modifying teh value of given Key
fuel_type['CNG']=100
print(fuel_type)

#deleting one item will delete one key: value pair
fuel_type1={'Petrol':80, 'Diseal': 50,'CNG':26}
del fuel_type1['Petrol']
print(fuel_type1)


#remove the entire item dictionary
fuel_type1.clear()
print(fuel_type1)

#creating Dictionaries
#these are the data structures represtents in Key value pairs
Fuel_type={"Petrol":1, "Diseal":2, 'CNG':3}

print(Fuel_type['Petrol'])
print(Fuel_type['Diseal'])
print(Fuel_type['CNG'])

#Accessing componenets of Dictionaries
#To access values from Dictonary Fuel_type
#syntax: dictonary_name.values
Fuel_type.values()

#In case we want to access keys
Fuel_type.keys()

#In case we want to access both Key and value
Fuel_type.items()

#Modifying a dictionary
#syntax: dictionary_name.[key]=value

Fuel_type["Nitrogen"]=14

#now printing the whole Fuel_types
print(Fuel_type)

#modifying without using built-in function
Fuel_type['Petrol']=20
Fuel_type['Diseal']=21
Fuel_type['CNG']=22
Fuel_type['Nitrogen']=25


#using Built-in command 'update'
#syntax: dictonary_type.update({key:value})

Fuel_type.update({'Nitrogen':11})
Fuel_type.update({'Petrol':12})
Fuel_type.update({'Diseal':13})
Fuel_type.update({'CNG':14})

#Removing keys form the dictonary
#syntax: del ditonary_name[key]

del Fuel_type["CNG"]

#To remove all the key value pairs,  clear()
Fuel_type.clear()

print(Fuel_type)




