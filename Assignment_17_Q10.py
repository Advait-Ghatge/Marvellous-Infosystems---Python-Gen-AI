def main():
    
    print()
    Num1 = input("Enter a number : ")
    print()

    Digits = []

    for i in Num1:
        Digits.append(int(i))

    # print(Digits)

    Sum = 0

    for i in Digits:
        Sum = Sum + i

    print(Sum)

if __name__ == "__main__":
    main()