def main():
    
    print()
    Num1 = int(input("Enter a number : "))
    print()

    for i in range(1, Num1 + 1):
        
        for j in range(1, i + 1):

            print(j, end = " ")

        print()
if __name__ == "__main__":
    main()