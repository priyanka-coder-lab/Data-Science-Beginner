pandas_dataframe.py

import pandas as pd

data = {
    "Name": ["Priyanka", "Amit", "Neha"],
    "Marks": [85, 78, 92]
}

df = pd.DataFrame(data)
print(df)

pandas_analysis.py

import pandas as pd

data = {
    "Name": ["Priyanka", "Amit", "Neha"],
    "Marks": [85, 78, 92]
}

df = pd.DataFrame(data)

print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

pandas_filter.py

import pandas as pd

data = {
    "Name": ["Priyanka", "Amit", "Neha"],
    "Marks": [85, 78, 92]
}

df = pd.DataFrame(data)

print("Students with marks >= 80")
print(df[df["Marks"] >= 80])


