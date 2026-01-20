# 1. Write a program which accepts one character and checks whether it is vowel or consonant.

# 2. Write a program which accepts one number and prints its factors.

# 3. Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.

# 4. Write a program which accepts one number and prints that many numbers starting from 1.

# 5. Write a program which accepts one number and prints that many numbers in reverse order.

def Alpha():
    print()

    Char1 = input("Enter a character : ")
    Char1 = Char1.upper()

    if Char1 in ["A", "E", "I", "O", "U"]:
        print("This character is a vowel")

    else:
        print("This character is a consonant")


def Factors():
    print()

    Num1 = int(input("Enter a number : "))
    FactorsList = []

    for i in range(1,Num1+1):
        if Num1 % i == 0:
            FactorsList.append(i)

    print("Factors of given number are :", FactorsList)


def MathOps():
    print()

    Num1 = int(input("Enter first number : "))
    Num2 = int(input("Enter second number : "))
    print()

    print("Addition of the given numbers is :", Num1 + Num2)
    print("Subtraction of the given numbers is :", Num1 - Num2)
    print("Multiplication of the given numbers is :", Num1 * Num2)
    print("Division of the given numbers is :", Num1 / Num2)

def TillNo():
    print()

    Num1 = int(input("Enter a number : "))
    TillList = []

    for i in range(1,Num1+1):
        TillList.append(i)

    print("The numbers till ", Num1, "are :", TillList)


def FromNo():
    print()

    Num1 = int(input("Enter a number : "))
    FromList = []

    for i in range(Num1,0,-1):
        FromList.append(i)

    print("The numbers from ", Num1, "are :", FromList)


def main():
    # Answer 1
    Alpha()

    # Answer 2
    Factors()

    # Answer 3
    MathOps()

    # Answer 4
    TillNo()

    # Answer 5
    FromNo()


    print()
if __name__ == "__main__":
    main()