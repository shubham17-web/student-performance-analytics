import pandas as pd

from src.config import (
    AVERAGE_RISK_THRESHOLD,
    ATTENDANCE_RISK_THRESHOLD,
    STUDY_HOURS_RISK_THRESHOLD,
    PREVIOUS_SCORE_RISK_THRESHOLD,
    AVERAGE_RISK_POINTS,
    ATTENDANCE_RISK_POINTS,
    STUDY_HOURS_RISK_POINTS,
    PREVIOUS_SCORE_RISK_POINTS,
    HIGH_RISK_THRESHOLD,
    MEDIUM_RISK_THRESHOLD
)

# ==========================================
# CREATE RISK REASONS
# ==========================================

def get_risk_reasons(row):

    reasons = []

    if row["AVERAGE"] < AVERAGE_RISK_THRESHOLD:
        reasons.append("Low Average")

    if row["Attendance"] < ATTENDANCE_RISK_THRESHOLD:
        reasons.append("Low Attendance")

    if row["Study_Hours"] < STUDY_HOURS_RISK_THRESHOLD:
        reasons.append("Low Study Hours")

    if row["Previous_Score"] < PREVIOUS_SCORE_RISK_THRESHOLD:
        reasons.append("Low Previous Score")

    return ", ".join(reasons)


# ==========================================
# CALCULATE RISK SCORE
# ==========================================

def calculate_risk_score(row):

    score = 0

    if row["AVERAGE"] < AVERAGE_RISK_THRESHOLD:
        score += AVERAGE_RISK_POINTS

    if row["Attendance"] < ATTENDANCE_RISK_THRESHOLD:
        score += ATTENDANCE_RISK_POINTS

    if row["Study_Hours"] < STUDY_HOURS_RISK_THRESHOLD:
        score += STUDY_HOURS_RISK_POINTS

    if row["Previous_Score"] < PREVIOUS_SCORE_RISK_THRESHOLD:
        score += PREVIOUS_SCORE_RISK_POINTS

    return score


# ==========================================
# GET RISK LEVEL
# ==========================================

def get_risk_level(score):

   if score >= HIGH_RISK_THRESHOLD:
    return "HIGH"

   elif score >= MEDIUM_RISK_THRESHOLD:
    return "MEDIUM"

   else:
    return "LOW"


# ==========================================
# ANALYZE STUDENT RISK
# ==========================================

def analyze_risk(complete_students):

    complete_students = complete_students.copy()

    complete_students["Risk_Score"] = (
        complete_students.apply(
            calculate_risk_score,
            axis=1
        )
    )

    complete_students["Risk_Level"] = (
        complete_students["Risk_Score"]
        .apply(get_risk_level)
    )

    at_risk_students = complete_students[
        complete_students["Risk_Score"] > 0
    ].copy()

    at_risk_students["Risk_Reason"] = (
        at_risk_students.apply(
            get_risk_reasons,
            axis=1
        )
    )

    return (
        complete_students,
        at_risk_students
    )