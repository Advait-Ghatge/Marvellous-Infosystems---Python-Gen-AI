from functools import reduce

print()
Items = int(input("How many numbers do you want in your data : "))
print()

Data = []

for i in range(Items):
    Num = int(input("Enter a number : "))
    Data.append(Num)

print()
print("Your data is : ", Data)
print()

# 1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

print()
Items = int(input("How many numbers do you want in your data : "))
print()

Data = []

for i in range(Items):
    Num = int(input("Enter a number : "))
    Data.append(Num)

print()
print("Your data is : ", Data)
print()

MData1 = list(map((lambda no : no * no), Data))
print("List of Squared Numbers is :", MData1)
print()

# 2. Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.

print()
Items = int(input("How many numbers do you want in your data : "))
print()

Data = []

for i in range(Items):
    Num = int(input("Enter a number : "))
    Data.append(Num)

print()
print("Your data is : ", Data)
print()

FData2 = list(filter((lambda no : no % 2 == 0), Data))
print("List of Even Numbers is :", FData2)
print()

# 3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.

print()
Items = int(input("How many numbers do you want in your data : "))
print()

Data = []

for i in range(Items):
    Num = int(input("Enter a number : "))
    Data.append(Num)

print()
print("Your data is : ", Data)
print()

FData3 = list(filter((lambda no : no % 2 != 0), Data))
print("List of Odd Numbers is :", FData3)
print()

# 4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.

print()
Items = int(input("How many numbers do you want in your data : "))
print()

Data = []

for i in range(Items):
    Num = int(input("Enter a number : "))
    Data.append(Num)

print()
print("Your data is : ", Data)
print()

RData4 = reduce((lambda no1, no2: no1 + no2), Data)
print("Addition of Numbers in List is :", RData4)
print()

# 5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

print()
Items = int(input("How many numbers do you want in your data : "))
print()

Data = []

for i in range(Items):
    Num = int(input("Enter a number : "))
    Data.append(Num)

print()
print("Your data is : ", Data)
print()

RData5 = reduce((lambda no1, no2 : max(no1, no2)), Data)
print("The largest number is :", RData5)
print()

# 6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.

print()
Items = int(input("How many numbers do you want in your data : "))
print()

Data = []

for i in range(Items):
    Num = int(input("Enter a number : "))
    Data.append(Num)

print()
print("Your data is : ", Data)
print()

RData6 = reduce((lambda no1, no2 : min(no1, no2)), Data)
print("The smallest number is :", RData6)
print()

# 7. Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

print()
Items = int(input("How many string items do you want in your data : "))
print()

StrData = []

for i in range(Items):
    Str1 = (input("Enter a string : "))
    StrData.append(Str1)

print()
print("Your data is : ", StrData)
print()

FData7 = list(filter(lambda str1 : len(str1) > 5, StrData))
print("Strings having more than 5 characters are :", FData7)
print()

# 8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

print()
Items = int(input("How many numbers do you want in your data : "))
print()

Data = []

for i in range(Items):
    Num = int(input("Enter a number : "))
    Data.append(Num)

print()
print("Your data is : ", Data)
print()

FData8 = list(filter(lambda no : no % 3 == 0 and no % 5 == 0, Data))
print("Numbers divisible by 3 and 5 are:", FData8)
print()

# 9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

print()
Items = int(input("How many numbers do you want in your data : "))
print()

Data = []

for i in range(Items):
    Num = int(input("Enter a number : "))
    Data.append(Num)

print()
print("Your data is : ", Data)
print()

RData9 = reduce(lambda no1, no2: no1 * no2, Data)
print("Product of all numbers is :", RData9)
print()

# 10. Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

print()
Items = int(input("How many numbers do you want in your data : "))
print()

Data = []

for i in range(Items):
    Num = int(input("Enter a number : "))
    Data.append(Num)

print()
print("Your data is : ", Data)
print()

FData10 = list(filter(lambda no : no % 2 == 0, Data))
print("Even numbers in this data are :", FData10)

print()
