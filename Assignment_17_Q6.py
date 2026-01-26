def main():
    
    print()
    No1 = int(input("Enter a number : "))
    print()

    for i in range(No1, 0, -1):
        print(" * " * i)
        i = i - 1

if __name__ == "__main__":
    main()