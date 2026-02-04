import os

def CountLines(File1):
    
    with open(File1) as f:
        for i,_ in enumerate(f):
            pass
    return i + 1


def WordCount(File1):

    fobj = open(File1, "r")

    Data = fobj.read().split()

    # print(Data)

    CountWords = 0

    for words in Data:

        CountWords = CountWords + 1

    print("Total count of words is :", CountWords)


def DisplayContent(File1):
    
    fobj = open(File1, "r")

    Data = fobj.read()

    print()
    print("Contents of given data are - ")
    print(Data)


def CopyData():

    print()
    File1 = input("Enter name of the source file - ")
    File2 = input("Enter the name of the file where you want the data to be stored - ")

    fobj1 = open(File1, "r")
    Data1 = fobj1.read()

    fobj2 = open(File2, "w")
    Data2 = fobj2.write(Data1)

    print("Data copied from source file to destination")


def SearchWord():

    print()
    File1 = input("Enter name of the file - ")
    Word1 = input("Enter the word you want to search - ")
    

    fobj = open(File1, "r")

    Data = fobj.read().split()

    Count = 0

    for word in Data:

        if word == Word1:
            
            print()
            print("Given word is present in the file")
            Count = Count + 1
            return
        
    if Count == 0:
        print()
        print("Word not found in file")



def main():
    
    print()
    File1 = input("Enter the name of the file : ")

    if os.path.exists(File1) == False:

        print()
        print("Given file does not exist in current directory")
        return

    # Answer 1

    Ans1 = CountLines(File1)

    print()
    print("The number of lines in given document are :", Ans1)

    # Answer 2
    WordCount(File1)

    # Answer 3
    DisplayContent(File1)

    # Answer 4
    CopyData()

    # Answer 5
    SearchWord()


if __name__ == "__main__":
    main()
    print()