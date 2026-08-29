import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# ==========================================
# CREATE FIGURE FOLDER
# ==========================================

os.makedirs(
    "reports/figures",
    exist_ok=True
)


# ==========================================
# LOAD ANALYZED DATA
# ==========================================

df = pd.read_csv(
    "reports/complete_student_risk_analysis.csv"
)


# ==========================================
# LOAD ORIGINAL CLEAN DATA
# ==========================================

all_students = pd.read_csv(
    "data/processed/students_cleaned.csv"
)


# ==========================================
# CALCULATE TOTAL AND AVERAGE
# ==========================================

all_students["Total"] = (
    all_students["Math"]
    + all_students["Science"]
    + all_students["English"]
)

all_students["AVERAGE"] = (
    all_students["Total"] / 3
)


# ==========================================
# IDENTIFY INCOMPLETE STUDENTS
# ==========================================

missing_marks = (
    all_students[
        ["Math", "Science", "English"]
    ]
    .isna()
    .any(axis=1)
)


all_students["STATUS"] = "COMPLETE"

all_students.loc[
    missing_marks,
    "STATUS"
] = "INCOMPLETE"


# ==========================================
# BASIC DATASET STATISTICS
# ==========================================

total_students = len(all_students)

complete_students_count = (
    all_students["STATUS"] == "COMPLETE"
).sum()

incomplete_students_count = (
    all_students["STATUS"] == "INCOMPLETE"
).sum()


# ==========================================
# PASS / FAIL
# ==========================================

passed_students = (
    df["STATUS"] == "PASS"
).sum()

failed_students = (
    df["STATUS"] == "FAIL"
).sum()


# ==========================================
# PASS RATE
# ==========================================

pass_rate = (
    passed_students
    / complete_students_count
) * 100


# ==========================================
# DEPARTMENT PERFORMANCE
# ==========================================

department_average = (
    df.groupby("Department")["AVERAGE"]
    .mean()
    .sort_values(
        ascending=False
    )
)


print("\n===== DEPARTMENT AVERAGES =====")

print(
    department_average.round(2)
)


# ==========================================
# DEPARTMENT PERFORMANCE CHART
# ==========================================

plt.figure(figsize=(8, 5))

sns.barplot(
    x=department_average.index,
    y=department_average.values
)

plt.title(
    "Average Performance by Department"
)

plt.xlabel("Department")

plt.ylabel("Average Marks")

plt.ylim(0, 100)

plt.tight_layout()

plt.savefig(
    "reports/figures/department_performance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()


# ==========================================
# ATTENDANCE VS PERFORMANCE
# ==========================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Attendance",
    y="AVERAGE"
)

plt.title(
    "Attendance vs Student Performance"
)

plt.xlabel("Attendance (%)")

plt.ylabel("Average Marks")

plt.xlim(0, 100)

plt.ylim(0, 100)

plt.tight_layout()

plt.savefig(
    "reports/figures/attendance_vs_performance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()


# ==========================================
# CORRELATION ANALYSIS
# ==========================================

attendance_correlation = (
    df["Attendance"]
    .corr(df["AVERAGE"])
)


print(
    "\n===== CORRELATION ANALYSIS ====="
)

print(
    "Attendance vs Performance:",
    round(
        attendance_correlation,
        2
    )
)


# ==========================================
# STUDY HOURS VS PERFORMANCE
# ==========================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="AVERAGE"
)

plt.title(
    "Study Hours vs Student Performance"
)

plt.xlabel(
    "Study Hours per Week"
)

plt.ylabel(
    "Average Marks"
)

plt.ylim(0, 100)

plt.tight_layout()

