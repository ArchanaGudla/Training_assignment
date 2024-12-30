#write a python program code print your name 100 times:
name = "Archana"
for _ in range(100):
    print("Archana")

#To write a python program is it even or odd
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

#To write a python program 7th table:
number = 16
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

#Write python program comparison two numbers to check whether which variable is minimum or maximum:
# Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the numbers
if num1 > num2:
    print(f"The maximum number is {num1} and the minimum number is {num2}")
elif num1 < num2:
    print(f"The maximum number is {num2} and the minimum number is {num1}")

# To write a program on largest of 3 numbers:
# Input three numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Compare the numbers and find the largest
if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")




##
#Task:

#create a list:
list = ["Archana", "Rachana", "Madhu","chaithu","Thrishan"]
print(", ".join(list))

#access the list:
list = ["archana", "Rachana", "Madhu","Chaithu","Thrishan"]
# Print the Third item of the list
print(list[3])

#Change the list items:
list=["archana", "Rachana", "Madhu","Chaithu","Thrishan"]
list[2] = "Sairam"
print(list)

#replace the values in list:
list = ["archana", "Rachana", "Madhu", "Chaithu", "Thrishan"]
list[list.index("Chaithu")] = "Nani"
print(list)

#appending operations on the list:
list = ["archana", "Rachana", "Madhu", "Chaithu", "Thrishan"]
list.append("Chikky")
print(list)

#insert into new items:
list = ["archana", "Rachana", "Madhu", "Chaithu", "Thrishan"]
list.insert(5,"Srikanth")
print(list)

#Extend item into the list:
list1=["archana", "Rachana", "Madhu", "Chaithu", "Thrishan"]
list2=["Harsha","Bablu"]
list.extend(list2)
print(list)

#Remove the items in the list:
list=["archana", "Rachana", "Madhu", "Chaithu", "Thrisha"]
list.remove("archana")
print(list)

#clearing the entire list:
list=["archana", "Rachana", "Madhu", "Chaithu", "Thrisha"]
list.clear()
print(list)