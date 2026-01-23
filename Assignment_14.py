# 1. Write a lambda function which accepts one number and returns square of that number.

print()
num1 = int(input("Enter a number : "))

Square = lambda num1 : num1 * num1

print("Square of entered number is :", Square(num1))
print()

# 2. Write a lambda function which accepts one number and returns cube of that number.

num1 = int(input("Enter a number : "))

Cube = lambda num1 : num1 * num1 * num1

print("Square of entered number is :", Cube(num1))
print()

# 3. Write a lambda function which accepts two numbers and returns maximum number.

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print()

GreaterThan = lambda num1, num2 : num1 > num2

if GreaterThan(num1, num2) == True:
    print("First number i.e.", num1, "is greater")

else:
    print("Second number i.e.", num2, "is greater")

print()

# 4. Write a lambda function which accepts two numbers and returns minimum number.

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print()

SmallerThan = lambda num1, num2 : num1 > num2

if SmallerThan(num1, num2) == True:
    print("Second number i.e.", num2, "is smaller")

else:
    print("First number i.e.", num1, "is smaller")

print()

# 5. Write a lambda function which accepts one number and returns True if number is even otherwise False.

num5 = int(input("Enter a number : "))

IsEven = lambda num5 : num5 % 2 == 0

if IsEven(num5) == True:
    print("Number is even")

else:
    print("Number is odd")

print()

# 6. Write a lambda function which accepts one number and returns True if number is odd otherwise False.


num6 = int(input("Enter a number : "))

IsOdd = lambda num6 : num6 % 2 != 0

if IsOdd(num6) == True:
    print("Number is odd")

else:
    print("Number is even")

print()

# 7. Write a lambda function which accepts one number and returns True if divisible by 5.

num7 = int(input("Enter a number whose divisbility by 5 is to be checked : "))

Divby5 = lambda no : no % 5 == 0

if Divby5(num7) == True :
    print("Number is divisible by 5")

else:
    print("Number is not divisible by 5")

print()

# 8. Write a lambda function which accepts two numbers and returns addition.

num81 = int(input("Enter first number : "))
num82 = int(input("Enter second number : "))

Addition = lambda num1, num2 : num1 + num2

print("Addition of aforementioned two numbers is :", Addition(num81, num82))
print()

# 9. Write a lambda function which accepts two numbers and returns multiplication.


num91 = int(input("Enter first number : "))
num92 = int(input("Enter second number : "))

Multiplication = lambda num1, num2 : num1 * num2

print("Multiplication of aforementioned two numbers is :", Multiplication(num91, num92))
print()

# 10. Write a lambda function which accepts three numbers and returns largest number.

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

Maxof3 = lambda num1, num2, num3 : max(num1, num2, num3)

print("Maximum of 3 given numbers is :", Maxof3(num1, num2, num3))