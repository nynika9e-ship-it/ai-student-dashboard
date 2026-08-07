import pandas as pd
from ai_assistant import get_suggestions
from analytics import show_dashboard

# Load student data
try:
    students = pd.read_csv("students.csv")
except FileNotFoundError:
    print("Error: students.csv file not found!")
    exit()

print("=" * 60)
print("      AI-BASED STUDENT ASSISTANT")
print("   + DATA ANALYTICS DASHBOARD")
print("=" * 60)
print("Developed using Python, Pandas, NumPy & Matplotlib")
print("=" * 60)

# Student Login
student_id = int(input("Enter Student ID: "))

# Check if student exists
student = students[students["Student_ID"] == student_id]

if student.empty:
    print("\nStudent not found!")
else:
    student = student.iloc[0]

    print(f"\nWelcome, {student['Name']}!")

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. View Profile")
        print("2. View Marks")
        print("3. View Attendance")
        print("4. AI Study Suggestions")
        print("5. Data Analytics Dashboard")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\n----- Student Profile -----")
            print(f"Student ID : {student['Student_ID']}")
            print(f"Name       : {student['Name']}")
            print(f"Branch     : {student['Branch']}")
            print(f"Semester   : {student['Semester']}")

        elif choice == "2":
            print("\n----- Marks -----")
            print(f"Python : {student['Python']}")
            print(f"DBMS   : {student['DBMS']}")
            print(f"DSA    : {student['DSA']}")

            average = (student["Python"] + student["DBMS"] + student["DSA"]) / 3
            print(f"Average: {average:.2f}")

        elif choice == "3":
            print("\n----- Attendance -----")
            print(f"Attendance: {student['Attendance']}%")

        elif choice == "4":
            get_suggestions(student)

        elif choice == "5":
            show_dashboard()

        elif choice == "6":
            print("\nThank you for using AI-Based Student Assistant!")
            break

        else:
            print("\nInvalid choice! Please try again.")