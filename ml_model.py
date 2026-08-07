import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load Dataset
students = pd.read_csv("students.csv")

# Features (Input)
X = students[
    [
        "Attendance",
        "Python",
        "DBMS",
        "DSA",
        "Assignments",
        "Previous_GPA"
    ]
]

# Target (Output)
y = students["Final_Grade"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("=" * 50)
print("Decision Tree Model")
print("=" * 50)

print(f"Accuracy : {accuracy*100:.2f}%")

print("\nClassification Report\n")
print(classification_report(y_test, predictions))

# Save the trained model
joblib.dump(model, "student_model.pkl")

print("\nModel saved successfully as student_model.pkl")