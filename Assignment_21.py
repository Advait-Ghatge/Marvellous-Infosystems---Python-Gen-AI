import threading

counter = 1
lockobj = threading.Lock()

def Update1():

    global counter

    for _ in range(20000000):
        with lockobj:
            counter = counter + 1

def PrimeNums(List1):

    PrimeList1 = []
    FactorsList =[]

    for Num in List1:

        for i in range(2, Num):
            if Num % i == 0:
                FactorsList.append(i)

        if len(FactorsList) == 0:
            # print("Number is prime")
            PrimeList1.append(Num)

        FactorsList.clear()
    
    print("The prime numbers from given list are :", PrimeList1)



def NotPrime(List1):

    NonPrimeList1 = []
    FactorsList =[]

    for Num in List1:

        for i in range(2, Num):
            if Num % i == 0:
                FactorsList.append(i)

        if len(FactorsList) != 0:
            # print("Number is prime")
            NonPrimeList1.append(Num)

        FactorsList.clear()
    
    print("The non-prime numbers from given list are :", NonPrimeList1)


def MaxList(List1):

    print("The maximum number from given list is :", max(List1))


def MinList(List1):

    print("The minimum number from given list is :", min(List1))


def SumList(List1):

    Sum = 0

    for i in List1:
        Sum = Sum + i

    return Sum


def ProductList(List1):

    Product = 1

    for i in List1:
        Product = Product * i

    return Product      
    

def main():

    # Answer 1

    IntList = []

    print()
    Num1 = int(input("How many items do you want in list? - "))
    print()

    for i in range(0, Num1):
        i = int(input("Enter a number : "))
        IntList.append(i)

    print()

    t11 = threading.Thread(target=PrimeNums, name="Prime", args=(IntList,))
    t12 = threading.Thread(target=NotPrime, name="NonPrime", args = (IntList,))

    t11.start()
    t11.join()
    print()

    t12.start()
    t12.join()
    print()

    # Answer 2

    t21 = threading.Thread(target=MaxList, args=(IntList,))
    t22 = threading.Thread(target=MinList, args=(IntList,))

    t21.start()
    t21.join()
    print()

    t22.start()
    t22.join()


    # Answer 4

    t41 = threading.Thread(target=SumList, args=(IntList,))
    t42 = threading.Thread(target=ProductList, args=(IntList,))

    t41.start()
    print()
    print("The sum of elements from given list is :", SumList(IntList))
    t41.join()

    t42.start()
    print()
    print("The product of elements from given list is :", ProductList(IntList))
    t42.join()


    # Answer 3

    t31 = threading.Thread(target=Update1)
    t32 = threading.Thread(target=Update1)
    t33 = threading.Thread(target=Update1)

    t31.start()
    t32.start()
    t33.start()

    t31.join()
    t32.join()
    t33.join()

    print()
    print("Value of counter is :", counter)
    

if __name__ == "__main__":
    main()