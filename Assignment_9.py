# 1. Write a program which contains one function named as Display() that prints "Jay Ganesh" on console.

def Display():
    print("Jay Ganesh")
    print()

# 2. Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.

def ChkGreater():

    print("To check greater number between two numbers")

    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))

    if (No1 > No2):
        # print(No1)
        print("Greater number is :", No1)
        print()

    else:
        # print(No2)
        print("Greater number is :", No2)
        print()

    print("Check Greater Function execution is complete")
    print()

# 3. Write a program which accepts one number and prints square of that number.

def Square():

    print("Execution of Square function starts")

    Num1 = int(input("Enter a number : "))
    print("Square of entered number is :", Num1*Num1)
    print()

    print("Execution of Square function ends")
    print()

# 4. Write a program which accepts one number and prints cube of that number.

def Cube():

    print("Execution of Cube function starts")

    Num1 = int(input("Enter a number : "))
    print("Cube of entered number is :", Num1*Num1*Num1)
    print()

    print("Execution of Cube function ends")
    print()


# 5. Write a program which accepts one number and checks whether it is divisible by 3 and 5.

def Divby3and5():
    Num5 = int(input("Enter a number : "))

    if (Num5 % 3 == 0):
        if(Num5 % 5 == 0):
            print(Num5, "is divisible by 3 and 5")

def main():

    # Answer 1
    Display()

    # Answer 2
    ChkGreater()

    #Answer 3
    Square()

    #Answer 4
    Cube()

    #Answer 5
    Divby3and5()

if __name__ == "__main__":
    main()