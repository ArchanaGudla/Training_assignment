#1. Numeric Data Types
x = 10  # Integer
y = 3.14  # Floating-point
z = 2 + 3j  # Complex

print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'complex'>

#2. Sequence Data Types
my_string = "Hello"
print(my_string[1])

my_list = [1, 2, 3, "apple"]
print(my_list[2])

my_tuple = (10, 20, 30)
print(my_tuple[0])

my_list[1] = 5
print(my_list)

#3. Mapping Data Type
dic={1:"Archana",2:"Rachana",3:"Chaithu"}
print(dic)
print(type(dic))
print(dic.keys())
print(dic.values())

#4. Set Data Type
#1.Set:
mset = {54, 34, 45, 76, 88}
print(mset)
mset.add(100)
print(mset)

#2.Frozenset:
fs = frozenset([18, 20, 36, 46])
print(fs)
print(type(fs))

#5.Boolean Type
a = 67
b = 34
result = a < b
print(result)

#6.Binary Type
#1.Bytes:
data = b"hello"
print(type(data))

#2.Bytearray
ba = bytearray(b"Archana")
ba[0] = 67
print(ba)  #bytearray(b'Crchana')

#Memoryview
b_data = b"Rachana"
# Create a memoryview
mv = memoryview(b_data)
# Access the first element
print(mv[0])     #82

#7.None Type
def my_function():
    pass
result = my_function()
print(result)  # Output: None

#Example2:
if not None:
    print("None is False")  # Output: None is False









#my_dict = {'name': 'Archana', 'age': 21, 'city': 'Kne'}
#print(my_dict['name'])
#print(my_dict['age'])
#print(my_dict['city'])
#my_dict['country'] = 'India'  # Add a new key-value pair
#print(my_dict['country'])
#my_dict['age'] = 31
#print(my_dict['age'])
#del my_dict['Name']  # Remove a key-value pair