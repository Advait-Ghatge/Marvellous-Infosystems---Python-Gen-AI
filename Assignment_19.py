from functools import reduce

def main():
    
    print()




    # Answer 1

    Num1 = int(input("Enter a number : "))
    Square1 = lambda No : No **2
    print("The square of given number is :", Square1(Num1))
    print()




    # Answer 2

    Num2 = int(input("Enter first number : "))
    Num3 = int(input("Enter second number : "))
    Mult1 = lambda No1, No2: No1 * No2
    print()
    print("The multiplication of given numbers is :", Mult1(Num2, Num3))




    # Answer 3

    print()
    NumList1 =[]

    CountElements1 = int(input("How many numbers do you want to store in a list? - "))
    print()

    for i in range(CountElements1):
        Num1 = int(input("Enter number : "))
        NumList1.append(Num1)

    List1 = NumList1
    print("Input List :", List1)

    FData1 = list(filter((lambda Num4 : Num4 >= 70 and Num4 <= 90), List1))
    print("List after filter is:", FData1)

    MData1 = list(map((lambda Num5 : Num5 + 10), FData1))
    print("List after map is :", MData1)

    RData1 = reduce(lambda No1, No2: No1 * No2, MData1)
    print("Output of reduce is :", RData1)

    
    
    
    # Answer 4

    print()
    NumList2 =[]

    CountElements2 = int(input("How many numbers do you want to store in a list? - "))
    print()

    for i in range(CountElements2):
        Num1 = int(input("Enter number : "))
        NumList2.append(Num1)

    List2 = NumList2
    print("Input List :", List2)

    FData2 = list(filter((lambda Num6 : Num6 % 2 == 0), List2))
    print("List after filter is:", FData2)

    MData2 = list(map((lambda Num7 : Num7 * Num7), FData2))
    print("List after map is :", MData2)

    RData2 = reduce((lambda No1, No2: No1 + No2), MData2)
    print("Output of reduce is :", RData2)




    # Answer 5

    def ChkPrime(Num):
        
        FactorsList = []

        for i in range(2, Num):
            if Num % i == 0:
                FactorsList.append(i)

        if len(FactorsList) == 0:
            # print("Number is prime")
            return True
    
    print()
    NumList3 =[]

    CountElements3 = int(input("How many numbers do you want to store in a list? - "))
    print()

    for i in range(CountElements3):
        Num1 = int(input("Enter number : "))
        NumList3.append(Num1)

        
    List3 = NumList3
    print("Input List :", List3)

    FData3 = list(filter((ChkPrime), List3))
    print("List after filter is:", FData3)

    MData3 = list(map((lambda Num9 : Num9 * 2), FData3))
    print("List after map is :", MData3)

    RData3 = reduce(max, MData3)
    print("Output of reduce is :", RData3)


if __name__ == "__main__":
    main()