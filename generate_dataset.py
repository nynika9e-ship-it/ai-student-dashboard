import pandas as pd
import random

# Sample student names
names = [
    "Rahul", "Priya", "Arjun", "Sneha", "Kiran", "Anjali", "Vikram",
    "Divya", "Rohan", "Meera", "Sai", "Harsha", "Keerthi", "Akhil",
    "Pooja", "Nikhil", "Sravani", "Varun", "Teja", "Deepika"
]

students = []

for i in range(300):

    student_id = 1001 + i
    name = random.choice(names) + str(i + 1)
    branch = "CSE"
    semester = 3

    attendance = random.randint(55, 100)

    python = random.randint(35, 100)
    dbms = random.randint(35, 100)
    dsa = random.randint(35, 100)

    assignments = random.randint(4, 10)

    previous_gpa = round(random.uniform(5.5, 9.8), 2)

    average = (python + dbms + dsa) / 3

    # Grade generation (Target Variable)
    if average >= 85:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 55:
        grade = "C"
    else:
        grade = "D"

    students.append([
        student_id,
        name,
        branch,
        semester,
        attendance,
        python,
        dbms,
        dsa,
        assignments,
        previous_gpa,
        grade
    ])

columns = [
    "Student_ID",
    "Name",
    "Branch",
    "Semester",
    "Attendance",
    "Python",
    "DBMS",
    "DSA",
    "Assignments",
    "Previous_GPA",
    "Final_Grade"
]

df = pd.DataFrame(students, columns=columns)

df.to_csv("students.csv", index=False)

print("Dataset Generated Successfully!")
print(df.head())