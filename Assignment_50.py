import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, roc_curve

# --------------------------------------------------------------------------------
# Answer 1
# --------------------------------------------------------------------------------

Border = "-" * 60

print()
print(Border)
print("Task 1 - Load & Explore The Dataset")
print(Border)

df = pd.read_csv("bank-full.csv", sep=";")

print("\nFirst 5 entries from the dataset are :")
print(df.head(5))

print("\nStatistical Summary of the dataset is :")
print(df.describe())

print("\nDistribution of Target Variable i.e. Outcome is :")

counts, edges, bars = plt.hist(df["y"])
plt.bar_label(bars, fmt='%d')
plt.show()

# --------------------------------------------------------------------------------
# Answer 2
# --------------------------------------------------------------------------------

print()
print(Border)
print("Task 2 - Data Preprocessing")
print(Border)

print("\nDataset Information :")
print(df.info())

# Listing Categorical Columns

cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
print(f"\nCategorical Columns: {cat_cols}")

# Encoding

df = pd.get_dummies(df,columns=cat_cols, drop_first = True)

for col in df.columns:
        if df[col].dtype == bool:
            df[col] = df[col].astype(int)

print("\nData after encoding :")
print(df.head(5))

# Scaling Numeric Columns

# print("\nDataset Information after encoding :")
# print(df.info())

X = df.drop(columns = ["y_yes"])
Y = df["y_yes"]

Scaler = StandardScaler()

X = Scaler.fit_transform(X)

# --------------------------------------------------------------------------------
# Answer 3
# --------------------------------------------------------------------------------

print()
print(Border)
print("Task 3 - Split The Data")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42, stratify = Y)

print("\nShape of X_train :", X_train.shape)
print("Shape of Y_train :", Y_train.shape)
print("Shape of X_test :", X_test.shape)
print("Shape of Y_test :", Y_test.shape)

# --------------------------------------------------------------------------------
# Answer 4
# --------------------------------------------------------------------------------

print()
print(Border)
print("Task 4 - Train Classification Models")
print(Border)

Model_DT = DecisionTreeClassifier(criterion = "gini", max_depth = 5)
Model_DT.fit(X_train, Y_train)
print("\nDecision Tree Model training completed!")

Model_LogR = LogisticRegression(max_iter=1000)
Model_LogR.fit(X_train, Y_train)
print("\nLogistic Regression Model training completed!")

Model_KNN = KNeighborsClassifier(n_neighbors = 7)
Model_KNN.fit(X_train, Y_train)
print("\nKNN Model training completed!")

# --------------------------------------------------------------------------------
# Answer 5
# --------------------------------------------------------------------------------

print()
print(Border)
print("Task 5 - Evaluating Trained Models")
print(Border)

# Decision Tree

Y_pred_DT = Model_DT.predict(X_test)

print("\nAccuracy of Decision Tree Model is :", accuracy_score(Y_test, Y_pred_DT))

print("\nClassification Report of Decision Tree Model is :")
print(classification_report(Y_test, Y_pred_DT))

print("\nConfusion Matrix of Decision Tree Model is :")
print(confusion_matrix(Y_test, Y_pred_DT))

print("\nROC-AUC Score of Decision Tree Model is :", roc_auc_score(Y_test, Y_pred_DT))

# Logistic Regression

Y_pred_LogR = Model_LogR.predict(X_test)

print("\nAccuracy of Logistic Regression Model is :", accuracy_score(Y_test, Y_pred_LogR))

print("\nClassification Report of Logistic Regression Model is :")
print(classification_report(Y_test, Y_pred_LogR))

print("\nConfusion Matrix of Logistic Regression Model is :")
print(confusion_matrix(Y_test, Y_pred_LogR))

print("\nROC-AUC Score of Logistic Regression Model is :", roc_auc_score(Y_test, Y_pred_LogR))

# KNN

Y_pred_KNN = Model_KNN.predict(X_test)

print("\nAccuracy of KNN Model is :", accuracy_score(Y_test, Y_pred_KNN))

print("\nClassification Report of KNN Model is :")
print(classification_report(Y_test, Y_pred_KNN))

print("\nConfusion Matrix of KNN Model is :")
print(confusion_matrix(Y_test, Y_pred_KNN))

print("\nROC-AUC Score of KNN Model is :", roc_auc_score(Y_test, Y_pred_KNN))

# --------------------------------------------------------------------------------
# Answer 6
# --------------------------------------------------------------------------------

print()
print(Border)
print("Task 6 - Visualizing ROC Curves")
print(Border)

plt.figure(figsize=(10, 6))

# Helper list to iterate through models and their names
# We use predict_proba()[:, 1] to get probabilities for the "positive" class
models = [
    (Model_DT, "Decision Tree", 'blue'),
    (Model_LogR, "Logistic Regression", 'red'),
    (Model_KNN, "KNN", 'green')
]

for model, name, color in models:
    # Get probabilities for the positive class (y_yes)
    probs = model.predict_proba(X_test)[:, 1]
    
    # Calculate TPR and FPR
    fpr, tpr, thresholds = roc_curve(Y_test, probs)
    
    # Calculate AUC for the label
    auc = roc_auc_score(Y_test, probs)
    
    # Plot the curve
    plt.plot(fpr, tpr, color=color, label=f'{name} (AUC = {auc:.2f})')

# Plot the diagonal 50/50 line (Baseline)
plt.plot([0, 1], [0, 1], color='black', linestyle='--')

plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')
plt.title('ROC Curve Comparison')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()