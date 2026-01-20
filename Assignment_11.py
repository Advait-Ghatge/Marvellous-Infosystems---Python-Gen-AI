# 1. Write a program which accepts one number and checks whether it is prime or not. Input: 11 Output: Prime Number

# 2. Write a program which accepts one number and prints count of digits in that number. Input: 7521 Output: 4

# 3. Write a program which accepts one number and prints sum of digits. Input: 123 Output: 6

# 4. Write a program which accepts one number and prints reverse of that number. Input: 123 Output: 321

# 5. Write a program which accepts one number and checks whether it is palindrome or not. Input: 121 Output: Palindrome


def prime():

    print()
    num1 = int(input("Enter a number to check if it is prime : "))

    for i in range(2,num1):
        if num1 % i == 0:
            return True
            
def CountofDigits():

    print()
    num2 = input("Enter a number whose count of digits you wish to see : ")
    
    print("Total number of digits in", num2, "is:", len(num2))


def SumofDigits():

    print()
    num3 = input("Enter a number whose sum of digits you wish to see : ")
    sum = 0

    for i in range(0, len(num3)):
        sum = sum + int(num3[i])

    print("Sum of Digits for", num3, "is", sum)


def ReverseNum():
    print()
    num = (input("Enter a number whose digits you want reversed : "))

    digits = list(num)
    # print("Before reverse :", digits)

    rev_digits = list()

    for i in range(len(digits)-1, -1, -1):
        rev_digits.append(digits[i])
        i = i-1

    rev_num = int(''.join(rev_digits))

    # print("After reverse :", rev_digits)
    print("Reversed number is :", rev_num)

def NumPal():
    print()
    num = (input("Enter a number to be checked for palindrome : "))

    digits = list(num)

    rev_digits = list()

    for i in range(len(digits)-1, -1, -1):
        rev_digits.append(digits[i])
        i = i-1

    rev_num = int(''.join(rev_digits))

    if digits == rev_digits:
        print("This number is a palindrome :", num)
    
    else:
        print("This number is not a palindrome :", num)

    print()

         
def main():

    # Answer 1
    if prime() == True:
        print("Number is not prime")
    else:
        print("Number is prime")

    # Answer 2
    CountofDigits()

    # Answer 3
    SumofDigits()

    # Answer 4
    ReverseNum()

    # Answer 5
    NumPal()

if __name__ == "__main__":
    main()