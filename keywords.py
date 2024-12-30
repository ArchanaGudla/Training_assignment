#AND:
a = 50
b = 40
c = 10
if a > b and b > c :
    print("Both conditions are true")
#Output : Both conditions are true

#OR
x = 10
y = 5

if x > 5 or y > 10:
    print("At least one condition is True")
else:
    print("Both conditions are False")
    #output: At least one condition is True

#NOT
x = True

if not x:
    print("x is False")
else:
    print("x is True")

#IF
age = 18

if age >= 18:
    print("You are an adult.")
    #output:You are an adult.
#ElSE
age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
#output:
#You are an adult.
#You are a minor.

# ELIF
number = 10

if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")
 #outpt: positive number

 #WHILE:
count = 1
while count <= 5:
    print(count)
    count += 1

#FOR:
Names = ["Archana", "Rachana", "Chaithu"]
for Name in Names:
    print(Name)

#IN:
Names = ['Archana', 'Rachana', 'Chaithu', 'Thrishan']
if 'Madhu' in Names :
    print("Madhu is present")
else :
    print("not present")

#TRY:
a = 10
b = 0
try :
    c = a / b
    print("div : ",c)
except Exception as e:
    print("e")
    print("Div by 0 NOT-OK in python")
#Output : e
#Div by 0 NOT-OK in python
#TRY:

a="10"
b= -10
try :
    c=a+b
    print("add :",c)
except Exception as Archana :
    print("Archana")
    print("add by 0 NOT-ok in python")

#Except:
a="10"
b= -10
try :
    c=a+b
    print("add :",c)
except Exception as Archana :
    print("Archana")
    print("add by 0 NOT-ok in python")

#Finally:
marks = 120
marks = 90
try :
    if(marks>100):
        raise Exception("marks are greater than 100")
    print("given marks:",marks)
except Exception as e :
    print(e)
finally :
    print("Finally block is executed")
# Output :
# given marks: 90
# Finally block is executed

#Def
def sum (a, b) :
    return a + b
print(sum(1,6))
#Output:7

#Return:
def square(num):
    return num * num
result = square(5)
print(result)

#Import:
import math

result = math.sqrt(16)
print(result)  # Output: 4.0

#class:
class Flower:
    def __init__(self, color, type):
        self.color = color
        self.type = type

    def describe_flower(self):
        print(f"This is a {self.color} {self.type} flower.")

# Creating flower instances
rose = Flower("Red", "Rose")
lily = Flower("White", "Lily")

# Describing the flowers
rose.describe_flower()  # Output: This is a Red Rose flower.
lily.describe_flower()  # Output: This is a White Lily flower.

# class Fruits:
#     def __init__(self,color,type):
#         self.color=color
#         self.type=type
#         def describe_fruits(self):
#            print(f"this is a {self.color} {self.type} fruits")
#
#         mango = Fruits("yello", "mango")
#         apple = Fruits ("red", "apple")
#         mango.describe_Fruits()
#         apple.describe_Fruits()

#FROM:
from math import sqrt

result = sqrt(25)
print("The square root of 25 is", result)

#AS
import numpy as np

arr = np.array([1, 2, 3])
print(arr)

#True
x = 20

if x > 15:
    print("True")
else:
    print("False")

#False
x = 20

if x > 30:
    print("True")
else:
    print("False")
#output= False

#NONE:
x = None

if x is None:
    print("x is None")
else:
    print("x is not None")

#output: x is None

#IS:
a = 10
b = 10
print(a is b)

#output:True

#LAMBDA
add = lambda x: x + 10
print(add(5))
#output:15

#WITH
# Opening and closing a file automatically using 'with'
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")

# Using 'with' with a custom context manager
with MyContextManager() as manager:
    print("Inside the context")

# No need to explicitly close the file

#GLOBAL:
c = 10  # Initialize c globally

def add():
    global c  # Using the global keyword to modify the global variable c
    c = c + 2
    print(c)

add()  # Calling the add function
#output: 12

#NON-LOCAL:
x = 5  # Global x

def name():
    x = 10  # Local x inside the function
    print("Non-local x:", x)  # This prints the local x inside the function

name()  # Calling the function
print("global x:", x)  # This prints the global x
#output:
#Non-local x: 10
#global x: 5

a = lambda x, y : x*y
print(a(7, 19))