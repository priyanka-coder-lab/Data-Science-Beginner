student_project.csv

Name,Marks,City
Priyanka,85,Pune
Amit,,Mumbai
Neha,92,Nashik
Ravi,67,Pune
Sneha,74,Mumbai

student_project_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

# Read data
df = pd.read_csv("student_project.csv")
print("Original Data:")
print(df)

# Fill missing values
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Analysis
print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

# Filter
print("\nStudents with Marks >= 75")
print(df[df["Marks"] >= 75])

# Visualization
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Performance Analysis")
plt.show()


