#EVEN OR ODD

num = int(input("Enter a number "))

if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")


#Armstrong number  153
num = int(input("Enter a 3-digit number: "))
original_num = num
sum = 0
while num > 0:
    digit = num % 10
    sum += digit ** 3
    num //= 10

if original_num == sum:
    print(original_num, "is an Armstrong number")
else:
    print(original_num, "is not an Armstrong number")


#Sum of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter  second number: "))
print("Sum:", a + b)


#Find the Largest Number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Largest:", max(a, b))



#Print Fibonacci Sequence
n = int(input("Enter a number : "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# Check Prime Number   2 3 5 7 11
num = int(input("Enter a number: "))

if num > 1:

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is Not Prime")
            break
    else:

        print(f"{num} is Prime")
else:

    print(f"{num} is Not Prime")


#Find HCF (GCD)
a = int(input("Enter first number: ")) #10
b = int(input("Enter second number: ")) #20
while b:
    a, b = b, a % b
print("HCF:", a)


#Find LCM
from math import gcd

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("LCM:", abs(a * b) // gcd(a, b))


#Reverse a Number
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed:", rev)


#Check Palindrome Number  121
num = input("Enter a number: ")
print("Palindrome" if num == num[::-1] else "Not Palindrome")


#Calculate Factorial
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial:", factorial)


#Sum of Digits
num = int(input("Enter a number: "))
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum of digits:", total)


#Count Digits in a Number
num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Number of digits:", count)


#Print Multiplication of  Tables
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


#Print All Factors of a Number
num = int(input("Enter a number: "))
factors = [i for i in range(1, num + 1) if num % i == 0]
print("Factors:", factors)


#Generate a Star Pattern
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print("*" * i)


#Print a Pyramid Pattern
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))


#Find Sum of N Natural Numbers
n = int(input("Enter a number: "))
print("Sum:", n * (n + 1) // 2)

#Find the whole numbers:
start = 0
end = 10
for num in range(start, end + 1):
    print(num)

#write a program on prime numbers bewlow 100
print("Prime numbers below 100 are:")
for i in range(2, 100):
    if all(i % x != 0 for x in range(2, int(i ** 0.5) + 1)):
        print(i, end=" ")

##print hello world:
print("hello,world")

## Simple Calculator (Addition)
num1= int(input("enter first number:"))
num2=int(input("enter second number:"))
sum= num1+num2
print("The sum is:", sum)

#even or odd:
num=int(input("enter a number:"))
if num % 2 == 0:
    print (num,"is even")

else:
    print(num,"is odd")

##Factorial of a Number:
num=int(input("enter a number:"))
factorial =1
for i in range (1,num + 1):
    factorial *=i
    print(f"The factorial of {num} is {factorial}.")


#palindrome:

string = input("Enter a string: ")

if string == string[::-1]:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")

#To print a prime number below 100:
print("Prime numbers below 100:")
for n in range(2, 100):
    if all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
        print(n, end=" ")

#practice:
#even or odd
num =int(input("enter a number:"))
if num % 2 == 0:
    print(num,"is even:")
else:
    print(num,"is odd:")

#sun of two numbers:
a= int(input("enter a first number:"))
b= int(input("enter a second number"))
print("sum:", sum)


#to find the largest number:
a= int(input("enter a fist number:"))
b= int(input("enter a second numbser:"))
print("Largest:", max(a, b))


#to find the smallest number:
a=int(input("enter a first  number:"))
b=int(input("enter a second number:"))
print("smallest:", min (a,b))

###division of two numbsers:

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if b != 0:
    print("Division result:", a / b)
else:
    print("Error: Division by zero is not allowed.")


###Fibonacci
n=int(input("enter a number:"))
a,b=1,2
for i in range (n):
    print(a,end="")
    a,b = b,a + b

#LCM:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("LCM:", abs(a * b) // gcd(a, b))

#palindrom:121
num = input("Enter a number: ")
print("Palindrome" if num == num[::-1] else "Not Palindrome")

