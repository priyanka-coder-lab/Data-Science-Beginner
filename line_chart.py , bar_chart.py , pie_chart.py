line_chart.py

import matplotlib.pyplot as plt

marks = [60, 70, 80, 90]
students = ["Amit", "Neha", "Priyanka", "Ravi"]

plt.plot(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students Marks Line Chart")
plt.show()

bar_chart.py

import matplotlib.pyplot as plt

students = ["Amit", "Neha", "Priyanka", "Ravi"]
marks = [60, 70, 80, 90]

plt.bar(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students Marks Bar Chart")
plt.show()

pie_chart.py

import matplotlib.pyplot as plt

labels = ["Pass", "Fail"]
values = [85, 15]

plt.pie(values, labels=labels, autopct="%1.1f%%")
plt.title("Result Analysis")
plt.show()









