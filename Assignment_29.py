import os
import sys
import hashlib

def FileExists(File1):

    FileList = []

    if os.path.exists(File1) == False:
        # print()
        print("Given file does not exist in current directory")

    else:

        # print()
        print("Given file is present in current directory")


def OpenFile(File1):

    fobj = open(File1, "r")

    Data = fobj.read()

    print()
    print("Data from given file is :", Data)


def NewFileCreate():

    if len(sys.argv) != 2:

        print()
        print("Insufficient number of command line arguments for Q3")

    if (os.path.exists(sys.argv[1])) == False:

        print()
        print("File does not exist")

    else:

        # print()
        # print("File exists!")

        FileName1 = sys.argv[1]

        Obj1 = open(FileName1, "r")
        Data1 = Obj1.read()

        NewObj = open("DemoQ3.txt", "w")
        NewObj.write(Data1)

        print("New File is created by the name of DemoQ3.txt")


def CalculateCheckSum(File1):

    fobj = open(File1, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while (len(Buffer) > 0):

        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()


def Compare2Files():

    if (len(sys.argv) != 3):

        print()
        print("Insufficient number of command line arguments to compare two files i.e. Q4")
        print()
        return

    File1 = sys.argv[1]
    File2 = sys.argv[2]

    ChkSum1 = CalculateCheckSum(File1)
    ChkSum2 = CalculateCheckSum(File2)

    #print(ChkSum1)
    #print(ChkSum2)

    if ChkSum1 == ChkSum2:
        print()
        print("Success")

    else:
        print()
        print("Failure")


def StringFrequency(File1 = "Demo.txt", Str1 = "Advait"):

    if os.path.exists(File1) == False:

        print()
        print("There exists no such file")
        print()
        return
    
    fobj1 = open(File1, "r")

    Data = fobj1.read().split()
    # print()
    # print(Data)

    Count = 0

    for word in Data:

        if word == Str1:
            Count = Count + 1

    print()
    print("The count of given string in specified file is -", Count)


def main():

    print()
    File1 = input("Enter the name of the file : ")

    # Answer 1
    FileExists(File1)

    # Answer 2
    OpenFile(File1)

    # Answer 3
    NewFileCreate()

    # Answer 4
    Compare2Files()

    # Answer 5
    print()
    File1 = input("Enter file name - ")
    Str1 = input("Enter the word whose frequency you want to know - ")

    StringFrequency(File1, Str1)
    print()


if __name__ == "__main__":
    main()