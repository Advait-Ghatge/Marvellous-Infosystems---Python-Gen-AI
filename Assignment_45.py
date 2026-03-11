import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def main():

    Border = "-" * 125
    
    df = pd.read_csv("WinePredictor.csv")

    print()
    print(Border)

    print()
    print("First few entries from the dataset are : ")
    print()
    print(df.head())

    print()
    print(Border)

    print()
    print("Missing Data Check : \n")
    print(df.isnull().sum())

    print()
    print("Data Validation Completed!")

    print()
    print(Border)

    X = df.drop(columns = ['Class'])
    Y = df['Class']

    # print()
    # print(X.shape)

    # print()
    # print(Y.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                                        test_size = 0.2, 
                                                        random_state = 42, 
                                                        stratify = Y)
    
    Model = DecisionTreeClassifier(
        max_depth = 9,
        criterion = 'gini',
        random_state = 42
    )

    print()
    print("Model selected is : Decision Tree Classifier")

    print()
    print(Border)

    Model.fit(X_train, Y_train)

    print()
    print("Model Training completed!")

    print()
    print(Border)

    Y_pred = Model.predict(X_test)

    accuracy = accuracy_score(Y_pred, Y_test)

    print()
    print("Accuracy of the model is :", accuracy * 100)

    print()
    print("Classification Report : ")
    print(classification_report(Y_pred, Y_test))


if __name__ == "__main__":
    main()