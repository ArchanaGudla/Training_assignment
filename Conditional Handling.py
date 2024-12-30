#Conditional Handling
#if
age = 18
if age >= 18:
    print("You are an adult.")

#if_else
number = 10

if number > 0:
    print("Positive number")
else:
    print("Negative or zero")

#elseif ladder
number = -5

if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")

#4. nested if else:
age = 25
nationality = "Indian"

if age >= 18:
    if nationality == "Indian":
        print("Eligible to vote in India")
    else:
        print("Check eligibility in your country")
else:
    print("Not eligible to vote")

#Control Statements:
#break statement
for i in range(10):
    if i == 5:
        break
    print(i)

#continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)