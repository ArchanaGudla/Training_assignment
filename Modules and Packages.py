#•	User defined modules
a=10
b=20
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return  a/b

c = add(a,b)
print(c)

c = sub(a,b)
print(c)

c= mul(a,b)
print(c)

c = div(a,b)
print(c)

#Built-in modules :
#1.Math
import math
print(math.pi)

#example:
import math

# Using a function from the math package
result = math.sqrt(4)
print(result)  # Output: 2.0

#2. Random
import random
print(random.randint(10, 20))

#3. Datetime
import datetime
now = datetime.datetime.now()
print(now)


#Package:
#my_package/
   # __init__.py
    #module1.py
    #module2.py
    #sb_package/
      #  __init__.py
       # submodule1.py
        #submodule2.py
#Example: Creating a Package
# module1.py
def greet(name):
    return f"Hello, {name}!"
# module2.py
def add(a, b):
    return a + b

