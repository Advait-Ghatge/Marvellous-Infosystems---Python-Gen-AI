def fun():
    
    No = int(input("Enter a number : "))

    if No > 0:
        print("Positive Number")
    
    elif No == 0:
        print("Zero")

    else:
        print("Negative Number")

def main():
    print()

    fun()

if __name__ == "__main__":
    main()