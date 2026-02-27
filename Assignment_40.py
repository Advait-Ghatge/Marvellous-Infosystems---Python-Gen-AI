import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import (
    accuracy_score
)

def main():
    
    Border = "-" * 40

    print()
    print(Border)
    print("Student Performance ML - Assignment 40")
    print(Border)

    ########################################
    # Basic Framework of ML
    ########################################

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    print("Dataset loaded successfully!")

    Features_Cols = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]

    X = df[Features_Cols]
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size = 0.2,
        random_state = 42
    )

    Model1 = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = 3,
        random_state = 42
    )

    Model1.fit(X_train, Y_train)

    Y_pred1 = Model1.predict(X_test)

    print()
    print("Model 1 Evaluation started - ")

    print()
    print("Predicted Answers v/s Actual Answers : ")
    res = "\n".join("{} {}".format(predicted, actual) for predicted, actual in zip(Y_pred1, Y_test))
    print(res)

    ########################################
    # Answer 1
    ########################################

    print()
    # print(zip(X.columns, Model1.feature_importances_))

    FeatureImp = Model1.feature_importances_

    for i,v in enumerate(FeatureImp) :
        print(f"Feature : {i}, Score : {v : .5f}")
    
    print()
    plt.bar([x for x in range(len(FeatureImp))], FeatureImp)
    plt.show()

    print("The feature - Attendance - contributes the most in predicting Final Result")

    print()
    print("The rest of the features contribute the least")

    print()
    print(Border)

    ########################################
    # Answer 2
    ########################################

    print()
    print("Training the model without 'StudyHours'...")

    Features_Cols2 = [
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]

    X2 = df[Features_Cols2]
    Y2 = df["FinalResult"]

    X_train2, X_test2, Y_train2, Y_test2 = train_test_split(
        X2,
        Y2,
        test_size = 0.2,
        random_state = 42
    )

    Model2 = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = 3,
        random_state = 42
    )

    Model2.fit(X_train2, Y_train2)

    Y_pred2 = Model2.predict(X_test2)

    print()
    print("Model is trained without 'StudyHours'")

    accuracy1 = accuracy_score(Y_pred1, Y_test)

    print()
    print(f"Accuracy of Model 1 (with StudyHours) is : {accuracy1 * 100}%")


    accuracy2 = accuracy_score(Y_pred2, Y_test2)

    print()
    print(f"Accuracy of Model 2 (without StudyHours) is : {accuracy2 * 100}%")

    print()
    print("Conclusion - Removing 'StudyHours' does not affect performance of the model")

    print()
    print(Border)

    ########################################
    # Answer 3
    ########################################

    print()
    print("Training the model with 'StudyHours' and 'Attendance' only...")

    Features_Cols3 = [
        "StudyHours",
        "Attendance"
    ]

    X3 = df[Features_Cols3]
    Y3 = df["FinalResult"]

    X_train3, X_test3, Y_train3, Y_test3 = train_test_split(
        X3,
        Y3,
        test_size = 0.2,
        random_state = 42
    )

    Model3 = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = 3,
        random_state = 42
    )

    Model3.fit(X_train3, Y_train3)

    Y_pred3 = Model3.predict(X_test3)

    print()
    print("Model is trained with 'StudyHours' and 'Attendance' only")

    accuracy1 = accuracy_score(Y_pred1, Y_test)

    print()
    print(f"Accuracy of Model 1 (with StudyHours) is : {accuracy1 * 100}%")


    accuracy2 = accuracy_score(Y_pred2, Y_test2)

    print()
    print(f"Accuracy of Model 2 (without StudyHours) is : {accuracy2 * 100}%")

    accuracy3 = accuracy_score(Y_pred3, Y_test3)

    print()
    print(f"Accuracy of Model 3 (with StudyHours and Attendance only) is : {accuracy3 * 100}%")

    print()
    print(Border)

    ########################################
    # Answer 4
    ########################################

    input_data = pd.DataFrame([{"StudyHours": 6, "Attendance": 45, "PreviousScore": 66, "AssignmentsCompleted": 7, "SleepHours": 7},
                               {"StudyHours": 7, "Attendance": 55, "PreviousScore": 76, "AssignmentsCompleted": 8, "SleepHours": 6},
                               {"StudyHours": 8, "Attendance": 85, "PreviousScore": 86, "AssignmentsCompleted": 8, "SleepHours": 8},
                               {"StudyHours": 8, "Attendance": 75, "PreviousScore": 96, "AssignmentsCompleted": 8, "SleepHours": 7.5},
                               {"StudyHours": 4, "Attendance": 85, "PreviousScore": 56, "AssignmentsCompleted": 7, "SleepHours": 8}])

    Y_ud = Model1.predict(input_data)

    print()
    print("Results for user-defined data is :", Y_ud)

    print()
    print(Border)

    ########################################
    # Answer 5
    ########################################

    print()
    print("Predicted Answers v/s Actual Answers for Training Model (with all features): ")
    res = "\n".join("{} {}".format(predicted, actual) for predicted, actual in zip(Y_pred1, Y_test))
    print(res)

    count_correct = 0
    total = 0

    for predicted, actual in zip(Y_pred1, Y_test):
        if predicted == actual:
            count_correct = count_correct + 1
            total = total + 1
        else:
            total = total + 1

    print()
    print(f"Accuracy of Model (manually calculated) is : {count_correct * 100/total}%%")

    accuracy5 = accuracy_score(Y_pred1, Y_test)

    print()
    print(f"Accuracy of Model (with accuracy_score) is : {accuracy5 * 100}%")
    
    print()
    print(Border)

    ########################################
    # Answer 6
    ########################################

    print()
    print("Predicted Answers v/s Actual Answers for Training Model (with all features): ")
    res = "\n".join("{} {}".format(predicted, actual) for predicted, actual in zip(Y_pred1, Y_test))
    print(res)

    print()
    print("None of the students were misclassified")

    print()
    print(Border)

    ########################################
    # Answer 7
    ########################################

    Model71 = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = 3,
        random_state = 0
    )

    Model71.fit(X_train, Y_train)
    
    print()
    print("Model 7.1 Training Completed!")

    Model72 = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = 3,
        random_state = 10
    )

    Model72.fit(X_train, Y_train)
    
    print()
    print("Model 7.2 Training Completed!")

    Model73 = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = 3,
        random_state = 42
    )

    Model73.fit(X_train, Y_train)

    print()
    print("Model 7.3 Training Completed!")

    Y_pred71 = Model71.predict(X_test)

    accuracy71 = accuracy_score(Y_pred71, Y_test)

    print()
    print(f"Accuracy of Model 7.1 is : {accuracy71 * 100}%")

    Y_pred72 = Model72.predict(X_test)

    accuracy72 = accuracy_score(Y_pred72, Y_test)

    print()
    print(f"Accuracy of Model 7.2 is : {accuracy72 * 100}%")

    Y_pred73 = Model73.predict(X_test)

    accuracy73 = accuracy_score(Y_pred73, Y_test)

    print()
    print(f"Accuracy of Model 7.3 is : {accuracy73 * 100}%")

    print()
    print("Conclusion - The results are not dependent on random state")

    print()
    print(Border)

    ########################################
    # Answer 8
    ########################################

    plot_tree(Model1)
    plt.show()

    print()
    print("The feature - Attendance - appears at the root node")
    print("This feature was selected because it contributes the most to the prediction (Final Result)")

    print()
    print(Border)

    ########################################
    # Answer 9
    ########################################

    PI_List = []

    for i, j in zip(df["StudyHours"], df["Attendance"]):
        item9 = (i*2) + j
        PI_List.append(item9)
    
    print()
    print("Performance Index is :", PI_List)
    
    Dataset2 = pd.DataFrame({"PerformanceIndex" : PI_List})

    Features_Cols = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]

    X9 = df[Features_Cols].join(Dataset2)
    Y9 = df["FinalResult"]

    X_train9, X_test9, Y_train9, Y_test9 = train_test_split(
        X9,
        Y9,
        test_size = 0.2,
        random_state = 42
    )

    Model9 = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = 3,
        random_state = 42
    )

    Model9.fit(X_train9, Y_train9)

    Y_pred9 = Model9.predict(X_test9)

    accuracy9 = accuracy_score(Y_pred9, Y_test9)

    print()
    print(f"Accuracy of Model with Performance Index is : {accuracy9 * 100}%")
    print("Accuracy stays the same")

    print()
    print(Border)

    ########################################
    # Answer 10
    ########################################


    X10 = df[Features_Cols]
    Y10 = df["FinalResult"]

    X_train10, X_test10, Y_train10, Y_test10 = train_test_split(
        X10,
        Y10,
        test_size = 0.2,
        random_state = 42
    )

    Model10 = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = None,
        random_state = 42
    )

    Model10.fit(X_train10, Y_train10)

    Y_pred101 = Model10.predict(X_test10)

    accuracy101 = accuracy_score(Y_pred101, Y_test10)

    print()
    print(f"Testing Accuracy of Model with max_depth = None is : {accuracy101 * 100}%")

    Y_pred102 = Model10.predict(X_train10)

    accuracy102 = accuracy_score(Y_pred102, Y_train10)

    print()
    print(f"Training Accuracy of Model with max_depth = None is : {accuracy102 * 100}%")

    print()
    print("If training accuracy is more than testing accuracy, the model suffers from overfitting")


if __name__ == "__main__":
    main()