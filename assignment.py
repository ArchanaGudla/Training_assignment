#Difference between break, continue,pass:
#break:
for i in range(5):
    if i == 4:
        break
    print(i)

#continue:
for i in range(5):
    if i == 4:
        continue
    print(i)
#pass:
for i in range(5):
    if i == 2:
        pass
    print(i)

#Difference between delete,pop,Remove:
#1.remove()
list=["archana", "Rachana", "Madhu", "Chaithu", "Thrisha"]
list.remove("archana")
print(list)

#2.Delete():
list=["archana", "Rachana", "Madhu", "Chaithu", "Thrisha"]
del list [1]
print(list)

#POP():
list = ["archana", "Rachana", "Madhu", "Chaithu", "Thrisha"]
item = list.pop(1)
print(list)

#difference between append and extend:
list = ["archana", "Rachana", "Madhu", "Chaithu", "Thrishan"]
list.append("Chikky")
print(list)

#Write a python program to print the element in the array with negative elements (ex : print the element which is present  in -2 positions) ..?

array = [36, 79, 87, 60, 54]


negative_index = -2

if abs(negative_index) <= len(array):
    print(f"The element at position {negative_index} is: {array[negative_index]}")
else:
    print(f"Invalid negative index {negative_index} for the array.")

#LAMDA:

def add(x, y):
    return x + y

add_lambda = lambda x, y: x + y
print(add_lambda(5, 3))


#Write a python program to print your name , designation, technology 100 times ?
name = "Archana"
designation = "Intern"
technology = "Devops"

for _ in range(100):
    print(f"Name: {name}, Designation: {designation}, Technology: {technology}")


