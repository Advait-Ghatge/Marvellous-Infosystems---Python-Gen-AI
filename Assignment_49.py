import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay

# --------------------------------------------------------------------------------
# Answer 1
# --------------------------------------------------------------------------------

Border = "=" * 60

print()
print(Border)
print("Answer 1")
print(Border)

df = pd.read_csv("diabetes.csv")

print("\nFirst Five Rows of Data are :")
print(df.head(5))

print("\nMissing Values Count :")
print(df.isnull().sum())

print("\nOutput from describe() method is :")
print(df.describe())

print("\nDistribution of Target Variable i.e. Outcome is :")

counts, edges, bars = plt.hist(df["Outcome"])
plt.bar_label(bars, fmt='%d')
plt.show()

print("\nData plotted with Pairplot :")
sns.pairplot(df, hue="Outcome")
plt.show()

# --------------------------------------------------------------------------------
# Answer 2
# --------------------------------------------------------------------------------

print()
print(Border)
print("Answer 2")
print(Border)

print("\nReplacing Zero Values in Glucose and Blood Pressure Columns with their Median :")

# --------------------------------------------------------------------------------
# Handling Glucose Column
# --------------------------------------------------------------------------------

print("\nMean of Glucose Column before Preprocessing :")
print(df["Glucose"].mean())

Median_Glucose = df["Glucose"].median()

df["Glucose"] = df["Glucose"].replace(0, Median_Glucose)

print("\nMean of Glucose Column after Preprocessing :")
print(df["Glucose"].mean())

# --------------------------------------------------------------------------------
# Handling Blood Pressure Column
# --------------------------------------------------------------------------------

print("\nMean of Blood Pressure Column before Preprocessing :")
print(df["BloodPressure"].mean())

Median_BP = df["BloodPressure"].median()

df["BloodPressure"] = df["BloodPressure"].replace(0, Median_BP)

print("\nMean of Blood Pressure Column after Preprocessing :")
print(df["BloodPressure"].mean())

# --------------------------------------------------------------------------------
# Splitting the Data into Independent (Features) and Dependent (Labels) Variables
# --------------------------------------------------------------------------------

X = df.drop(columns = ["Outcome"])
Y = df["Outcome"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42, stratify = Y)

print("\nShape of X_train is :", X_train.shape)
print("Shape of Y_train is :", Y_train.shape)
print("Shape of X_test is :", X_test.shape)
print("Shape of Y_test is :", Y_test.shape)

# --------------------------------------------------------------------------------
# Feature Scaling
# --------------------------------------------------------------------------------

Scaler = StandardScaler()

X_train_scaled = Scaler.fit_transform(X_train)
X_test_scaled = Scaler.fit_transform(X_test)

# --------------------------------------------------------------------------------
# Answer 3
# --------------------------------------------------------------------------------

print()
print(Border)
print("Answer 3")
print(Border)

# --------------------------------------------------------------------------------
# Fitting Different Models
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# 1 : Decision Tree Classifier
# --------------------------------------------------------------------------------

Model_DT = DecisionTreeClassifier(criterion = 'gini', max_depth = 7)

Model_DT.fit(X_train_scaled, Y_train)

Y_pred_DT = Model_DT.predict(X_test_scaled)

print("\nAccuracy of the Model - Decision Tree is :", accuracy_score(Y_pred_DT, Y_test))
print("\nClassification Report for Decision Tree Classifier :")
print(classification_report(Y_test, Y_pred_DT))

print("\nConfusion Matrix for Decision Tree Classifier is :")
CM_DT = confusion_matrix(Y_test, Y_pred_DT)
DISP_DT = ConfusionMatrixDisplay(confusion_matrix = CM_DT)
DISP_DT.plot(cmap = plt.cm.Blues)
plt.show()

Results_DT = pd.DataFrame({"Actual" : Y_test, "Predicted" : Y_pred_DT})
print("\nThe Results of Decision Tree Classifier are :")
print(Results_DT.head())

print("\nThe predictions made by the Decision Tree Model are saved in the file - Results_DT.csv")
Results_DT.to_csv("Results_DT.csv", index = True)

# --------------------------------------------------------------------------------
# 1 : K Nearest Neighbour
# --------------------------------------------------------------------------------

Model_KNN = KNeighborsClassifier(n_neighbors = 29)

Model_KNN.fit(X_train_scaled, Y_train)

Y_pred_KNN = Model_KNN.predict(X_test_scaled)

print("\nAccuracy of the Model - KNN is :", accuracy_score(Y_pred_KNN, Y_test))
print("\nClassification Report for KNN :")
print(classification_report(Y_test, Y_pred_KNN))

print("\nConfusion Matrix for KNN is :")
CM_KNN = confusion_matrix(Y_test, Y_pred_KNN)
DISP_KNN = ConfusionMatrixDisplay(confusion_matrix = CM_KNN)
DISP_KNN.plot(cmap = plt.cm.Blues)
plt.show()

Results_KNN = pd.DataFrame({"Actual" : Y_test, "Predicted" : Y_pred_KNN})
print("\nThe Results of KNN are :")
print(Results_KNN.head())

print("\nThe predictions made by the KNN Model are saved in the file - Results_KNN.csv")
Results_KNN.to_csv("Results_KNN.csv", index = True)