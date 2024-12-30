#Example 1: Creating a Dictionary using Curly Braces:

# dictionary
a= {'a':123456 , 1:'abc'}
print(a)
#output:{'a': 123456, 1: 'abc'}

# get()
my = {'a': 1, 'b': 2, 'c': 3}
print(my.get('b'))
# Output: 2
print(my.get('d'))
# Output: None

# update()
k = {'a': 1, 'b': 2}
k.update({'b': 10, 'c': 3})
print(k)
# Output: {'a': 1, 'b': 10, 'c': 3}
# pop()

archana = {'a': 1, 'b': 2, 'c': 3}
value = archana.pop('b')
print(value)
# Output: 2
print(archana)
# Output: {'a': 1, 'c': 3}

#popitem()
h = {'a': 1, 'b': 2, 'c': 3}
key_value_archana = h.popitem()
print(key_value_archana)
# Output: ('c', 3)
print(h)
# Output: {'a': 1, 'b': 2}

#values()
my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values()
print(list(values))
# Output: [1, 2, 3]

#keys()
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
print(list(keys))
# Output: ['a', 'b', 'c']

#items()
my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
print(list(items))
# Output: [('a', 1), ('b', 2), ('c', 3)]

#SET:
#set example
archana={1,2,8,4,2}
k=set(archana)
print(k)
# output{1,2,8,4}
# Add()

my = {1, 2, 3}
my.add(4)
print(my)
#output: {1, 2, 3, 4}
# Clear()

my1 = {1, 2, 3}
my1.clear()
print(my1)
# output: set()

# Copy()
a = {1, 2, 3}
new = a.copy()
print(new)  # output: {1, 2, 3}

# difference
set1 = {1, 2, 3}
set2 = {3, 1, 5}
print(set1.difference(set2))  # output: {2}

# Discard()
my1 = {1, 2, 3}
my1.discard(2)
my1.discard(4)
print(my1)
# Output: {1, 3}

# Intersection()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2))
# 0utput: {2, 3}

# isdisjoint
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))
# Output: True

# pop()
hari = {1, 2, 3}
element = archana.pop()
print(element)
# Output: 1

print(archana)
# Output: {2, 3}

# remove()
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)
# Output: {1, 3}

# Symmetric difference()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.symmetric_difference(set2))
# Output: {1, 2, 4, 5}
# union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
# Output: {1, 2, 3, 4, 5}

# Update()
set1 = {1, 2, 3}
set2 = {3,4, 5}
set1.update(set2)
print(set1)
# Output: {1, 2, 3, 4, 5}
# length
b = {1, 2, 3, 4}
print(len(b))
# Output: 4
# max()
archana = {10, 20, 5, 7}
print(max(archana))
# Output: 20

# sorted()
j = {3, 1, 4, 2}
print(sorted(j))
# Output: [1, 2, 3, 4]





