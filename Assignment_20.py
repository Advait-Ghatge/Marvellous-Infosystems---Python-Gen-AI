import threading

# Answer 1

def Even():

    ListEven = []
    count = 0
    i = 1

    while count < 10:
        if i % 2 == 0:
            ListEven.append(i)
            count = count + 1
        i = i + 1

    print(ListEven)

# Answer 1

def Odd():

    ListOdd = []
    count = 0
    i = 1

    while count < 10:
        if i % 2 != 0:
            ListOdd.append(i)
            count = count + 1
        i = i + 1

    print(ListOdd)



# Answer 2

def EvenFactors(No1):

    EvenFactorsList = []

    for i in range(1, No1):
        if No1 % i == 0:
            if i % 2 == 0:
                EvenFactorsList.append(i)
        i = i + 1

    print("Even factors of given number are :", EvenFactorsList)

    Sum = 0

    for i in EvenFactorsList:
        Sum = Sum + i
    
    print("Sum of Even Factors is :", Sum)

# Answer 2

def OddFactors(No1):

    OddFactorsList = []

    for i in range(1, No1):
        if No1 % i == 0:
            if i % 2 != 0:
                OddFactorsList.append(i)
        i = i + 1

    print("Odd factors of given number are :", OddFactorsList)

    Sum = 0

    for i in OddFactorsList:
        Sum = Sum + i
    
    print("Sum of Odd Factors is :", Sum)



# Answer 3

def EvenList(List1):
    
    EvenFromList = []
    
    for i in List1:
        if i % 2 == 0:
            EvenFromList.append(i)

    Sum = 0

    for i in EvenFromList:
        Sum = Sum + i

    print("Sum of even numbers from list is", Sum)

def OddList(List1):
    
    OddFromList = []
    
    for i in List1:
        if i % 2 != 0:
            OddFromList.append(i)

    Sum = 0

    for i in OddFromList:
        Sum = Sum + i

    print("Sum of odd numbers from list is", Sum)



    # Answer 4

def UpperCaseChar(Str1):
    
    CharList = []

    UpperCharList = []

    for i in Str1:

        CharList.append(i)

    for i in CharList:
        
        if i.isdigit() == False:
        
            if i.upper() == i:
                UpperCharList.append(i)


    print("List of uppercase characters is :", UpperCharList)
    print("Thread ID of Upper Case Char is :", threading.get_ident())


def LowerCaseChar(Str1):
    
    CharList = []

    LowerCharList = []

    for i in Str1:

        CharList.append(i)

    for i in CharList:

        if i.isdigit() == False:
            
            if i.lower() == i:
                LowerCharList.append(i)


    print("List of lowercase characters is :", LowerCharList)
    print("Thread ID of Lower Case Char is :", threading.get_ident())


def DigitsinChar(Str1):
    
    CharList = []

    DigitsList = []

    for i in Str1:

        CharList.append(i)

    for i in CharList:

        if i.isdigit() == True:
            DigitsList.append(i)

    print("List of Digits is :", DigitsList)
    print("Thread ID of Digits in Char is :", threading.get_ident())


def OneFifty():

    AscList = []
        
    for i in range(1,51):
        AscList.append(i)

    print(AscList)
    

def FiftyOne():

    DescList = []

    for i in range(50,0,-1):
        DescList.append(i)

    print()
    print(DescList)


def main():

    # Answer 1
    
    t11 = threading.Thread(target=Even, name="Even")
    t12 = threading.Thread(target=Odd, name="Odd")

    t11.start()
    t12.start()

    t11.join()
    t12.join()

    # Answer 2
    
    print()
    Num1 = int(input("Enter a number : "))

    t21 = threading.Thread(target=EvenFactors, args=(Num1,), name="EvenFactor")
    t22 = threading.Thread(target=OddFactors, args=(Num1,), name="OddFactor")

    t21.start()
    t22.start()
    
    t21.join()
    t22.join()

    print("Exit from main")

    
    # Answer 3
    
    IntList = []

    print()
    IntLen = int(input("How many elements do you want the list to have? - "))

    for i in range(IntLen):

        Num1 = int(input("Enter a number : "))
        IntList.append(Num1)

    t31 = threading.Thread(target=EvenList, args = (IntList,), name="EvenList")
    t32 = threading.Thread(target=OddList, args = (IntList,), name="OddList")

    t31.start()
    t32.start()

    t31.join()
    t32.join()


    
    # Answer 4

    print()
    Text1 = input("Enter a string : ")
    print()

    t41 = threading.Thread(target=UpperCaseChar, args=(Text1,), name="Capital")
    t42 = threading.Thread(target=LowerCaseChar, args=(Text1,), name="Small")
    t43 = threading.Thread(target=DigitsinChar, args=(Text1,), name="Digits")

    print(f"Name of threads are : {t41.name}, {t42.name}, {t43.name}")

    t41.start()
    t42.start()
    t43.start()

    t41.join()
    t42.join()
    t43.join()

    

    # Answer 5

    print()
    t51 = threading.Thread(target=OneFifty, name="Thread1")
    t52 = threading.Thread(target=FiftyOne, name="Thread2")

    t51.start()
    t51.join()

    t52.start()
    t52.join()

if __name__ == "__main__":
    main() 