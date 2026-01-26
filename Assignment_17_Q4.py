def main():
    
    print()
    No1 = int(input("Enter a number : "))
    print()

    FactorsAdd = 0

    for i in range(1, No1):
        if No1 % i == 0:
            FactorsAdd = FactorsAdd + i

    print(FactorsAdd)

if __name__ == "__main__":
    main()