import pandas as pd
import numpy as np
import os

from src.risk_analysis import analyze_risk

from src.analysis import (
    get_top_student,
    get_subject_toppers,
    get_subject_averages,
    get_department_analysis
)

from src.validation import (
    validate_data,
    create_validation_report
)

# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_csv(
    "data/processed/students_cleaned.csv"
)

# ==========================================
# DATA VALIDATION
# ==========================================

is_valid, validation_errors = validate_data(df)

create_validation_report(
    df,
    validation_errors
)


if not is_valid:

    print("\n===== DATA VALIDATION FAILED =====")

    for error in validation_errors:

        print("-", error)

    raise ValueError(
        "Dataset contains invalid data."
    )


print(
    "\n===== DATA VALIDATION PASSED ====="
)

# ==========================================
# 2. CALCULATE TOTAL AND AVERAGE
# ==========================================

df["Total"] = (
    df["Math"]
    + df["Science"]
    + df["English"]
)

df["AVERAGE"] = df["Total"] / 3


# ==========================================
# 3. CHECK MISSING MARKS
# ==========================================

missing_marks = (
    df[["Math", "Science", "English"]]
    .isna()
    .any(axis=1)
)


# ==========================================
# 4. STATUS
# ==========================================

df["STATUS"] = np.where(
    missing_marks,
    "INCOMPLETE",
    np.where(
        df["AVERAGE"] >= 40,
        "PASS",
        "FAIL"
    )
)


# ==========================================
# 5. GRADE
# ==========================================

conditions = [
    df["AVERAGE"] >= 90,
    df["AVERAGE"] >= 80,
    df["AVERAGE"] >= 70,
    df["AVERAGE"] >= 60,
    df["AVERAGE"] >= 50
]

choices = [
    "A+",
    "A",
    "B",
    "C",
    "D"
]

df["GRADE"] = np.select(
    conditions,
    choices,
    default="F"
)


# Students with missing marks
# should not receive a grade

df.loc[
    missing_marks,
    "GRADE"
] = "N/A"


# ==========================================
# 6. SORT STUDENTS BY TOTAL
# ==========================================

df = df.sort_values(
    "Total",
    ascending=False
)


# ==========================================
# 7. CREATE RANK
# ==========================================

df["Rank"] = range(
    1,
    len(df) + 1
)


# ==========================================
# 8. RESET INDEX
# ==========================================

df = df.reset_index(
    drop=True
)


# ==========================================
# 9. COMPLETE STUDENTS
# ==========================================

complete_students = (
    df[~missing_marks]
    .copy()
)


# ==========================================
# 10. TOP STUDENT
# ==========================================

top_student = get_top_student(
    complete_students
)


print("\n===== TOP STUDENT =====")

print(
    "Name:",
    top_student["Name"]
)

print(
    "Total:",
    top_student["Total"]
)

print(
    "Average:",
    round(
        top_student["AVERAGE"],
        2
    )
)


# ==========================================
# 11. TOP PERFORMERS BY SUBJECT
# ==========================================

print(
    "\n===== TOP PERFORMERS ====="
)


subject_toppers = get_subject_toppers(
    complete_students
)


# ------------------------------------------
# MATH
# ------------------------------------------

math_top = subject_toppers["Math"]

print("\nMath:")

print(
    "Student:",
    math_top["Name"]
)

print(
    "Marks:",
    math_top["Math"]
)


# ------------------------------------------
# SCIENCE
# ------------------------------------------

science_top = subject_toppers["Science"]

print("\nScience:")

print(
    "Student:",
    science_top["Name"]
)

print(
    "Marks:",
    science_top["Science"]
)


# ------------------------------------------
# ENGLISH
# ------------------------------------------

english_top = subject_toppers["English"]

print("\nEnglish:")

print(
    "Student:",
    english_top["Name"]
)

print(
    "Marks:",
    english_top["English"]
)


# ==========================================
# 12. FINAL DATA
# ==========================================

print(
    "\n===== FINAL STUDENT DATA ====="
)

print(df)


# ==========================================
# 13. PERFORMANCE REPORT
# ==========================================

print(
    "\n===== PERFORMANCE REPORT ====="
)

print(
    "Total Students:",
    len(df)
)

print(
    "Passed Students:",
    (df["STATUS"] == "PASS").sum()
)

print(
    "Failed Students:",
    (df["STATUS"] == "FAIL").sum()
)

print(
    "Incomplete Students:",
    (df["STATUS"] == "INCOMPLETE").sum()
)


# ==========================================
# 14. SUBJECT AVERAGES
# ==========================================

print(
    "\n===== SUBJECT AVERAGES ====="
)


subject_averages = get_subject_averages(
    complete_students
)


print(
    "Math:",
    round(
        subject_averages["Math"],
        2
    )
)

print(
    "Science:",
    round(
        subject_averages["Science"],
        2
    )
)

print(
    "English:",
    round(
        subject_averages["English"],
        2
    )
)


print(
    "\nOverall Class Average:",
    round(
        complete_students["AVERAGE"].mean(),
        2
    )
)


# ==========================================
# 15. DEPARTMENT ANALYSIS
# ==========================================

department_analysis = (
    get_department_analysis(
        complete_students
    )
)


print(
    "\n===== DEPARTMENT PERFORMANCE ====="
)

print(
    department_analysis.round(2)
)


# ==========================================
# 16. RISK ANALYSIS
# ==========================================

complete_students, at_risk_students = (
    analyze_risk(
        complete_students
    )
)


# ==========================================
# 17. DISPLAY AT-RISK STUDENTS
# ==========================================

print(
    "\n===== AT-RISK STUDENTS ====="
)


print(
    at_risk_students[
        [
            "Student_ID",
            "Name",
            "Department",
            "AVERAGE",
            "Attendance",
            "Study_Hours",
            "Previous_Score",
            "Risk_Score",
            "Risk_Level",
            "Risk_Reason"
        ]
    ]
)


print(
    f"\nAt-risk students identified: "
    f"{len(at_risk_students)}"
)


# ==========================================
# 18. RISK DISTRIBUTION
# ==========================================

risk_counts = (
    complete_students["Risk_Level"]
    .value_counts()
    .reindex(
        [
            "LOW",
            "MEDIUM",
            "HIGH"
        ],
        fill_value=0
    )
)


print(
    "\n===== RISK DISTRIBUTION ====="
)

print(
    risk_counts
)


# ==========================================
# 19. CREATE REPORT FOLDERS
# ==========================================

os.makedirs(
    "reports",
    exist_ok=True
)


# ==========================================
# 20. SAVE AT-RISK STUDENTS
# ==========================================

at_risk_students.to_csv(
    "reports/at_risk_students.csv",
    index=False
)


# ==========================================
# 21. SAVE COMPLETE RISK ANALYSIS
# ==========================================

complete_students.to_csv(
    "reports/complete_student_risk_analysis.csv",
    index=False
)


# ==========================================
# 22. CONFIRM FILES
# ==========================================

print(
    "\nSaved at-risk students to:"
    " reports/at_risk_students.csv"
)

print(
    "Saved complete risk analysis to:"
    " reports/complete_student_risk_analysis.csv"
)