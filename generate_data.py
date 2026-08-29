import pandas as pd
import numpy as np
import os


# ==========================================
# RANDOM SEED
# ==========================================

np.random.seed(42)


# ==========================================
# BASIC SETTINGS
# ==========================================

n = 200


# ==========================================
# STUDENT INFORMATION
# ==========================================

student_ids = [f"S{i:03d}" for i in range(1, n + 1)]

first_names = [
    "Rahul", "Priya", "Aman", "Sneha", "Rohan",
    "Karan", "Neha", "Arjun", "Ananya", "Vikram",
    "Pooja", "Aditya", "Simran", "Nikhil", "Isha"
]

names = np.random.choice(first_names, n)

ages = np.random.randint(18, 23, n)

departments = np.random.choice(
    ["CSE", "IT", "ECE", "ME", "CE"],
    n
)


# ==========================================
# STUDY / BEHAVIOR DATA
# ==========================================

attendance = np.random.randint(50, 101, n)

study_hours = np.random.randint(5, 31, n)

assignments = np.random.randint(3, 11, n)

previous_score = np.random.randint(40, 101, n)


# ==========================================
# REALISTIC PERFORMANCE
# ==========================================

base_performance = (
    previous_score * 0.35
    + attendance * 0.20
    + study_hours * 0.80
    + assignments * 1.50
    + np.random.normal(0, 5, n)
)


math = np.clip(
    base_performance + np.random.normal(0, 5, n),
    35,
    100
)

science = np.clip(
    base_performance + np.random.normal(0, 5, n),
    35,
    100
)

english = np.clip(
    base_performance + np.random.normal(0, 5, n),
    35,
    100
)


math = np.round(math).astype(int)
science = np.round(science).astype(int)
english = np.round(english).astype(int)


# ==========================================
# CREATE DATAFRAME
# ==========================================

df = pd.DataFrame({
    "Student_ID": student_ids,
    "Name": names,
    "Age": ages,
    "Department": departments,
    "Math": math,
    "Science": science,
    "English": english,
    "Attendance": attendance,
    "Study_Hours": study_hours,
    "Assignments_Completed": assignments,
    "Previous_Score": previous_score
})


# ==========================================
# INTRODUCE DATA QUALITY PROBLEMS
# ==========================================

# Missing marks
df.loc[5, "Math"] = np.nan
df.loc[20, "Science"] = np.nan
df.loc[35, "English"] = np.nan

# Missing attendance
df.loc[50, "Attendance"] = np.nan

# Invalid age
df.loc[60, "Age"] = 15
df.loc[70, "Age"] = 35

# Invalid attendance
df.loc[80, "Attendance"] = 105
df.loc[90, "Attendance"] = -10

# Invalid study hours
df.loc[100, "Study_Hours"] = -5

# Invalid assignment count
df.loc[110, "Assignments_Completed"] = -2

# Extra spaces
df.loc[120, "Name"] = "  Rahul  "
df.loc[130, "Department"] = " CSE "

# Duplicate student
df = pd.concat(
    [df, df.iloc[[0]]],
    ignore_index=True
)


# ==========================================
# SAVE RAW DATA
# ==========================================

os.makedirs("data/raw", exist_ok=True)

df.to_csv(
    "data/raw/students_raw.csv",
    index=False
)


# ==========================================
# OUTPUT
# ==========================================

print("Dataset created successfully!")

print("Number of students:", len(df))

print("\nFirst 5 rows:")
print(df.head())