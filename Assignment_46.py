from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

Border = "-" * 40

# Answer 1

print()
print(Border)
print("Answer 1")
print(Border)

print("\nCoefficient is the rate of change of the dependent variable when there is unit change in the value of the independent variable.")
print("For example : Let's assume the following equation - Value of car (Y) = Horsepower (X) * 10 + 5000.\nHere, when the power of car increases by 1 horsepower, it's value increases by 10 times.")

# Answer 2

print()
print(Border)
print("Answer 2")
print(Border)

print("\nCoefficient is 8.")
print("Intercept is 15.")
print("The value of coefficient is 8 which means that for every unit change in X, the value of Y increases 8 times.")

# Answer 3

print()
print(Border)
print("Answer 3")
print(Border)

print("\nCoefficient is 6. This means that for every hour student studies, his/her marks increase by 6.")
print("Intercept is 40. This means that even if the student does not study (Study Hours = 0), he/she will still get 40 marks.")

# Answer 4

print()
print(Border)
print("Answer 4")
print(Border)
print()

Salary = []
Experience = [2,5,7]

for i in Experience:

    # Salary = 12 * Experience + 25
    Salary_i = 12 * i + 25

    Salary.append(Salary_i)

for i in range(3):

    print(f"Experience : {Experience[i]}\tSalary : {Salary[i]}")

# Answer 5

print()
print(Border)
print("Answer 5")
print(Border)

print("\nNegative coefficient indicates that the value of Y decreases when the value of X increases.")
print("Y decreases by 3 when X increases by 1.")
print(f"Value of Y when X = 4 is : {(-3 * 4) + 20}")

# Answer 6

print()
print(Border)
print("Answer 6")
print(Border)

print("\nSize : When the size of house increases by 1 unit, the price of the house increases by 3,000.")
print("Bedrooms : When the number of bedrooms in the house increase by 1, the price of the house increases by 40,000.")
print("The number of bedrooms of a house has a larger impact on its price as compared to its size.")

# Answer 7

print()
print(Border)
print("Answer 7")
print(Border)

Study_Hours = np.array([1,2,3,4,5]).reshape(-1,1)
Marks = [50,55,60,65,70]

Model = LinearRegression()

Model.fit(Study_Hours, Marks)

print("\nCoefficient is :", Model.coef_)
print("Intercept is :", Model.intercept_)

# Answer 8

print()
print(Border)
print("Answer 8")
print(Border)

X_test = np.array(6).reshape(-1,1)
print("\nMarks for 6 study hours are :", Model.predict(X_test))

# Answer 9

print()
print(Border)
print("Answer 9")
print(Border)

Sleep_Hours = np.array([7,6,7,6,8]).reshape(-1,1)

Features = np.concatenate([Study_Hours, Sleep_Hours], axis=1)
Feature_Names = ['Study_Hours', 'Sleep_Hours']
# print(Features)

Model.fit(Features, Marks)

Coefficients = pd.DataFrame(Model.coef_, index=Feature_Names, columns=['Coefficients'])

print("\nCoefficients are :\n\n", Coefficients)
print("\nIntercept is :", Model.intercept_)

# Answer 10

print()
print(Border)
print("Answer 10")
print(Border)

print("\nFeatures are important in Regression Models because they tell us how the dependent variable is affected by changes in the independent variable.")
print("If the value of a coefficient is very low, we can remove that particular independent variable from the dataset to increase model accuracy or vice-versa.")