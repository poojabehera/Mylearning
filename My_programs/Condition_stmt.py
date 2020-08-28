"""
Created on Sun Mar 29 22:48:55 2020

@author: pooja.behera
"""
# If Conditions statement
# Iterative statement

a= 200
b= 500

if a< b: print("a")
 #short hand if else
print("A") if a>b else print("B")          
#one line if else statement
b= 200
print("A") if a<b else print("equals") if a==b else print("b")

# Elif Conditions statement
# it says if first statement not true then try this statement
a=200
b=200
if b>a:
    print("not staisfied")
elif a==b:
    print("both are equal")
    
 # Else Conditions statement 
a= 200
b= 500
if a>b:
        print("first no. is greater than second no")
elif a==b:
        print("both first and second nus. are equal")
else:
        print("b")

#Nested if
if a>500:
    print("a is gteater than 500")
if a< 500:
    print("a is less than 500")
else:
       print("but not equal to 500")
       
#**************************Iterative condition********************************    
i=1
while i<6:
    print(i)
    i += 1

#it is necccasry to put incremet after this else the loop will keep continue
    
#Break statement
i= 1
while i<6:
      print(i)
      if i==3:
          break
      i += 1
   
    

