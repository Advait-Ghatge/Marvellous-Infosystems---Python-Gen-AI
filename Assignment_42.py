import numpy as np
import matplotlib.pyplot as plt

def LinearRegression(X, Y):

    sum = 0
    for i in X:
        sum = sum + i

    X_mean = sum/len(X)

    sum = 0
    for i in Y:
        sum = sum + i

    Y_mean = sum/len(Y)

    numerator = 0
    denominator = 0

    for i in range(len(X)):
        numerator = numerator + ((X[i] - X_mean) * (Y[i] - Y_mean))
        denominator = denominator + ((X[i] - X_mean)**2)

    slope = numerator / denominator

    intercept = Y_mean - (slope * X_mean)

    return X_mean, Y_mean, slope, intercept

def main():
    
    Border = "-" * 45
    
    print()
    print(Border)
    print("Answer 1")
    print(Border)

    ###############
    # Answer 1
    ###############

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    sum = 0
    for i in X:
        sum = sum + i

    print()
    X_mean = sum/len(X)
    print("Mean of X is :", X_mean)

    sum = 0
    for i in Y:
        sum = sum + i

    Y_mean = sum/len(Y)
    print("Mean of Y is :", Y_mean)

    numerator = 0
    denominator = 0

    for i in range(len(X)):
        numerator = numerator + ((X[i] - X_mean) * (Y[i] - Y_mean))
        denominator = denominator + ((X[i] - X_mean)**2)

    slope = numerator / denominator

    print()
    print("Slope is :", slope)

    intercept = Y_mean - (slope * X_mean)

    print("Intercept is :", intercept)

    print()
    print(Border)
    print("Answer 2")
    print(Border)

    ###############
    # Answer 2
    ###############


    Y_pred = []

    for i in range(len(Y)):
        element = (slope * X[i]) + intercept
        Y_pred.append(element)

    print()
    print("Predicted Y-values are :", Y_pred)

    numerator = 0
    denominator = 0

    for i in range(len(Y)):
        numerator = numerator + ((Y_pred[i] - Y_mean)**2)
        denominator = denominator + ((Y[i] - Y_mean)**2)

    R2 = numerator / denominator

    print()
    print("Value of R2 is :", 1 - R2)

    numerator = 0
    denominator = len(Y)

    for i in range(len(Y)):
        numerator = numerator + ((Y[i] - Y_pred[i])**2)

    MSE = numerator / denominator

    print("Value of MSE is :", MSE)


    print()
    print(Border)
    print("Answer 3")
    print(Border)

    ###############
    # Answer 3
    ###############

    X3 = [1,2,3,4,5]
    Y3 = [20000, 25000, 30000, 35000, 40000]

    X_mean3, Y_mean3, slope3, intercept3 = LinearRegression(X3, Y3)

    print()
    print(f"The equation for Q3 is : Y = {slope3} * X + {intercept3}")

    print()
    print("The salary for 6 years of experience is :", (slope3 * 6 + intercept3))

    x3 = np.linspace(1,6,len(X3))
    y3 = (slope3 * x3) + intercept3

    plt.plot(x3, y3, color = 'g', label = "Regression Line")
    plt.scatter(X3, Y3, color = 'r', label = "Scatter Plot")

    plt.xlabel("X : Experience (in years)")
    plt.ylabel("Y : Salary (per month)")
    plt.legend()

    plt.show()

    print()
    print(Border)
    print("Answer 4")
    print(Border)

    ###############
    # Answer 4
    ###############

    print()
    print("KNN is called a lazy learner because it takes a lot of time for testing and does not have any training phase in the traditional sense\n"
    "All calculations are done in the testing phase which makes it very testing-heavy")

    print()
    print(Border)
    print("Answers 5 and 6")
    print(Border)

    ###############
    # Answers 5 and 6
    ###############

    print()
    print("The prediction changes for value of K because the number of neighbouring points varies according to the value of K chosen -\n\nSmall K - Low Bias, High Variance\n"\
    "Large K - High Bias, Low Variance")

    print()
    print(Border)
    print("Answer 7")
    print(Border)

    ###############
    # Answer 7
    ###############

    print()
    print("Smaller the value of MSE, better is the model")

    print()
    print(Border)
    print("Answer 8")
    print(Border)

    ###############
    # Answer 8
    ###############

    print()
    print("MSE predicts how far the predictions are from actual values whereas R2 shows the percentage of variance in Y explained by the model")


    print()
    print(Border)
    print("Answer 9")
    print(Border)

    ###############
    # Answer 9
    ###############

    print()
    print("R2 explains how much variation in Y can be explained by X. R2 = 1 means all the variation is accounted for by X\n"
    "R2 > 1 would imply that model has accuracy more than 100% which is not possible")


    print()
    print(Border)
    print("Answer 10")
    print(Border)

    ###############
    # Answer 10
    ###############

    print()
    print("While K-Nearest Neighbors (KNN) is often taught as a classification algorithm, it works perfectly well for regression.\n" \
    "How it work s: Instead of looking at the most common class among the $k$ neighbors, the algorithm takes the average (or weighted average) of the numerical values of those $k$ neighbors to make a prediction.")

if __name__ == "__main__":
    main()