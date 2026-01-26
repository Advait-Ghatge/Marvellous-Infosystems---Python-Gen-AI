# 1. Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.

def AddList(List1):

    Sum = 0

    for i in List1:
        Sum = Sum + i
        i = i + 1
        
    print("The addition of elements from list is :", Sum)

# 2. Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.

def MaxList(List2):

    MaxNum = None

    for i in List2:

        if MaxNum == None:
            MaxNum = i

        else:
            if i > MaxNum:
                MaxNum = i

    print("The maximum number from given list is :", MaxNum)


# 3. Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.

def MinList(List3):

    MinNum = None

    for i in List3:

        if MinNum == None:
            MinNum = i

        else:    
            if i < MinNum:
                MinNum = i

    print("The minimum number from given list is :", MinNum)

# 4. Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.

def ElementFrequency(List4, CountNum2):

    count = 0

    for i in List4:
        if CountNum2 == i:
            count = count + 1

    print("The frequency of given number is :", count)

# 5. Write a program which accept N numbers from user and store it into List. 
#    Return addition of all prime numbers from that List. 
#    Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. 
#    Name of the function from main python file should be ListPrime().

from MarvellousNum import ChkPrime

def ListPrime(List5):
    
    SumOfPrimes = 0

    for i in List5:
        if ChkPrime(i) == True:
            SumOfPrimes = SumOfPrimes + i

    print("The sum of prime numbers in given list is :", SumOfPrimes)


def main():
    
    print()
    NumList =[]

    CountElements = int(input("How many numbers do you want to store in a list? - "))
    print()

    for i in range(CountElements):
        Num1 = int(input("Enter number : "))
        NumList.append(Num1)

    # print()
    # print("Your list of numbers is :", NumList)

    # Answer 1
    print()
    AddList(NumList)

    # Answer 2
    print()
    MaxList(NumList)

    # Answer 3
    print()
    MinList(NumList)

    # Answer 4
    print()
    CountNum1 = int(input("Enter number whose frequency you want to check - "))
    print()
    ElementFrequency(NumList, CountNum1)

    # Answer 5
    print()
    ListPrime(NumList)
    print()

if __name__ == "__main__":
    main()