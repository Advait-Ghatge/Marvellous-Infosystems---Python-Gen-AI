import math

def EucDist(P1, P2):

    Ans = math.sqrt(((P1['X'] - P2['X'])**2) + ((P1['Y'] - P2['Y'])**2))
    return Ans

def EucDist2(P1, P2):

    Ans = math.sqrt(((P1["Study_Hours"] - P2["Study_Hours"])**2) + ((P1["Attendance"] - P2["Attendance"])**2))
    return Ans


def main():
    
    ##############
    # Answer 1
    ##############

    # X = [1,2,3,6]
    # Y = [2,3,1,5]
    # Labels = ["Red", "Red", "Blue", "Blue"]

    Data = [
                {'point' : 'A', 'X' : 1, 'Y' : 2, 'label' : 'Red'},
                {'point' : 'B', 'X' : 2, 'Y' : 3, 'label' : 'Red'},
                {'point' : 'C', 'X' : 3, 'Y' : 1, 'label' : 'Blue'},
                {'point' : 'D', 'X' : 5, 'Y' : 6, 'label' : 'Blue'}
    ]

    print()
    X_pred = int(input("Enter X Coordinate : "))
    Y_pred = int(input("Enter Y Coordinate : "))

    new_point = {'X' : X_pred, 'Y' : Y_pred}
    print()
    print("Coodinates given by user are :", new_point)

    for i in Data:
        i['Dist'] = EucDist(i, new_point)

    print()
    print("All distances of provided point from given data are : ")

    for i in Data:
        print("Distance :", i)

    Sorted_Dist = sorted(Data, key = lambda item : item['Dist'])

    print()
    print("Sorted Distances are : ")
    for i in Sorted_Dist:
        print("Distance :", i)

    print()
    k = int(input("Enter the value of K for KNN : "))

    nearest = Sorted_Dist[:k]

    print()
    print("The K-Nearest coordinates are : ")
    for i in nearest:
        print("Distance :", i)

    # Voting

    votes = {}

    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label,0) + 1

    print()
    print("Voting Result is : ")

    for i in votes:
        print("Name :", i, "Number of votes :", votes[i])

    predicted_class = max(votes, key = votes.get)

    print()
    print(f"Predicted class of {new_point} is {predicted_class}")

    ##############
    # Answer 2
    ##############
    
    print()
    print("-" * 45)
    
    print()
    print("The prediction changes for value of K because the number of neighbouring points varies according to the value of K chosen -\n\nSmall K - Low Bias, High Variance\n"\
    "Large K - High Bias, Low Variance")

    ##############
    # Answer 3
    ##############
    print()
    print("-" * 45)

    Data = [
        {"Study_Hours" : 2, "Attendance" : 60, "Result" : "Fail"},
        {"Study_Hours" : 5, "Attendance" : 80, "Result" : "Pass"},
        {"Study_Hours" : 6, "Attendance" : 85, "Result" : "Pass"},
        {"Study_Hours" : 1, "Attendance" : 50, "Result" : "Fail"},
    ]

    print()
    SH1 = int(input("Enter Study Hours : "))
    Att1 = int(input("Enter Attendance : "))

    Input_Data = {"Study_Hours" : SH1, "Attendance" : Att1}
    print()
    print("Data from user is :", Input_Data)

    for i in Data:
        i["Distance"] = EucDist2(Input_Data, i)

    print()
    print("Distance of User Data from Training Data is : ")
    for i in Data:
        print(i)

    sorted_data = sorted(Data, key = lambda item : item["Distance"])
    print()
    print("Sorted Data is : ")
    for i in sorted_data:
        print(i)

    k = 3
    print()
    print("The value of K for this case is :", k)

    nearest = sorted_data[:k]
    print()
    print("The K Nearest Points are : ")
    for i in nearest:
        print(i)

    # Voting
    votes = {}
    for neighbour in nearest:
        label = neighbour['Result']
        votes[label] = votes.get(label, 0) + 1
    print()
    for i in votes:
        print(f"Name : {i}, Votes : {votes[i]}")

    predicted_result = max(votes, key = votes.get)
    print()
    print(f"Predicted Result for {Input_Data} is {predicted_result}")

if __name__ == "__main__":
    main()