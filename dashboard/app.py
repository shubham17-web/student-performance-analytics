import streamlit as st
import pandas as pd


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="📊",
    layout="wide"
)


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #666;
        margin-bottom: 20px;
    }

    .section-title {
        font-size: 25px;
        font-weight: 600;
        margin-top: 25px;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================
# DASHBOARD HEADER
# ==========================================

st.markdown(
    '<div class="main-title">📊 Student Performance Analytics</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Interactive academic analytics dashboard for analyzing
    student performance, academic behavior, department trends,
    and student risk factors.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv(
    "reports/complete_student_risk_analysis.csv"
)


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🎛️ Dashboard Controls")

st.sidebar.markdown(
    """
    Use the controls below to explore
    student performance data.
    """
)

st.sidebar.divider()


# ==========================================
# DEPARTMENT FILTER
# ==========================================

st.sidebar.header("🔎 Filters")

departments = ["All Departments"] + sorted(
    df["Department"].unique().tolist()
)


selected_department = st.sidebar.selectbox(
    "Select Department",
    departments
)


# ==========================================
# FILTER DATA
# ==========================================

if selected_department == "All Departments":

    filtered_df = df.copy()

else:

    filtered_df = df[
        df["Department"] == selected_department
    ].copy()


st.sidebar.write(
    f"Students shown: {len(filtered_df)}"
)


# ==========================================
# STUDENT SELECTOR
# ==========================================

st.sidebar.subheader("👤 Student Profile")


student_options = (
    filtered_df["Student_ID"]
    + " - "
    + filtered_df["Name"]
)


selected_student = st.sidebar.selectbox(
    "Select Student",
    student_options
)


selected_student_id = (
    selected_student.split(" - ")[0]
)


student = filtered_df[
    filtered_df["Student_ID"] == selected_student_id
].iloc[0]


# ==========================================
# KEY PERFORMANCE INDICATORS
# ==========================================

st.markdown(
    '<div class="section-title">📈 Performance Overview</div>',
    unsafe_allow_html=True
)


total_students = len(filtered_df)


passed_students = (
    filtered_df["STATUS"] == "PASS"
).sum()


failed_students = (
    filtered_df["STATUS"] == "FAIL"
).sum()


at_risk_students = (
    filtered_df["Risk_Score"] > 0
).sum()


average_performance = (
    filtered_df["AVERAGE"].mean()
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "👨‍🎓 Total Students",
        total_students
    )


with col2:

    st.metric(
        "✅ Passed",
        passed_students
    )


with col3:

    st.metric(
        "❌ Failed",
        failed_students
    )


with col4:

    st.metric(
        "📊 Average Performance",
        f"{average_performance:.2f}"
    )


# ==========================================
# INDIVIDUAL STUDENT PROFILE
# ==========================================

st.markdown(
    '<div class="section-title">👤 Student Profile</div>',
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Student",
        student["Name"]
    )


with col2:

    st.metric(
        "Average",
        f"{student['AVERAGE']:.2f}"
    )


with col3:

    st.metric(
        "Grade",
        student["GRADE"]
    )


with col4:

    st.metric(
        "Rank",
        int(student["Rank"])
    )


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Attendance",
        f"{student['Attendance']:.0f}%"
    )


with col2:

    st.metric(
        "Study Hours",
        f"{student['Study_Hours']:.0f}"
    )


with col3:

    st.metric(
        "Previous Score",
        f"{student['Previous_Score']:.0f}"
    )


with col4:

    st.metric(
        "Risk Level",
        student["Risk_Level"]
    )


# ==========================================
# STUDENT SUBJECT PERFORMANCE
# ==========================================

st.markdown(
    '<div class="section-title">📚 Student Subject Performance</div>',
    unsafe_allow_html=True
)


student_subjects = pd.DataFrame(
    {
        "Subject": [
            "Math",
            "Science",
            "English"
        ],
        "Marks": [
            student["Math"],
            student["Science"],
            student["English"]
        ]
    }
)


st.bar_chart(
    student_subjects.set_index("Subject")
)


# ==========================================
# STUDENT RISK INFORMATION
# ==========================================

if student["Risk_Score"] > 0:

    st.warning(
        f"⚠️ This student is classified as "
        f"{student['Risk_Level']} risk."
    )


    st.write(
        "**Risk Score:**",
        int(student["Risk_Score"])
    )


    reasons = []


    if student["AVERAGE"] < 50:

        reasons.append(
            "Low Average"
        )


    if student["Attendance"] < 60:

        reasons.append(
            "Low Attendance"
        )


    if student["Study_Hours"] < 8:

        reasons.append(
            "Low Study Hours"
        )


    if student["Previous_Score"] < 50:

        reasons.append(
            "Low Previous Score"
        )


    st.write(
        "**Risk Reasons:**",
        ", ".join(reasons)
    )

else:

    st.success(
        "✅ No major risk factors detected "
        "for this student."
    )


# ==========================================
# SUBJECT PERFORMANCE
# ==========================================

st.markdown(
    '<div class="section-title">📚 Department Subject Performance</div>',
    unsafe_allow_html=True
)


subject_averages = {
    "Math": filtered_df["Math"].mean(),
    "Science": filtered_df["Science"].mean(),
    "English": filtered_df["English"].mean()
}


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Mathematics",
        f"{subject_averages['Math']:.2f}"
    )


