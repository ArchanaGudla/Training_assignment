# a=10
# b=20
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
#
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)
# print(a!=b)
#
# x=True
# y=False
# print(x and y)
# print(x or y)
# print(not x)
# print(not y)
# print (not (x and Y))
from operator import is_not

# total = 10
# total += 5
# total -= 3
# total *= 2
# total /= 4
# print("Final value of total:", total)

a = 10
b = 4
#
# # Bitwise operations
# bitwise_and = a & b
# bitwise_or = a | b
# bitwise_xor = a ^ b
# bitwise_not_a = ~a
# left_shift = a << 2
# right_shift = b >> 1
# print(a&b)
# print(a|b)
# print(a^b)
# print(~a)
# print(a<<2)
# print(b>>1)



# my_list=[7,22,98,76,36,87]
# print(2 is my_list)
# print(10 is not my_list)
# print(2 in my_list)
# print(100 not in my_list)
# list1=[1,2,4,5]
# list2=[3,4,5,6]
# print(list1 is list2)
# print(list1 is not list2)
# operators:

# 1. Addition (+)
a = 10
b = 5
print (a + b)
#print(result) # Output: 15

#  2. Subtraction (-)
a = 10
b = 5
print (a - b)
#print(result)  #  10-5  Output: 5

# 3, Multiplication (*)
a = 10
b = 5
print(a * b)
#print(result)  # Output: 50

# 4. Division (/)
a = 10
b = 5
print(a / b)
#print(result)  # Output: 2.0

# 5. Floor Division (//)
a = 10
b = 5
print(a // b)
#print(result)  # Output: 2

# 6. Modulus (%)
a = 10
b = 5
print( a % b)
#print(result) # Output: 0


# 7. Exponentiation (**)
a=10
b=5
result= a**b
#print(result) #output=100000


#Comparison Operators:
x = 10
y = 5

print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)   # Output: True
print(x < y)   # Output: False
print(x >= y)  # Output: True
print(x <= y)  # Output: False

#logical operator:
x = True
y = False

print(x and y)  # Output: False
print(x or y)   # Output: True
print(not x)    # Output: False

#assignment operator:
# 1. Assign (=)
x = 5
print(x)  # Output: 5

# 2. Add and Assign (+=)
x = 5
x += 3
print(x)  # Output: 8

# 3. Subtract and Assign (-=)
x = 5
x -= 3
print(x)  # Output: 2

# 4. Multiply and Assign (*=)
x = 5
x *= 3
print(x)  # Output: 15

# 5. Divide and Assign (/=)
x = 10
x /= 2
print(x)  # Output: 5.0

# 6. Modulus and Assign (%=)
x = 10
x %= 3
print(x)  # Output: 1


#bitwise operator:
x = 10
y = 5

print(x & y)  # Output: 0
print(x | y)  # Output: 15
print(x ^ y)  # Output: 15
print(~x)    # Output: -11
print(x << 2)  # Output: 40
print(x >> 2)  # Output: 2

#6. Membership Operators
a = [1, 2, 3, 4, 5]
print(3 in a)      # True
print(6 not in a)  # True

#7. Identity Operators
# 1. is
a = [1, 2, 3]
b = a

#result = a is b
print(result)  # Output: True

a = [1, 2, 3]
b = [1, 2, 3]

result = a is b
print(result)  # Output: False

# 2. is not
a = [1, 2, 3]
b = [1, 2, 3]

result = a is not b
print(result)  # Output: True

a = [1, 2, 3]
b = a

