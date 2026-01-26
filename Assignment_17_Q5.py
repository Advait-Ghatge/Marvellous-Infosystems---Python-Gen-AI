def main():
    
    print()
    No1 = int(input("Enter a number : "))
    print()

    FactorsCount = []

    for i in range(2, No1):

        if No1 % i == 0 :
            FactorsCount.append(i)

        i = i + 1

    if len(FactorsCount) == 0:
        print("It is prime number")

    else:
        print("It is not a prime number")

if __name__ == "__main__":
    main()