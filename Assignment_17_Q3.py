def main():

    print()
    No1 = int(input("Enter a number : "))
    print()

    fact = 1

    for i in range(1, No1+1):
        fact = fact * i
        i = i + 1

    print(fact)

if __name__ == "__main__":
    main()