# 1. Write a program which accepts length and width of rectangle and prints area.

# 2. Write a program which accepts radius of circle and prints area of circle.

# 3. Write a program which accepts one number and checks whether it is perfect number or not.

# 4. Write a program which accepts one number and prints binary equivalent.

# 5. Write a program which accepts marks and displays grade.


def AreaRect():
    print()

    Length1 = int(input("Enter length of rectangle : "))
    Breadth1 = int(input("Enter breadth of rectangle : "))

    print("Area of rectangle is :", Length1 * Breadth1)

def AreaCircle():
    print()

    Rad1 = int(input("Enter radius of circle : "))

    print("Area of circle is :", 3.14*Rad1*Rad1)

def PerfectNum():
    print()

    Num1 = int(input("Enter a number : "))
    FactorsList = []

    for i in range(1, Num1):
        if Num1 % i == 0:
            FactorsList.append(i)
        i = i+1

    print("The list of Factors is :", FactorsList)
    print()

    Sum = 0

    for i in range(0, len(FactorsList)):
        Sum = Sum + FactorsList[i]

    print("The Sum of Factors is :", Sum)
    print()

    if Sum == Num1:
        print("The given number i.e.", Num1, "is a perfect number")
    
    else:
        print("The given number i.e.", Num1, "is not a perfect number")

def ToBinary():
    
    print()
    num1 = int(input("Enter a number : "))

    list1 = []
    list2 = [1]

    i = 1

    while num1 > i:
        if num1 % 2 == 0:
            list1.append(0)
        else:
            list1.append(1)
        num1 = int(num1/2)

    for i in range(len(list1)-1, -1, -1):
        list2.append(list1[i])

    print("The given number in binary is :",''.join(str(i) for i in list2))

def Grade():

    print()

    Marks = input("Enter marks scored : ")
    Marks = int(Marks)

    if Marks >= 75:
        print("Scored class is Distinction")

    elif (Marks >= 60 & Marks < 75):
        print("Scored class is First Class")

    elif (Marks >= 50 & Marks < 60):
        print("Scored class is Second Class")

    else :
        print("Student has failed")

def main():

    # Answer 1
    AreaRect()

    # Answer 2
    AreaCircle()

    # Answer 3
    PerfectNum()

    # Answer 4
    ToBinary()

    # Answer 5
    Grade()

if __name__ == "__main__":
    print()
    main()
    print()