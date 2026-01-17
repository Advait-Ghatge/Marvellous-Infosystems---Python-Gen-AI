# 1. Write a program which accepts one number and prints multiplication table of that number.

def MultiplicationTable():

    Num1 = int(input("Enter a number : "))
    print()
    Table = list()

    for i in range(1,11):
        Num2 = Num1 * i
        Table.append(Num2)

    print("The multiplication table of that number is : ", Table)
    print()


# 2. Write a program which accepts one number and prints sum of first N natural numbers.

def SumN():

    Num1 = int(input("Enter a number : "))
    Sum = 0
    print()

    for i in range(1,Num1+1):
        Sum = Sum + i
    
    print("Sum of first N natural numbers upto", Num1, "is :", Sum)
    print()


# 3. Write a program which accepts one number and prints factorial of that number.

def Factorial():

    Num1 = int(input("Enter a number : "))
    print()
    Factorial = 1

    for i in range(1, Num1+1):
        Factorial = Factorial * i

    print("Factorial of ", Num1, "is :", Factorial)
    print()


# 4. Write a program which accepts one number and prints all even numbers till that number.

def EvenList():

    Num1 = int(input("Enter a number : "))
    print()
    ListEven = list()

    for i in range(1, Num1):
        if i % 2 == 0:
            ListEven.append(i)

    print("The list of even numbers upto ", Num1, "is :", ListEven)
    print()

# 5. Write a program which accepts one number and prints all odd numbers till that number.

def OddList():
    
    Num1 = int(input("Enter a number : "))
    print()
    ListOdd = list()

    for i in range(1, Num1):
        if i % 2 != 0:
            ListOdd.append(i)

    print("The list of even numbers upto ", Num1, "is :", ListOdd)
    print()

def main():

    print()

    # Answer 1
    MultiplicationTable()

    # Answer 2
    SumN()

    # Answer 3
    Factorial()

    # Answer 4
    EvenList()

    # Answer 5
    OddList()

if __name__ == "__main__":
    main()