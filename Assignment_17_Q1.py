from Arithmetic import Add, Sub, Mult, Div

def main():
    print()

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Add(No1, No2)
    Sub(No1, No2)
    Mult(No1, No2)
    Div(No1, No2)


if __name__ == "__main__":
    main()