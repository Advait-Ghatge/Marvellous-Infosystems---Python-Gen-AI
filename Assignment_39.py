import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

def main():
    
    Border = "-" * 60

    print()
    print(Border)
    print("Step 1 : Dataset Loading")
    print(Border)

    ########################################
    # Step 1 : Dataset Loading
    ########################################

    print()

    Dataset = "student_performance_ml.csv"

    df = pd.read_csv(Dataset)

    print("Dataset loaded successfully!")

    print()
    print("Initial entries from the dataset are : ")
    print(df.head(5))

    print()
    print(Border)
    print("Step 2 : Data Analysis")
    print(Border)

    ########################################
    # Step 2 : Data Analysis
    ########################################

    print()
    print("Shape of Dataset is :", df.shape)

    print()
    print("Column Names are :", list(df.columns))

    print()
    print("Missing Values (per column) : ")
    print(df.isnull().sum())

    print()
    print(Border)
    print("Step 3 : Visualization")
    print(Border)

    ########################################
    # Step 3 : Visualization
    ########################################

    Features_Cols = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]

    X = df[Features_Cols]
    Y = df["FinalResult"]

    print()
    print("This is the boxplot for column - StudyHours")

    sns.boxplot(x = df["StudyHours"])
    plt.show()

    print()
    print("This is the scatter plot for columns - Attendance v/s Final Result")

    for result in df["FinalResult"].unique():
        temp = df[df["FinalResult"] == result]
        plt.scatter(temp["Attendance"], temp["FinalResult"], label = result)

    plt.title("Student Performance : Attendance v/s Final Result")

    plt.xlabel("Attendance")
    plt.ylabel("Final Result")

    plt.grid(True)
    plt.legend()
    plt.show()

    print()
    print(Border)
    print("Step 4 : Train-Test Split")
    print(Border)

    ########################################
    # Step 4 : Train-Test Split
    ########################################

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size = 0.2,
        random_state = 42
    )

    print()
    print("Data Splitting Activity Completed. The data has been split into the following - ")
    print("X_train :", X_train.shape)
    print("X_test :", X_test.shape)
    print("Y_train :", Y_train.shape)
    print("Y_test :", Y_test.shape)

    print()
    print(Border)
    print("Step 5 : Model Training")
    print(Border)

    ########################################
    # Step 5 : Model Training
    # Answer 1
    # Answer 6
    ########################################

    print()
    print("We are using the model - Decision Tree Classifier")

    Model1 = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = 1,
        random_state = 42
    )

    Model1.fit(X_train, Y_train)
    
    print()
    print("Model 1 Training Completed!")

    Model2 = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = 3,
        random_state = 42
    )

    Model2.fit(X_train, Y_train)
    
    print()
    print("Model 2 Training Completed!")

    Model3 = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = None,
        random_state = 42
    )

    Model3.fit(X_train, Y_train)

    print()
    print("Model 3 Training Completed!")

    print()
    print(Border)
    print("Step 6 : Prediction")
    print(Border)

    ########################################
    # Step 6 : Prediction
    # Answer 2
    ########################################

    Y_pred1 = Model1.predict(X_test)

    print()
    print("Model 1 Evaluation started - ")

    print()
    print("Predicted Answers v/s Actual Answers : ")
    res = "\n".join("{} {}".format(predicted, actual) for predicted, actual in zip(Y_pred1, Y_test))
    print(res)

    Y_pred2 = Model2.predict(X_test)

    print()
    print("Model 2 Evaluation started - ")

    print()
    print("Predicted Answers v/s Actual Answers : ")
    res = "\n".join("{} {}".format(predicted, actual) for predicted, actual in zip(Y_pred2, Y_test))
    print(res)

    Y_pred3 = Model3.predict(X_test)

    print()
    print("Model 3 Evaluation started - ")

    print()
    print("Predicted Answers v/s Actual Answers : ")
    res = "\n".join("{} {}".format(predicted, actual) for predicted, actual in zip(Y_pred3, Y_test))
    print(res)

    print()
    print(Border)
    print("Step 7 : Accuracy Calculation")
    print(Border)

    ########################################
    # Step 7 : Accuracy Calculation
    # Answer 3
    # Answer 5 - Testing Accuracy
    ########################################

    accuracy1 = accuracy_score(Y_pred1, Y_test)

    print()
    print(f"Accuracy of Model 1 is : {accuracy1 * 100}%")

    accuracy2 = accuracy_score(Y_pred2, Y_test)

    print()
    print(f"Accuracy of Model 2 is : {accuracy2 * 100}%")

    accuracy3 = accuracy_score(Y_pred3, Y_test)

    print()
    print(f"Accuracy of Model 3 is : {accuracy3 * 100}%")

    print()
    print(Border)
    print("Step 8 : Confusion Matrix Generation")
    print(Border)

    ########################################
    # Step 8 : Confusion Matrix Generation
    ########################################

    cm1 = confusion_matrix(Y_pred1, Y_test)

    tn, fp, fn, tp = confusion_matrix(Y_pred1, Y_test).ravel()

    print()
    print("Confusion Matrix for Model 1 is : ")
    print(cm1)

    print()
    print("For Model 1 : ")
    
    print()
    print(f"True Positive (TP) : {tp}")
    print(f"True Negative (TN) : {tn}")
    print(f"False Positive (FP) : {fp}")
    print(f"False Negative (FN) : {fn}")

    Data1 = ConfusionMatrixDisplay(confusion_matrix = cm1, display_labels = Model1.classes_)
    
    Data1.plot()
    plt.title("Confusion Matrix of Student Performance with max_depth = 1")
    plt.show()

    ########################################
    # Answer 5 - Training Model
    ########################################

    Y_pred_train = Model1.predict(X_train)

    print()
    print("Predicted Answers v/s Actual Answers for Training Model: ")
    res = "\n".join("{} {}".format(predicted, actual) for predicted, actual in zip(Y_pred_train, Y_train))
    print(res)

    accuracy_train = accuracy_score(Y_pred_train, Y_train)

    print()
    print(f"Training Accuracy is : {accuracy_train * 100}%")    

    print()
    print(Border)
    print("Step 9 : Final Conclusion")
    print(Border)

    ########################################
    # Step 9 : Final Conclusion
    ########################################

    print()
    print("After comparing both training and testing accuracy, " \
    "we conclude that all models (max_depth = 1, 3, None) are of good fit with 100% accuracy")

    # Answer 7

    input_data = pd.DataFrame([{
    "StudyHours": 6,
    "Attendance": 85,
    "PreviousScore": 66,
    "AssignmentsCompleted": 7,
    "SleepHours": 7
}])

    Y_ud = Model1.predict(input_data)

    print()
    print(Y_ud)

    print()
    print("The outcome of the student performance data given by input is that the student will pass")

if __name__ == "__main__":
    
    # Answer 8
    main()