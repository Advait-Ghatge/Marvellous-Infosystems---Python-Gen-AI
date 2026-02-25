import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    Border = "-"*40

    DatasetPath = "student_performance_ml.csv"

    # url = "https://drive.google.com/drive/folders/1xLQH0Eqx7w5SRhfxlN0bwiTs-zbRnLma/student_performance_ml.csv"
    df = pd.read_csv(DatasetPath)

    print()
    print("Dataset loaded successfully")

    # Answer 1

    print()
    print(Border)
    print("Answer 1")
    print(Border)

    print()
    print("First Five Records are : ")
    print(df.head(5))

    print()
    print("Last Five Records are : ")
    print(df.tail(5))

    print()
    print(f"Total Number of Rows and Columns are {df.shape[0]} and {df.shape[1]} respectively")

    print()
    print("List of columns is :", list(df.columns))

    print()
    print("The data types of columns is :")
    for i in df.columns:
        print(f"The datatype of column {i} is {type(i)}")

    # Answer 2
    
    print()
    print(Border)
    print("Answer 2")
    print(Border)

    print()
    print("The total number of students in the dataset is :", df["FinalResult"].count())

    
    print()
    print("The total number of students who passed is :", len(df[df["FinalResult"] == 1]))
    
    print()
    print("The total number of students who failed is :", len(df[df["FinalResult"] == 0]))

    # Answer 3
    
    print()
    print(Border)
    print("Answer 3")
    print(Border)

    print()
    print("Average Study Hours :", df["StudyHours"].mean())

    print()
    print("Average Attendance :", df["Attendance"].mean())

    print()
    print("Maximum of Previous Score is :", df["PreviousScore"].max())

    print()
    print("Minimum Sleep Hours :", df["SleepHours"].min())

    # Answer 4

    print()
    print(Border)
    print("Answer 4")
    print(Border)

    print()
    print("Distribution of Label i.e. Final Result is :", df["FinalResult"].value_counts())

    print()
    print(f"The percentage of students who passed is : {(len(df[df["FinalResult"] == 1]) / df["FinalResult"].count()) * 100} %")

    
    print()
    print(f"The percentage of students who failed is : {(len(df[df["FinalResult"] == 0]) / df["FinalResult"].count()) * 100} %")

    print()
    print("The dataset is indeed balanced as there is almost even split between the data")

    
    # Answer 5

    print()
    print(Border)
    print("Answer 5")
    print(Border)

    print()
    print("All the students who have passed study for at least 4.5 hours daily")
    print("All the students who have failed study less than 4 hours daily")
    print("Hence, we can conclude that studying more increases chances of passing")

    print()
    print("All students who have passed have minimum 75% attendance")
    print("All students who have failed have less than 75% attendance")
    print("Hence, we can conclude that attending classes increases chances of passing")


    # Answer 6

    print()
    print(Border)
    print("Answer 6")
    print(Border)

    print()
    print("Histogram of Study Hours - ")
    sns.histplot(df["StudyHours"])
    plt.show()


    # Answer 7

    print()
    print(Border)
    print("Answer 7")
    print(Border)

    for result in df["FinalResult"].unique():
        temp = df[df["FinalResult"] == result]
        plt.scatter(temp["StudyHours"], temp["PreviousScore"], label = result)

    plt.title("Student Performance : Study Hours v/s Previous Score")

    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")

    plt.legend()
    plt.grid(True)
    plt.show()


    # Answer 8

    print()
    print(Border)
    print("Answer 8")
    print(Border)

    print()
    print("The Box Plot for Attendance - ")
    sns.boxplot(x = df["Attendance"])
    plt.show()

    print()
    print("Observation : There are no outliers in this column data")

    
    # Answer 9

    print()
    print(Border)
    print("Answer 9")
    print(Border)

    for result in df["FinalResult"].unique():
        temp = df[df["FinalResult"] == result]
        plt.scatter(temp["AssignmentsCompleted"], temp["FinalResult"], label = result)

    plt.title("Student Performance : Assignments Completed v/s Final Result")

    plt.xlabel("Assignments Completed")
    plt.ylabel("Final Result")

    plt.legend()
    plt.grid(True)
    plt.show()

    print()
    print("Observation : The more assignments you complete, the better chance you have at passing")


    # Answer 10

    print()
    print(Border)
    print("Answer 10")
    print(Border)

    for result in df["FinalResult"].unique():
        temp = df[df["FinalResult"] == result]
        plt.scatter(temp["SleepHours"], temp["FinalResult"], label = result)

    plt.title("Student Performance : Sleep Hours v/s Final Result")

    plt.xlabel("Sleep Hours")
    plt.ylabel("Final Result")

    plt.legend()
    plt.grid(True)
    plt.show()

    print()
    print("Observation : If you sleep for more than 6 hours, the better chance you have at passing")


if __name__ == "__main__":
    main()