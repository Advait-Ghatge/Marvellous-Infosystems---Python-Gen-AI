# Answer 1

class Demo:

    def __init__(self,no1,no2):
        self.value1 = no1
        self.value2 = no2

    def fun(self):
        print("The values of first and second numbers in fun() are", self.value1 ,"and", self.value2, "respectively")

    
    def gun(self):
        print("The values of first and second numbers in gun() are", self.value1 ,"and", self.value2, "respectively")

Obj1 = Demo(11,21)
Obj2 = Demo(51,101)

Obj1.fun()
Obj2.fun()

Obj1.gun()
Obj2.gun()



# Answer 2

class Circle:

    PI = 3.14

    def __init__(self, radius = 0, area = 0, circumference = 0):
        self.value1 = radius
        self.value2 = area
        self.value3 = circumference
    
    def Accept(self):
        radius = int(input("Enter radius : "))
        print("Radius is : ", radius)
        print()
        return radius

    def CalculateArea(self):
        Obj1 = Circle()
        radius = Obj1.Accept()
        PI2 = Obj1.PI
        area = PI2 * radius * radius
        print("Area is : ", area)
        print()

    def CalculateCircumference(self):
        Obj1 = Circle()
        radius = Obj1.Accept()
        PI2 = Obj1.PI
        circumference = PI2 * radius * 2
        print("Circumference is : ", circumference)
        print()

Obj1 = Circle()
print()

Obj1.CalculateArea()
Obj1.CalculateCircumference()

    
# Answer 3

class Arithmetic:

    def __init__(self, Num1 = 0, Num2 = 0):
        self.value1 = Num1
        self.value2 = Num2

    def Accept(self):
        Num1 = int(input("Enter first number : "))
        Num2 = int(input("Enter second number : "))
        print()
        print("First number is :", Num1)
        print("Second number is :", Num2)
        print()
        return Num1, Num2

    def Addition(self):
        Obj1 = Arithmetic()
        Num1, Num2 = Obj1.Accept()
        Ans = 0
        Ans = Num1 + Num2
        print("Addition is :", Ans)
        print()


    def Subtraction(self):
        Obj1 = Arithmetic()
        Num1, Num2 = Obj1.Accept()
        Ans = 0
        Ans = Num1 - Num2
        print("Subtraction is :", Ans)
        print()


    def Multiplication(self):
        Obj1 = Arithmetic()
        Num1, Num2 = Obj1.Accept()
        Ans = 0
        Ans = Num1 * Num2
        print("Multiplication is :", Ans)
        print()


    def Division(self):
        Obj1 = Arithmetic()
        Num1, Num2 = Obj1.Accept()
        Ans = 0
        Ans = Num1 / Num2
        print("Division is :", Ans)
        print()

Obj1 = Arithmetic()
print()

Obj1.Addition()
Obj1.Subtraction()
Obj1.Multiplication()
Obj1.Division()