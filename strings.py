#strings:
print("Archana")
print('Archana')
#output:
#Archana
#Archana


#string length:
s="Hello"
print(len(s))
#output= 5

#max string:
numbers = [10, 25, 30, 5, 70, 60]
max_value = max(numbers)
print("The maximum value is:", max_value)
#output: The maximum value is: 70

#min string:
numbers = [10, 25, 30, 5, 70, 60]
min_value = min(numbers)
print("The minimum value is:", min_value)
#output: The minimum value is: 5


#Inside Quotes:
print("It's alright")
print("she is called 'Chaithu'")
print('she is called "Chaithu"')
#output:
# It's alright
# she is called 'Chaithu'
# she is called "Chaithu"


#Looping Through a String
print("It's alright")
print("He is called ‘Rohi'")
print('He is called “Rohi"')



#Multiline Strings:
a= """Strings  are sequences of characters"""
print(a)
a='''Strings  are sequences of characters.'''
print(a)

#output:
#Strings  are sequences of characters
#Strings  are sequences of characters.

#methods:
#slicing string
b ="Hello, World!"
print(b[2:5])
#output:llo

#Slice From the Start:
b ="Hello, World!"
print(b[:5])
#output:Hello

#slice to the end:
b = "Hello, World!"
print(b[2:])
#output:
#llo, World!

#negative indexsing     # "H  e  l  l  o, W   o  r l  d"
                        #  0  1  2  3  4, 5 -5 -4 -3 -2 -1
b ="Hello, World!"
print(b[-5:-2])
#output: orl

#modify strings:
#upper:
a ="Hello, World!"
print(a.upper())
#output:
#HELLO, WORLD!

#lower:
a ="Hello, World!"
print(a.lower())
#output:
#hello, world!

#Strip():
a =" Hello, World! "
print(a.strip())
#output:
#Hello, World!

#Replace()
a ="Hello, World!"
print(a.replace("H","J"))
#output:
#Jello, World!


#Split():
a = " Hello, World! "
print(a.strip())

#output:
#['Hello', ' World!']
text = "apple,banana,orange"
result = text.split(",")
print(result)  # Output: ['apple', 'banana', 'orange']



#string Concatenation:
a ="Hello"
b ="World"
c = a + b
print(c)
#output: HelloWorld
#To add a space between them, add a" ":
a ="Hello"
b ="World"
c = a +" "+ b
print(c)
#output: Hello World

#Format - Strings:
print("I love {0} and {1}.".format("Python", "JavaScript"))
#outpuy:
#I love Python and JavaScript.

#Escape Characters:
text = "Hello\nWorld"
print(text)
#output:
#Hello
#World

#modification:
#strip (remove white spaces begining or ending)
a="   archana gudla    "
print(a.strip())

#UPPER:
a ="Archana"
print(a.upper())

#LOWER:
a= "Archana"
print(a.lower())

#repalce:
a ="Archana"
print(a.replace("A","R"))

#slicing:
a="Archana,gudla"
print(a[1:5])
print(a[:5])
print(a[5:])

#cancatnation:
a="Archana"
b="gudla"
print(a+b)















