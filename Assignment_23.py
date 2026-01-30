# Answer 1

class BookStore:

    NoOfBooks = 0

    def __init__(self, Name, Author):
        
        self.value1 = Name
        self.value2 = Author
        BookStore.NoOfBooks = BookStore.NoOfBooks+1

    def Display(self):
        print(f"{self.value1} by {self.value2}; No of books =", BookStore.NoOfBooks)

Obj1 = BookStore("Book 1", "Anuj 1")
Obj1.Display()


Obj2 = BookStore("Book 2", "Anuj 2")
Obj2.Display()


Obj3 = BookStore("Book 3", "Anuj 3")
Obj3.Display()



# Answer 2

class BankAccount:

    ROI = 10.5

    def __init__(self, Name, Amount):
        
        self.value1 = Name
        self.value2 = int(Amount)

    def Display(self):

        print()
        print("Account holder's Name is :", self.value1)
        print("Account holder's Balance is :", self.value2)

    def Deposit(self):

        print()
        DAmount = int(input("Enter Deposit Amount : "))
        self.value2 = self.value2 + DAmount
        print("Total amount is :", self.value2)


    def Withdraw(self):

        print()
        WAmount = int(input("Enter Withdrawal Amount : "))

        if WAmount > int(self.value2):
            print()
            print("Insufficient funds")

        else:
            print()
            print("Amount Withdrawn =", WAmount)
            print("Remaining balance is :", self.value2 - WAmount)


    def CalculateInterest(self):

        Interest = (self.value2 * BankAccount.ROI) / 100
        print()
        print("Interest is :", Interest)


Obj1 = BankAccount("Advait", "10000")

Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw() 
Obj1.CalculateInterest()
print()


# Answer 3

class Numbers:

    FactorsList = []

    def __init__(self, Value = 0):
        
        print()
        Value = int(input("Enter a number : "))
        self.value1 = Value


    def Factors(self):

        Numbers.FactorsList = []

        for i in range(2, self.value1):
            if self.value1 % i == 0:
                Numbers.FactorsList.append(i)

        print()
        print("Factors of given number are :", Numbers.FactorsList)


    def ChkPrime(self):

        Numbers.FactorsList = []

        for i in range(2, self.value1):
            if self.value1 % i == 0:
                Numbers.FactorsList.append(i)

        if ((len(Numbers.FactorsList)) == 0):
            
            print()
            print("Number is prime")

        else:
            
            print()
            print("Number is not prime")


    def SumFactors(self):

        Numbers.FactorsList = []

        for i in range(1, self.value1):
            if self.value1 % i == 0:
                Numbers.FactorsList.append(i)

        SumFactors1 = 0

        for i in range(0, len(Numbers.FactorsList)):
            SumFactors1 = int(Numbers.FactorsList[i]) + SumFactors1

        print()
        print("Sum of factors for given number is :", SumFactors1)


    def ChkPerfect(self):

        Numbers.FactorsList = []

        for i in range(1, self.value1):
            if self.value1 % i == 0:
                Numbers.FactorsList.append(i)

        SumFactors1 = 0

        for i in range(0, len(Numbers.FactorsList)):
            SumFactors1 = int(Numbers.FactorsList[i]) + SumFactors1

        # print()
        # print("Sum of factors for given number is :", SumFactors1)
        
        if self.value1 == SumFactors1:
            print()
            print("Number is perfect")

        else:
            print()
            print("Number is not perfect")


Obj1 = Numbers()

Obj1.Factors()
Obj1.ChkPrime()
Obj1.SumFactors()
Obj1.ChkPerfect()

print()