with col2:

    st.metric(
        "Science",
        f"{subject_averages['Science']:.2f}"
    )


with col3:

    st.metric(
        "English",
        f"{subject_averages['English']:.2f}"
    )


st.bar_chart(
    pd.DataFrame(
        subject_averages,
        index=["Average Marks"]
    ).T
)


# ==========================================
# PERFORMANCE DISTRIBUTION
# ==========================================

st.markdown(
    '<div class="section-title">📈 Performance Distribution</div>',
    unsafe_allow_html=True
)


performance_data = filtered_df[
    [
        "Math",
        "Science",
        "English",
        "AVERAGE"
    ]
]


st.line_chart(
    performance_data
)


# ==========================================
# AT-RISK STUDENT ANALYSIS
# ==========================================

st.markdown(
    '<div class="section-title">⚠️ At-Risk Student Analysis</div>',
    unsafe_allow_html=True
)


risk_counts = (
    filtered_df["Risk_Level"]
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


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "🟢 Low Risk",
        risk_counts["LOW"]
    )


with col2:

    st.metric(
        "🟡 Medium Risk",
        risk_counts["MEDIUM"]
    )


with col3:

    st.metric(
        "🔴 High Risk",
        risk_counts["HIGH"]
    )


# ==========================================
# RISK DISTRIBUTION CHART
# ==========================================

st.bar_chart(
    risk_counts
)


# ==========================================
# AT-RISK STUDENT TABLE
# ==========================================

at_risk_df = filtered_df[
    filtered_df["Risk_Score"] > 0
].copy()


# ==========================================
# GENERATE RISK REASONS
# ==========================================

def get_risk_reasons(row):

    reasons = []


    if row["AVERAGE"] < 50:

        reasons.append(
            "Low Average"
        )


    if row["Attendance"] < 60:

        reasons.append(
            "Low Attendance"
        )


    if row["Study_Hours"] < 8:

        reasons.append(
            "Low Study Hours"
        )


    if row["Previous_Score"] < 50:

        reasons.append(
            "Low Previous Score"
        )


    return ", ".join(reasons)


at_risk_df["Risk_Reason"] = (
    at_risk_df.apply(
        get_risk_reasons,
        axis=1
    )
)


# ==========================================
# DISPLAY AT-RISK STUDENTS
# ==========================================

st.subheader(
    "🚨 Students Requiring Attention"
)


st.dataframe(
    at_risk_df[
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
    ],
    use_container_width=True
)


# ==========================================
# AUTOMATED INSIGHTS
# ==========================================

st.markdown(
    '<div class="section-title">🧠 Automated Insights</div>',
    unsafe_allow_html=True
)


# ==========================================
# BASIC CALCULATIONS
# ==========================================

total_students = len(filtered_df)