plt.savefig(
    "reports/figures/study_hours_vs_performance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()


# ==========================================
# STUDY HOURS CORRELATION
# ==========================================

study_correlation = (
    df["Study_Hours"]
    .corr(df["AVERAGE"])
)


print(
    "\nStudy Hours vs Performance:",
    round(
        study_correlation,
        2
    )
)


# ==========================================
# CORRELATION HEATMAP
# ==========================================

numeric_columns = [
    "Age",
    "Math",
    "Science",
    "English",
    "Attendance",
    "Study_Hours",
    "Assignments_Completed",
    "Previous_Score",
    "AVERAGE"
]


correlation_matrix = (
    df[numeric_columns]
    .corr()
)


print(
    "\n===== CORRELATION MATRIX ====="
)

print(
    correlation_matrix.round(2)
)


plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0
)

plt.title(
    "Correlation Between Student Performance Factors"
)

plt.tight_layout()

plt.savefig(
    "reports/figures/correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()


# ==========================================
# GRADE DISTRIBUTION
# ==========================================

grade_counts = (
    df["GRADE"]
    .value_counts()
    .reindex(
        ["A+", "A", "B", "C", "D", "F"],
        fill_value=0
    )
)


print(
    "\n===== GRADE DISTRIBUTION ====="
)

print(
    grade_counts
)


# ==========================================
# GRADE DISTRIBUTION CHART
# ==========================================

plt.figure(figsize=(8, 5))

sns.barplot(
    x=grade_counts.index,
    y=grade_counts.values
)

plt.title(
    "Student Grade Distribution"
)

plt.xlabel("Grade")

plt.ylabel(
    "Number of Students"
)

plt.tight_layout()

plt.savefig(
    "reports/figures/grade_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()


# ==========================================
# RISK DISTRIBUTION
# ==========================================

risk_counts = (
    df["Risk_Level"]
    .value_counts()
    .reindex(
        ["LOW", "MEDIUM", "HIGH"],
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
# RISK DISTRIBUTION CHART
# ==========================================

plt.figure(figsize=(8, 5))

sns.barplot(
    x=risk_counts.index,
    y=risk_counts.values
)

plt.title(
    "Student Risk Level Distribution"
)

plt.xlabel("Risk Level")

plt.ylabel(
    "Number of Students"
)

plt.tight_layout()

plt.savefig(
    "reports/figures/risk_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()


# ==========================================
# RISK STATISTICS
# ==========================================

low_risk = risk_counts["LOW"]

medium_risk = risk_counts["MEDIUM"]

high_risk = risk_counts["HIGH"]

at_risk_students = (
    medium_risk
    + high_risk
)

risk_percentage = (
    at_risk_students
    / complete_students_count
) * 100


# ==========================================
# TOP STUDENT
# ==========================================

top_student_index = (
    df["AVERAGE"].idxmax()
)

top_student = (
    df.loc[top_student_index]
)


# ==========================================
# BEST DEPARTMENT
# ==========================================

best_department = (
    department_average.idxmax()
)

best_department_average = (
    department_average.max()
)


# ==========================================
# OVERALL AVERAGE
# ==========================================

overall_average = (
    df["AVERAGE"].mean()
)


# ==========================================
# EXECUTIVE INSIGHTS
# ==========================================

if study_correlation > attendance_correlation:

    stronger_factor = "Study Hours"

else:

    stronger_factor = "Attendance"


# ==========================================
# AUTOMATED ANALYSIS REPORT
# ==========================================

with open(
    "reports/analysis_report.txt",
    "w"
) as file:

    file.write(
        "STUDENT PERFORMANCE ANALYTICS REPORT\n"
    )

    file.write(
        "=" * 50 + "\n\n"
    )


    # --------------------------------------
    # EXECUTIVE SUMMARY
    # --------------------------------------

    file.write(
        "===== EXECUTIVE SUMMARY =====\n\n"
    )

    file.write(
        f"Total Students: "
        f"{total_students}\n"
    )

    file.write(
        f"Complete Students: "
        f"{complete_students_count}\n"
    )

    file.write(
        f"Incomplete Students: "
        f"{incomplete_students_count}\n"
    )

    file.write(
        f"Passed Students: "
        f"{passed_students}\n"
    )

    file.write(
        f"Failed Students: "
        f"{failed_students}\n"
    )

    file.write(
        f"Pass Rate: "
        f"{pass_rate:.2f}%\n"
    )

    file.write(
        f"Overall Average: "
        f"{overall_average:.2f}\n\n"
    )


    # --------------------------------------
    # TOP STUDENT
    # --------------------------------------

    file.write(
        "===== TOP STUDENT =====\n\n"
    )

    file.write(
        f"Name: "
        f"{top_student['Name']}\n"
    )

    file.write(
        f"Student ID: "
        f"{top_student['Student_ID']}\n"
    )

    file.write(
        f"Department: "
        f"{top_student['Department']}\n"
    )

    file.write(
        f"Average: "
        f"{top_student['AVERAGE']:.2f}\n"
    )

    file.write(
        f"Total Marks: "
        f"{top_student['Total']:.0f}\n\n"
    )


    # --------------------------------------
    # BEST DEPARTMENT
    # --------------------------------------

    file.write(
        "===== BEST DEPARTMENT =====\n\n"
    )

    file.write(
        f"Department: "
        f"{best_department}\n"
    )

    file.write(
        f"Average Performance: "
        f"{best_department_average:.2f}\n\n"
    )


    # --------------------------------------
    # DEPARTMENT AVERAGES
    # --------------------------------------

    file.write(
        "===== DEPARTMENT AVERAGES =====\n\n"
    )

    for department, average in (
        department_average.items()
    ):

        file.write(
            f"{department}: "
            f"{average:.2f}\n"
        )


    # --------------------------------------
    # CORRELATION ANALYSIS
    # --------------------------------------

    file.write(
        "\n===== CORRELATION ANALYSIS =====\n\n"
    )

    file.write(
        f"Attendance vs Performance: "
        f"{attendance_correlation:.2f}\n"
    )

    file.write(
        f"Study Hours vs Performance: "
        f"{study_correlation:.2f}\n"
    )

    file.write(
        f"Stronger Relationship: "
        f"{stronger_factor}\n"
    )


    # --------------------------------------
    # GRADE DISTRIBUTION
    # --------------------------------------

    file.write(
        "\n===== GRADE DISTRIBUTION =====\n\n"
    )

    for grade in [
        "A+",
        "A",
        "B",
        "C",
        "D",
        "F"
    ]:

        count = grade_counts.get(
            grade,
            0
        )

        file.write(
            f"{grade}: {count}\n"
        )


    # --------------------------------------
    # RISK ANALYSIS
    # --------------------------------------

    file.write(
        "\n===== RISK ANALYSIS =====\n\n"
    )

    file.write(
        f"Low Risk: "
        f"{low_risk}\n"
    )

    file.write(
        f"Medium Risk: "
        f"{medium_risk}\n"
    )

    file.write(
        f"High Risk: "
        f"{high_risk}\n"
    )

    file.write(
        f"At-Risk Students: "
        f"{at_risk_students}\n"
    )

    file.write(
        f"At-Risk Percentage: "
        f"{risk_percentage:.2f}%\n"
    )


    # --------------------------------------
    # KEY INSIGHTS
    # --------------------------------------

    file.write(
        "\n===== KEY INSIGHTS =====\n\n"
    )

    file.write(
        f"1. {best_department} has the "
        f"highest average departmental "
        f"performance ({best_department_average:.2f}).\n"
    )

    file.write(
        f"2. {stronger_factor} has the "
        f"stronger correlation with "
        f"student performance.\n"
    )

    file.write(
        f"3. {at_risk_students} students "
        f"are classified as medium or "
        f"high risk.\n"
    )

    file.write(
        f"4. {incomplete_students_count} "
        f"students have incomplete "
        f"academic records.\n"
    )


# ==========================================
# FINAL MESSAGE
# ==========================================

print(
    "\n===== REPORT GENERATED ====="
)

print(
    "Report saved to: "
    "reports/analysis_report.txt"
)