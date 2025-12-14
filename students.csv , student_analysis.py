students.csv

Name,Marks,City
Priyanka,85,Pune
Amit,78,Mumbai
Neha,92,Nashik
Ravi,67,Pune

student_analysis.py

import pandas as pd

df = pd.read_csv("students.csv")

print("Full Data:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

print("\nStudents from Pune:")
print(df[df["City"] == "Pune"])

print("\nStudents with Marks >= 80:")
print(df[df["Marks"] >= 80])
