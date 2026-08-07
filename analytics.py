import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def show_dashboard():

    students = pd.read_csv("students.csv")

    students["Average"] = (
        students["Python"] +
        students["DBMS"] +
        students["DSA"]
    ) / 3

    print("\n==========================================")
    print("      DATA ANALYTICS DASHBOARD")
    print("==========================================")

    print(f"Total Students      : {len(students)}")
    print(f"Highest Average     : {students['Average'].max():.2f}")
    print(f"Lowest Average      : {students['Average'].min():.2f}")
    print(f"Overall Average     : {students['Average'].mean():.2f}")
    print(f"Average Attendance  : {students['Attendance'].mean():.2f}%")

    topper = students.loc[students["Average"].idxmax()]

    print(f"Top Performer       : {topper['Name']}")

    passed = np.sum(students["Average"] >= 50)
    pass_percentage = (passed / len(students)) * 100

    print(f"Pass Percentage     : {pass_percentage:.2f}%")

    print("\nTop 5 Students")
    print("------------------------------------------")

    top5 = students.sort_values(
        by="Average",
        ascending=False
    ).head(5)

    print(top5[["Name", "Average"]])

    print("\nGenerating Charts...")

    plt.figure(figsize=(12, 8))

    # Chart 1
    plt.subplot(2, 2, 1)
    top10 = students.sort_values(
    	by="Average",
    	ascending=False
    ).head(10)

    plt.bar(top10["Name"], top10["Average"])
    plt.title("Average Marks")
    plt.xlabel("Students")
    plt.ylabel("Marks")

    # Chart 2
    plt.subplot(2, 2, 2)

    fail = len(students) - passed

    plt.pie(
        [passed, fail],
        labels=["Pass", "Fail"],
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Pass vs Fail")

    # Chart 3
    plt.subplot(2, 2, 3)

    grade_counts = students["Final_Grade"].value_counts()

    plt.bar(
        grade_counts.index,
        grade_counts.values
    )

    plt.title("Grade Distribution")
    plt.xlabel("Grade")
    plt.ylabel("Students")

    # Chart 4
    plt.subplot(2, 2, 4)

    plt.hist(
    students["Attendance"],
    bins=10
    )

    plt.title("Attendance Distribution")
    plt.xlabel("Attendance")
    plt.ylabel("Students")

    plt.title("Student Attendance Analysis")
    plt.xlabel("Students")
    plt.ylabel("Attendance (%)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()