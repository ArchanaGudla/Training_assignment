#For Loops:
#1
numbers = [67, 98, 90, 46, 53]
for number in numbers:
    print(number)
#2
for i in range(5):
    print(f"Iteration {i}")
#3
for i in range(1, 6):
    print(i)
#4 Iterating over a list:
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#
#for loop with tuple
x='Archu'
for i in x:
    print(i)

# Iterating over a string:
word = "hello"
for char in word:
  print(char)

# Iterating over a range of numbers:Python
for i in range(5):
  print(i)

#Nested for loops:Python
for i in range(3):
  for j in range(2):
    print(i, j)

#Using break and continue:Python
for i in range(10):
  if i == 5:
    break
  if i % 2 == 0:
    continue
  print(i)

#Iterating over a dictionary:Python

person = {"name": "Archana", "age": 21, "city": "Knr"}
for key, value in person.items():
  print(key, value)

#while loops:
  count = 0
  while count < 5:
      print(count)
      count += 1

#Infinite Loop
while True:
  print("Hello, world!")
