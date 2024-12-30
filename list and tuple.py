#LIST:
list = ["Archana", "Rachana", "Madhu"]
print(", ".join(list))  # Outputs: Archana, Rachana, Madhu

#Dupicates:
list_a = ["Archana", "Rachana", "Madhu", "Archana", "chaithu"]
print(list_a)

#List Length:
names = ["Archana", "Rachana", "Chaithu"]
print(f"The number of names in the list is: {len(names)}")

#List Items - Data Types:
# List of strings
list1 = ["Archana", "Rachana", "Madhu"]

# List of integers
list2 = [1, 5, 7, 9, 3]

# List of booleans
list3 = [True, False, False]

# Printing the lists
print("List of Strings:", list1)
print("List of Integers:", list2)
print("List of Booleans:", list3)

#Access Items:
# List of fruits
thislist = ["apple", "banana", "cherry"]

# Print the second item of the list
print(thislist[1])  # Output: banana

#Negative Indexing:
# List of fruits
thislist = ["apple", "banana", "cherry"]

# Print the last item of the list
print(thislist[-1])  # Output: cherry

#Range of Indexes (Slicing):
# List of fruits
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# Print the third, fourth, and fifth items
print(thislist[2:5])  # Slicing from index 2 to index 5 (5 is excluded)

# Print items from the start to the fourth item
print(thislist[:4])  # Slicing from the start (index 0) to index 4 (4 is excluded)

#Adding Items to List:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")  # Adds "orange" to the end of the list
print(thislist)

#Insert Items:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")  # Inserts "orange" at index 1
print(thislist)

#Extend List:
#Example
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#o/p ["apple", "banana", "cherry","mango", "pineapple", "papaya"]

#Remove Item from List
#Remove Specified Item
#Example
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")  # Removes the first occurrence of "banana"
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")  # Removes only the first occurrence of "banana"
print(thislist)

#Remove Item at Specified Index:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)  # Removes the item at index 1 ("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()  # Removes the last item ("cherry")
print(thislist)

#Sorting List:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()  # Sorts the list in ascending alphabetical order
print(thislist)

#Example
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)  #o/p [23,50,65,82,100]
#Example
thislist = [100, 50, 65, 82, 3]
thislist.sort(reverse = True)
print(thislist)  #o/p [100,82,65,50,3]

#Tuple:
#Create a Tuple:
# tuple = ("apple", "banana", "cherry")
print(tuple)  #o/p ("apple", "banana", "cherry")

#Tuple allows Duplicates:
#Example
tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(tuple)   #o/p ("apple", "banana", "cherry", "apple", "cherry")

#Access Tuple Items

x = ("apple", "banana", "cherry")  # Original tuple
y = list(x)                        # Convert tuple to list
y[0] = "orange"                      # Modify the second element
x = tuple(y)                       # Convert list back to tuple
print(x)                           # Print the updated tuple

#Add tuple to a tuple.
#Example
tuple = ("apple", "banana", "cherry")
y = ("orange",)
tuple += y
print(tuple)
#o/p ("apple", "banana", "cherry",”orange”)

#Tuple Methods:
#count():
tuple = ("apple", "banana", "cherry", "apple")
print(tuple.count("apple"))

tuple =("apple","banana","cherry","apple")
print(tuple.count("banana"))

#index():
tuple=("apple","banana","cherry","apple")
print(tuple.index("cherry"))

#Operations on Tuples:
#Concatenation (+):
tuple1 =("apple","banana")
tuple2 =("cheery","kiwi")
result= tuple1 + tuple2
print(result)

#Repetition (*):
tuple1=("apple","banana")
result= tuple1 * 4
print (result)

#Slicing:
tuple=("apple","banana","cherry","kiwi")
print(tuple[0:4])

#Membership (in and not in):
tuple = ("apple", "banana", "cherry")
print("banana" in tuple)
print("apple" not in tuple)

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

mu_list=["Archana","gudla"]
print= my_list[::-1]