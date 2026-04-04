import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():

    Border = "-" * 60
    
    #-------------------------------------
    # Step 1 : Load the dataset
    #-------------------------------------

    print()
    print(Border)
    print("Step 1 : Load the dataset")
    print(Border)
    
    df = pd.read_csv("student-mat.csv", sep=";")

    print("\nFirst 5 records of the dataset are :")
    print(df.head(5))

    print("\nShape of the dataset is :")
    print(df.shape)

    print("\nMissing values in the dataset :")
    print(df.isnull().sum())

    print("\nStatistical Analysis of the Dataset :")
    print(df.describe())

    #-------------------------------------
    # Step 2 : Select Features (Independent)
    #-------------------------------------

    print("\nStep 2 : Select Features (Independent)")

    X = df[["G1", "G2", "G3", "studytime", "failures", "absences"]]

    print("\nSelected features : ")
    print(X.head())

    print("\nShape of selected features : ")
    print(X.shape)

    #-------------------------------------
    # Step 3 : Scale the data
    #-------------------------------------

    scalar = StandardScaler()
    X_scaled = scalar.fit_transform(X)

    print("\nData after scaling :")
    print(X_scaled[:5])

    #-------------------------------------
    # Step 4 : Use elbow method
    #-------------------------------------

    WCSS = []

    for i in range(1, 11):
        model = KMeans(n_clusters=i, random_state=42, n_init=10)
        model.fit(X_scaled)
        WCSS.append(model.inertia_)

    plt.figure(figsize=(8,5))
    plt.plot(range(1,11), WCSS, marker = 'o')
    plt.xlabel("Number of clusters")
    plt.ylabel("WCSS")
    plt.title("Elbow method")
    plt.grid(True)
    plt.show()

    #-------------------------------------
    # Step 5 : Train the model
    #-------------------------------------

    model = KMeans(n_clusters=3, random_state=42, n_init=10)
    clusters = model.fit_predict(X_scaled)

    df["clusters"] = clusters

    print("\nDataset with clusters :")
    print(df.head(30))

if __name__ == "__main__":
    main()