at_risk_count = (
    filtered_df["Risk_Score"] > 0
).sum()


high_risk_count = (
    filtered_df["Risk_Level"] == "HIGH"
).sum()


average_performance = (
    filtered_df["AVERAGE"].mean()
)


# ==========================================
# BEST DEPARTMENT
# ==========================================

department_performance = (
    filtered_df
    .groupby("Department")["AVERAGE"]
    .mean()
    .sort_values(
        ascending=False
    )
)


# ==========================================
# CORRELATIONS
# ==========================================

attendance_correlation = (
    filtered_df["Attendance"]
    .corr(
        filtered_df["AVERAGE"]
    )
)


study_correlation = (
    filtered_df["Study_Hours"]
    .corr(
        filtered_df["AVERAGE"]
    )
)


# ==========================================
# INSIGHT 1 — PERFORMANCE
# ==========================================

if average_performance >= 80:

    st.success(
        f"📈 Overall performance is strong. "
        f"The average score is "
        f"{average_performance:.2f}."
    )

elif average_performance >= 60:

    st.info(
        f"📊 Overall performance is moderate. "
        f"The average score is "
        f"{average_performance:.2f}."
    )

else:

    st.warning(
        f"⚠️ Overall performance needs attention. "
        f"The average score is "
        f"{average_performance:.2f}."
    )


# ==========================================
# INSIGHT 2 — STUDY HOURS
# ==========================================

if study_correlation >= 0.5:

    st.success(
        f"📚 Study hours have a strong positive "
        f"relationship with performance "
        f"(correlation: "
        f"{study_correlation:.2f})."
    )

elif study_correlation >= 0.3:

    st.info(
        f"📚 Study hours have a moderate "
        f"relationship with performance "
        f"(correlation: "
        f"{study_correlation:.2f})."
    )

else:

    st.warning(
        f"📚 Study hours show a weak "
        f"relationship with performance "
        f"(correlation: "
        f"{study_correlation:.2f})."
    )


# ==========================================
# INSIGHT 3 — ATTENDANCE
# ==========================================

if attendance_correlation >= 0.5:

    st.success(
        f"🗓️ Attendance has a strong positive "
        f"relationship with performance "
        f"(correlation: "
        f"{attendance_correlation:.2f})."
    )

elif attendance_correlation >= 0.3:

    st.info(
        f"🗓️ Attendance has a moderate "
        f"relationship with performance "
        f"(correlation: "
        f"{attendance_correlation:.2f})."
    )

else:

    st.warning(
        f"🗓️ Attendance shows a weak "
        f"relationship with performance "
        f"(correlation: "
        f"{attendance_correlation:.2f})."
    )


# ==========================================
# INSIGHT 4 — RISK
# ==========================================

if at_risk_count > 0:

    st.warning(
        f"⚠️ {at_risk_count} out of "
        f"{total_students} students have at least "
        f"one identified risk factor."
    )

else:

    st.success(
        "✅ No students currently have "
        "identified risk factors."
    )


# ==========================================
# INSIGHT 5 — HIGH RISK
# ==========================================

if high_risk_count > 0:

    st.error(
        f"🚨 {high_risk_count} student(s) are "
        f"classified as HIGH risk and may "
        f"require immediate attention."
    )


# ==========================================
# INSIGHT 6 — BEST DEPARTMENT
# ==========================================

if len(department_performance) > 0:

    best_department = (
        department_performance.idxmax()
    )


    best_department_average = (
        department_performance.max()
    )


    st.info(
        f"🏆 {best_department} is the "
        f"highest-performing department with "
        f"an average score of "
        f"{best_department_average:.2f}."
    )


# ==========================================
# DATASET TABLE
# ==========================================

st.markdown(
    '<div class="section-title">📋 Student Data</div>',
    unsafe_allow_html=True
)


st.dataframe(
    filtered_df,
    use_container_width=True
)


# ==========================================
# FOOTER
# ==========================================

st.divider()


st.caption(
    "Student Performance Analytics • "
    "Built with Python, Pandas, NumPy, "
    "Matplotlib, Seaborn & Streamlit"
)