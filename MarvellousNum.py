def ChkPrime(Num):
    
    FactorsList = []

    for i in range(2, Num):
        if Num % i == 0:
            FactorsList.append(i)

    if len(FactorsList) == 0:
        # print("Number is prime")
        return True

# ChkPrime(int(input("Enter a number - ")))