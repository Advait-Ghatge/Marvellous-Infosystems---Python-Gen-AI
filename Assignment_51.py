import pandas as pd
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def preprocess(text):

    text = re.sub(r'\W', ' ', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = text.lower()  # Convert to lowercase
    return text

def main():

    df_fake = pd.read_csv("Fake.csv")
    df_true = pd.read_csv("True.csv")

    Border = "-" * 160

    # ------------------------------------------------
    # Step 1 : Data Preprocessing
    # ------------------------------------------------

    print()
    print(Border)
    print("Part 1 : Data Preprocessing")
    print(Border)

    print("\nValues from Fake Dataset are :")
    print(df_fake.head())

    print()
    print(Border)

    print("\nShape of Fake Dataset is :", df_fake.shape)

    print()
    print(Border)

    print("\nValues from True Dataset are :")
    print(df_true.head())

    print()
    print(Border)

    print("\nShape of True Dataset is :", df_true.shape)

    print()
    print(Border)

    df_fake["label"] = 0
    df_true["label"] = 1

    print("\nValues from Fake Dataset with Labels are :")
    print(df_fake.head())

    print()
    print(Border)

    print("\nValues from True Dataset with Labels are :")
    print(df_true.head())

    print()
    print(Border)

    print("\nShape of Fake Dataset after Label Creation is :", df_fake.shape)

    print("\nShape of True Dataset after Label Creation is :", df_true.shape)

    print()
    print(Border)

    print("\nConcatenating the 2 datasets - Fake.csv and True.csv")

    df = pd.concat([df_fake, df_true], axis=0)

    print("\nFirst 5 entries of merged dataset are :")
    print(df.head(5))

    print()
    print(Border)

    print("\nShape of merged dataset is :", df.shape)

    # ------------------------------------------------
    # Step 2 : Feature Extraction
    # ------------------------------------------------

    print()
    print(Border)
    print("Part 2 : Feature Extraction")
    print(Border)

    print("\nMissing Values from the dataset are :")
    print(df.isnull().sum())

    print("\nUnique Values from column - Subject are :")
    print(df["subject"].unique())

    print("\nUnique Values from column - Label are :")
    print(df["label"].unique())

    df["title"] = df["title"].apply(preprocess)
    df["text"] = df["text"].apply(preprocess)

    print("\nFirst 5 entries of preprocessed text data are :")
    print(df.head(5))

    y = df["label"].values

    combined_text = df["title"] + " " + df["text"]

    # ------------------------------------------------
    # Initialise the TF-IDF Vectorizer
    # ------------------------------------------------

    vectorizer = TfidfVectorizer(max_features=5000)

    # ------------------------------------------------
    # Fit and Transform the data
    # ------------------------------------------------

    tfidf_matrix = vectorizer.fit_transform(combined_text)

    # ------------------------------------------------
    # Convert the TF-IDF Matrix into DataFrame
    # ------------------------------------------------

    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

    tfidf_df["label"] = y

    df = tfidf_df

    print("\nFirst 5 entries of preprocessed text data with TF-IDF are :")
    print(df.head(5))

    print("\nShape of TF-IDF dataset is :", df.shape)

    print("\nColumns of the dataset are :")
    print(df.columns)

    # df.to_csv("MergedTF.csv", index = False)

    # print("\nMergedTF.csv gets created successfully")

    if "subject" in df.columns:
        print("\n'subject' column is present in dataframe")

    if "date" in df.columns:
        print("\n'date' column is present in dataframe")

    if "label" in df.columns:
        print("\n'label' column is present in dataframe")

    # ------------------------------------------------
    # Step 3 : Model Training
    # ------------------------------------------------

    print()
    print(Border)
    print("Part 3 : Model Training")
    print(Border)

    X = df.drop(columns=["label"])
    Y = df["label"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("\nTraining and Testing Data Splitting Completed!")

    Model_DT = DecisionTreeClassifier(random_state=42)
    Model_LR = LogisticRegression(max_iter=5000)

    Model_DT.fit(X_train, Y_train)
    Model_LR.fit(X_train, Y_train)

    hard_model = VotingClassifier(
        estimators=[
            ('lr', Model_LR),
            ('dt', Model_DT)
        ], voting="hard"
    )

    hard_model.fit(X_train, Y_train)

    pred_hard = hard_model.predict(X_test)

    acc_hard = accuracy_score(pred_hard, Y_test)

    cm_hard = confusion_matrix(pred_hard, Y_test)

    soft_model = VotingClassifier(
        estimators=[
            ('lr', Model_LR),
            ('dt', Model_DT)
        ], voting="soft"
    )

    soft_model.fit(X_train, Y_train)

    pred_soft = soft_model.predict(X_test)

    acc_soft = accuracy_score(pred_soft, Y_test)

    cm_soft = confusion_matrix(pred_soft, Y_test)

    # ------------------------------------------------
    # Step 4 : Model Evaluation
    # ------------------------------------------------

    print()
    print(Border)
    print("Part 4 : Model Evaluation")
    print(Border)

    print("\nAccuracy of Hard-Voting is :", acc_hard)
    print("\nAccuracy of Soft-Voting is :", acc_soft)

    print("\nConfusion Matrix of Hard-Voting is :")
    print(cm_hard)

    print("\nConfusion Matrix of Soft-Voting is :")
    print(cm_soft)


if __name__ == "__main__":
    main()