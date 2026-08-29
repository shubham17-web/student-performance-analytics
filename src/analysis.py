# ==========================================
# TOP STUDENT
# ==========================================

def get_top_student(complete_students):

    return complete_students.loc[
        complete_students["Total"].idxmax()
    ]


# ==========================================
# TOP STUDENT BY SUBJECT
# ==========================================

def get_subject_toppers(complete_students):

    math_top = complete_students.loc[
        complete_students["Math"].idxmax()
    ]

    science_top = complete_students.loc[
        complete_students["Science"].idxmax()
    ]

    english_top = complete_students.loc[
        complete_students["English"].idxmax()
    ]

    return {
        "Math": math_top,
        "Science": science_top,
        "English": english_top
    }


# ==========================================
# SUBJECT AVERAGES
# ==========================================

def get_subject_averages(complete_students):

    return {
        "Math": complete_students["Math"].mean(),
        "Science": complete_students["Science"].mean(),
        "English": complete_students["English"].mean()
    }


# ==========================================
# DEPARTMENT ANALYSIS
# ==========================================

def get_department_analysis(complete_students):

    return (
        complete_students
        .groupby("Department")
        .agg(
            Students=("Student_ID", "count"),
            Average_Math=("Math", "mean"),
            Average_Science=("Science", "mean"),
            Average_English=("English", "mean"),
            Average_Overall=("AVERAGE", "mean")
        )
    )