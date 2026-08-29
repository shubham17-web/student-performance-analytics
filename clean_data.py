import pandas as pd
import os


# ==========================================
# 1. LOAD RAW DATA
# ==========================================

df = pd.read_csv("data/raw/students_raw.csv")

print("Original rows:", len(df))


# ==========================================
# 2. REMOVE DUPLICATES
# ==========================================

duplicates = df.duplicated().sum()

print("Duplicate rows found:", duplicates)

df = df.drop_duplicates()


# ==========================================
# 3. CLEAN TEXT COLUMNS
# ==========================================

df["Name"] = df["Name"].str.strip()

df["Department"] = df["Department"].str.strip().str.upper()


# ==========================================
# 4. HANDLE INVALID AGE
# ==========================================

df.loc[
    (df["Age"] < 18) | (df["Age"] > 25),
    "Age"
] = pd.NA


# ==========================================
# 5. HANDLE INVALID ATTENDANCE
# ==========================================

df.loc[
    (df["Attendance"] < 0) |
    (df["Attendance"] > 100),
    "Attendance"
] = pd.NA


# ==========================================
# 6. HANDLE INVALID STUDY HOURS
# ==========================================

df.loc[
    df["Study_Hours"] < 0,
    "Study_Hours"
] = pd.NA


# ==========================================
# 7. HANDLE INVALID ASSIGNMENTS
# ==========================================

df.loc[
    (df["Assignments_Completed"] < 0) |
    (df["Assignments_Completed"] > 10),
    "Assignments_Completed"
] = pd.NA


# ==========================================
# 8. HANDLE INVALID MARKS
# ==========================================

subjects = ["Math", "Science", "English"]

for subject in subjects:

    df.loc[
        (df[subject] < 0) |
        (df[subject] > 100),
        subject
    ] = pd.NA


# ==========================================
# 9. HANDLE INVALID PREVIOUS SCORE
# ==========================================

df.loc[
    (df["Previous_Score"] < 0) |
    (df["Previous_Score"] > 100),
    "Previous_Score"
] = pd.NA


# ==========================================
# 10. FILL MISSING NUMERICAL VALUES
# ==========================================

numeric_columns = [
    "Age",
    "Math",
    "Science",
    "English",
    "Attendance",
    "Study_Hours",
    "Assignments_Completed",
    "Previous_Score"
]

for column in numeric_columns:

    df[column] = df[column].fillna(
        df[column].median()
    )


# ==========================================
# 11. CREATE PROCESSED FOLDER
# ==========================================

os.makedirs("data/processed", exist_ok=True)


# ==========================================
# 12. SAVE CLEAN DATA
# ==========================================

df.to_csv(
    "data/processed/students_cleaned.csv",
    index=False
)


# ==========================================
# 13. FINAL QUALITY CHECK
# ==========================================

print("\n===== CLEANING COMPLETE =====")

print("Final rows:", len(df))

print("\nMissing values after cleaning:")
print(df.isna().sum())

print("\nCleaned data preview:")
print(df.head())