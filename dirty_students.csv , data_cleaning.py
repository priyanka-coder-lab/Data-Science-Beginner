dirty_students.csv

Name,Marks,City
Priyanka,85,Pune
Amit,,Mumbai
Neha,92,Nashik
Ravi,67,Pune
Amit,,Mumbai

data_cleaning.py

import pandas as pd

df = pd.read_csv("dirty_students.csv")

print("Original Data:")
print(df)

# Missing values check
print("\nMissing values:")
print(df.isnull())

# Fill missing marks with average
avg_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(avg_marks)

# Remove duplicate rows
df = df.drop_duplicates()

print("\nCleaned Data:")
print(df)
