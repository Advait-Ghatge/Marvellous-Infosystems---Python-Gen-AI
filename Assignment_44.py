import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def Marvellous_Advertise(DataPath):
    
    Border = "-" * 90

    #-------------------------------------------------------
    # Step 1 : Loading Dataset
    #-------------------------------------------------------
    print()
    print(Border)
    print("Step 1 : Loading Dataset")
    print(Border)

    df = pd.read_csv(DataPath)

    print()
    print("Few Columns from Dataset : ")
    print()
    print(df.head())

    #-------------------------------------------------------
    # Step 2 : Data Cleaning - Removing Unwanted Columns
    #-------------------------------------------------------

    print()
    print(Border)
    print("Step 2 : Data Cleaning - Removing Unwanted Columns")
    print(Border)

    print()
    print("Shape of Dataset before removal :", df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns = ['Unnamed: 0'], inplace = True)

    print()
    print("Shape of Dataset after removal :", df.shape)

    print()
    print(Border)
    print()
    print("Clean Dataset is : ")
    print()
    print(df.head())
    print()
    print(Border)

    #-------------------------------------------------------
    # Step 3 : Data Cleaning - Checking Missing Values
    #-------------------------------------------------------

    print()
    print(Border)
    print("Step 3 : Data Cleaning - Checking Missing Values")
    print(Border)

    print()
    print("Missing Values Count : ")
    print(df.isnull().sum())

    #-------------------------------------------------------
    # Step 4 : Data Analysis - Display Statistical Summary
    #-------------------------------------------------------

    print()
    print(Border)
    print("Step 4 : Data Analysis - Display Statistical Summary")
    print(Border)

    print()
    print(df.describe())

    #-------------------------------------------------------
    # Step 5 : Data Analysis - Correlation Between Columns
    #-------------------------------------------------------

    print()
    print(Border)
    print("Step 5 : Data Analysis - Correlation Between Columns")
    print(Border)

    print()
    print("Correlation Matrix : \n")
    print(df.corr())

    #---------------------------------------------------------------------------------
    # Step 6 : Model Building - Split Dataset into Independent and Dependent Variables
    #---------------------------------------------------------------------------------

    print()
    print(Border)
    print("Step 6 : Model Building - Split Dataset into Independent and Dependent Variables")
    print(Border)

    X = df[['TV', 'radio', 'newspaper']]
    Y = df['sales']

    print()
    print("Shape of Independent Variables :", X.shape)
    print("Shape of Dependent Variables :", Y.shape)

    #---------------------------------------------------------------------------------
    # Step 7 : Model Building - Split Dataset for Training and Testing
    #---------------------------------------------------------------------------------

    print()
    print(Border)
    print("Step 7 : Model Building - Split Dataset for Training and Testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

    print()
    print("Shape of X_train :", X_train.shape)

    print()
    print("Shape of X_test :", X_test.shape)

    print()
    print("Shape of Y_train :", Y_train.shape)

    print()
    print("Shape of Y_test :", Y_test.shape)

    #---------------------------------------------------------------------------------
    # Step 8 : Model Creation and Training - Create and Train the Model
    #---------------------------------------------------------------------------------

    print()
    print(Border)
    print("Step 8 : Model Creation and Training - Create and Train the Model")
    print(Border)

    Model = LinearRegression()

    Model.fit(X_train, Y_train)

    print()
    print("Model Training completed!")

    #---------------------------------------------------------------------------------
    # Step 9 : Model Testing - Test the Model
    #---------------------------------------------------------------------------------

    print()
    print(Border)
    print("Step 9 : Model Testing - Test the Model")
    print(Border)

    Y_pred = Model.predict(X_test)
 
    print()
    print("Model Testing completed!")

    #---------------------------------------------------------------------------------
    # Step 10 : Model Evaluation - Evaluate the Model
    #---------------------------------------------------------------------------------

    print()
    print(Border)
    print("Step 10 : Model Evaluation - Evaluate the Model")
    print(Border)

    MSE = mean_squared_error(Y_test, Y_pred)

    RMSE = np.sqrt(MSE)

    R2 = r2_score(Y_test, Y_pred)

    print()
    print("Mean Squared Error :", MSE)

    print()
    print("Root Mean Squared Error :", RMSE)

    print()
    print("R-Squared Value :", R2)

    #---------------------------------------------------------------------------------
    # Step 11 : Model Evaluation - Calculating Model Coefficient and Intercept
    #---------------------------------------------------------------------------------

    print()
    print(Border)
    print("Step 11 : Model Evaluation - Calculating Model Coefficient and Intercept")
    print(Border)

    print()
    for column, value in zip(X.columns, Model.coef_):

        print(f"{column} : {value}")

    print()
    print("Intercept :", Model.intercept_)

    #---------------------------------------------------------------------------------
    # Step 12 : Model Evaluation - Comparing the Actual and Predicted Values
    #---------------------------------------------------------------------------------

    print()
    print(Border)
    print("Step 12 : Model Evaluation - Comparing the Actual and Predicted Values")
    print(Border)

    Result = pd.DataFrame({
        'Actual Sales' : Y_test.values,
        'Predicted Sales' : Y_pred,
        })
    
    print()
    print(Result.head())


def main():
    
    Marvellous_Advertise("Advertising.csv")

if __name__ == "__main__":
    main()