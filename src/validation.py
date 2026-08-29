# ==========================================
# DATA VALIDATION
# ==========================================

def validate_data(df):

    errors = []

    # ==========================================
    # REQUIRED COLUMNS
    # ==========================================

    required_columns = [
        "Student_ID",
        "Name",
        "Age",
        "Department",
        "Math",
        "Science",
        "English",
        "Attendance",
        "Study_Hours",
        "Assignments_Completed",
        "Previous_Score"
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:

        errors.append(
            f"Missing columns: {missing_columns}"
        )

        return False, errors


    # ==========================================
    # MISSING VALUES
    # ==========================================

    missing_values = df.isna().sum()

    for column, count in missing_values.items():

        if count > 0:

            # Subject marks are allowed to be missing
            if column in ["Math", "Science", "English"]:

                continue

            errors.append(
                f"{column}: "
                f"{count} missing values"
            )


    # ==========================================
    # DUPLICATE STUDENT IDs
    # ==========================================

    duplicate_ids = df[
        df["Student_ID"].duplicated()
    ]

    if len(duplicate_ids) > 0:

        errors.append(
            f"Duplicate Student IDs found: "
            f"{len(duplicate_ids)}"
        )


    # ==========================================
    # DATA TYPE VALIDATION
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

        if not df[column].dtype.kind in "iuf":

            errors.append(
                f"{column}: "
                f"Expected numeric data type"
            )


    # ==========================================
    # MARKS VALIDATION
    # ==========================================

    subjects = [
        "Math",
        "Science",
        "English"
    ]

    for subject in subjects:

        invalid_marks = (
            (df[subject] < 0)
            | (df[subject] > 100)
        ).sum()

        if invalid_marks > 0:

            errors.append(
                f"{subject}: "
                f"{invalid_marks} invalid marks"
            )


    # ==========================================
    # ATTENDANCE VALIDATION
    # ==========================================

    invalid_attendance = (
        (df["Attendance"] < 0)
        | (df["Attendance"] > 100)
    ).sum()

    if invalid_attendance > 0:

        errors.append(
            f"Attendance: "
            f"{invalid_attendance} invalid values"
        )


    # ==========================================
    # AGE VALIDATION
    # ==========================================

    invalid_age = (
        (df["Age"] < 15)
        | (df["Age"] > 100)
    ).sum()

    if invalid_age > 0:

        errors.append(
            f"Age: "
            f"{invalid_age} invalid values"
        )


    # ==========================================
    # STUDY HOURS VALIDATION
    # ==========================================

    invalid_study_hours = (
        df["Study_Hours"] < 0
    ).sum()

    if invalid_study_hours > 0:

        errors.append(
            f"Study Hours: "
            f"{invalid_study_hours} invalid values"
        )


    # ==========================================
    # ASSIGNMENTS VALIDATION
    # ==========================================

    invalid_assignments = (
        df["Assignments_Completed"] < 0
    ).sum()

    if invalid_assignments > 0:

        errors.append(
            f"Assignments Completed: "
            f"{invalid_assignments} invalid values"
        )


    # ==========================================
    # PREVIOUS SCORE VALIDATION
    # ==========================================

    invalid_previous_score = (
        (df["Previous_Score"] < 0)
        | (df["Previous_Score"] > 100)
    ).sum()

    if invalid_previous_score > 0:

        errors.append(
            f"Previous Score: "
            f"{invalid_previous_score} invalid values"
        )


    # ==========================================
    # FINAL RESULT
    # ==========================================

    if len(errors) > 0:

        return False, errors

    return True, []

# ==========================================
# VALIDATION REPORT
# ==========================================

def create_validation_report(df, errors):

    import os

    os.makedirs(
        "reports",
        exist_ok=True
    )

    # ==========================================
    # BASIC COUNTS
    # ==========================================

    total_rows = len(df)

    duplicate_ids = (
        df["Student_ID"].duplicated()
    ).sum()

    total_missing_values = (
        df.isna().sum().sum()
    )


    # ==========================================
    # INVALID MARKS
    # ==========================================

    subjects = [
        "Math",
        "Science",
        "English"
    ]

    invalid_marks = 0

    for subject in subjects:

        invalid_marks += (
            (df[subject] < 0)
            | (df[subject] > 100)
        ).sum()


    # ==========================================
    # INVALID ATTENDANCE
    # ==========================================

    invalid_attendance = (
        (df["Attendance"] < 0)
        | (df["Attendance"] > 100)
    ).sum()


    # ==========================================
    # INVALID AGE
    # ==========================================

    invalid_age = (
        (df["Age"] < 15)
        | (df["Age"] > 100)
    ).sum()


    # ==========================================
    # VALIDATION STATUS
    # ==========================================

    if errors:

        status = "FAILED"

    else:

        status = "PASSED"


    # ==========================================
    # CREATE REPORT
    # ==========================================

    with open(
        "reports/validation_report.txt",
        "w"
    ) as file:

        file.write(
            "DATA QUALITY VALIDATION REPORT\n"
        )

        file.write(
            "=" * 45 + "\n\n"
        )

        file.write(
            f"Total Rows: "
            f"{total_rows}\n"
        )

        file.write(
            f"Duplicate Student IDs: "
            f"{duplicate_ids}\n"
        )

        file.write(
            f"Total Missing Values: "
            f"{total_missing_values}\n"
        )

        file.write(
            f"Invalid Marks: "
            f"{invalid_marks}\n"
        )

        file.write(
            f"Invalid Attendance: "
            f"{invalid_attendance}\n"
        )

        file.write(
            f"Invalid Ages: "
            f"{invalid_age}\n"
        )

        file.write(
            f"\nValidation Status: "
            f"{status}\n"
        )


        # ==========================================
        # ERROR DETAILS
        # ==========================================

        if errors:

            file.write(
                "\n===== ERRORS =====\n"
            )

            for error in errors:

                file.write(
                    f"- {error}\n"
                )


    print(
        "\nValidation report saved to:"
        " reports/validation_report.txt"
    )