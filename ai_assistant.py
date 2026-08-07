import pandas as pd
import joblib

# Load trained model
model = joblib.load("student_model.pkl")


def predict_grade(student):

    data = pd.DataFrame([{
        "Attendance": student["Attendance"],
        "Python": student["Python"],
        "DBMS": student["DBMS"],
        "DSA": student["DSA"],
        "Assignments": student["Assignments"],
        "Previous_GPA": student["Previous_GPA"]
    }])

    prediction = model.predict(data)

    return prediction[0]


def get_suggestions(student):

    attendance = student["Attendance"]

    average = (
        student["Python"] +
        student["DBMS"] +
        student["DSA"]
    ) / 3

    predicted_grade = predict_grade(student)

    print("\n==========================================")
    print("          AI STUDENT REPORT")
    print("==========================================")

    print(f"Student Name      : {student['Name']}")
    print(f"Predicted Grade   : {predicted_grade}")
    print("Model Used        : Decision Tree")
    print("Model Accuracy    : 71.67 %")

    print("\nAcademic Summary")
    print("----------------")

    print(f"Average Marks     : {average:.2f}")
    print(f"Attendance        : {attendance}%")

    print("\nStrengths")

    if student["Python"] >= 75:
        print("✔ Good Python Performance")

    if student["DBMS"] >= 75:
        print("✔ Good DBMS Performance")

    if student["DSA"] >= 75:
        print("✔ Good DSA Performance")

    if attendance >= 85:
        print("✔ Excellent Attendance")

    print("\nNeeds Improvement")

    if student["Python"] < 60:
        print("• Improve Python")

    if student["DBMS"] < 60:
        print("• Improve DBMS")

    if student["DSA"] < 60:
        print("• Improve DSA")

    if attendance < 75:
        print("• Improve Attendance")

    print("\nAI Recommendations")

    if predicted_grade == "A":
        print("✔ Continue your current preparation.")
        print("✔ Practice coding regularly.")
        print("✔ Maintain your attendance.")

    elif predicted_grade == "B":
        print("✔ Revise difficult subjects weekly.")
        print("✔ Solve coding problems daily.")
        print("✔ Improve attendance if possible.")

    elif predicted_grade == "C":
        print("✔ Spend more time on weak subjects.")
        print("✔ Complete all assignments.")
        print("✔ Increase practice sessions.")

    else:
        print("✔ Meet your faculty mentor.")
        print("✔ Follow a daily study plan.")
        print("✔ Focus on fundamentals.")

    print("==========================================")