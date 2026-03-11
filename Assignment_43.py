import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

Border = "-" * 50

##################################################
# Step 1 : Get Data
##################################################

print()
print(Border)
print("Step 1 : Get Data")
print(Border)

df = pd.read_csv("PlayPredictor.csv")

print()
print("Few entries from the loaded dataset are :\n")
print(df.head())

##################################################
# Step 2 : Clean, Prepare and Manipulate the Data
##################################################

print()
print(Border)
print("Step 2 : Clean, Prepare and Manipulate the Data")
print(Border)

print()
print("Removing the unnamed indexed column from the dataset...")

print()
print("Shape of dataset before unnamed column removal :", df.shape)

if 'Unnamed: 0' in df.columns:
    df.drop(columns = ['Unnamed: 0'],inplace = True)

print("Shape of dataset after unnamed column removal :", df.shape)

##################################################
# Step 3 : Train the Model
##################################################

print()
print(Border)
print("Step 3 : Train the Model")
print(Border)

# --- Step 3: Prepared Data ---
df.dropna(inplace=True)

# Map values directly using a dictionary (more robust than .replace)
weather_map = {"Sunny": 0, "Overcast": 1, "Rainy": 2}
temp_map = {"Cool": 0, "Mild": 1, "Hot": 2}
play_map = {"No": 0, "Yes": 1}

# Apply mapping (Ensure column names match your CSV exactly)
df['Whether'] = df['Whether'].map(weather_map) 
df['Temperature'] = df['Temperature'].map(temp_map)
df['Play'] = df['Play'].map(play_map)

X = df[['Whether', 'Temperature']] # Keep as DataFrame
Y = df['Play']

# Split the data
X_train, X_test_split, Y_train, Y_test_split = train_test_split(X, Y, stratify=Y, test_size=0.2, random_state=42)

Model = KNeighborsClassifier(n_neighbors=3)
Model.fit(X_train, Y_train)

# --- Step 4: Testing with User Input ---
w_input = input("Enter weather (Sunny, Overcast, Rainy): ")
t_input = input("Enter temperature (Cool, Mild, Hot): ")

# Convert input to numbers using the same maps
w_num = weather_map.get(w_input, 0) # Default to 0 if typo
t_num = temp_map.get(t_input, 0)

# Create a 2D array for prediction (KNN expects a list of samples)
user_data = [[w_num, t_num]]
prediction = Model.predict(user_data)

result = "Play" if prediction[0] == 1 else "Don't Play"
print(f"Prediction: {result}")