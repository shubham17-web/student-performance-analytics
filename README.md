# 📊 Student Performance Analytics

An end-to-end student performance analytics project built with
Python, Pandas, NumPy, Matplotlib, Seaborn, and Streamlit.

The project analyzes academic performance, identifies at-risk
students, studies relationships between academic factors, and
provides an interactive dashboard for exploring the results.

---

## 🚀 Features

### 📊 Performance Analysis

- Calculate total marks and average marks
- Identify top-performing students
- Analyze subject-wise performance
- Calculate department-level performance
- Generate student rankings

### ⚠️ Student Risk Detection

The project identifies students who may require additional
academic attention using multiple factors:

- Low average marks
- Low attendance
- Low study hours
- Low previous score

Each student receives:

- Risk Score
- Risk Level
- Risk Reason

Risk levels:

- LOW
- MEDIUM
- HIGH

### 📈 Statistical Analysis

The project analyzes relationships between:

- Attendance and performance
- Study hours and performance
- Previous score and performance
- Subject marks
- Other numerical student factors

Correlation analysis and a correlation heatmap are generated
to understand these relationships.

### 📊 Data Visualization

The project generates:

- Department performance chart
- Attendance vs performance chart
- Study hours vs performance chart
- Correlation heatmap
- Grade distribution chart
- Risk distribution chart

### 🖥️ Interactive Streamlit Dashboard

The dashboard provides:

- Department filtering
- Student selection
- KPI metrics
- Individual student profiles
- Subject performance charts
- Risk analysis
- Automated insights
- Interactive student data table

---

## 📊 Power BI Dashboard

The project also includes an interactive Power BI dashboard for deeper
student performance and risk analysis.

### Power BI Features

- Student performance KPIs
- Average score and pass percentage
- Top student identification
- Department performance analysis
- Grade distribution
- Risk-level analysis
- High-risk student identification
- Risk factor analysis
- Student performance details
- Interactive slicers and filters
- Performance Analysis page
- Risk Analysis page

### Power BI Report Pages

- **Overview Dashboard** — overall student performance and key metrics
- **Performance Analysis** — department, grade, and individual student analysis
- **Risk Analysis** — at-risk students, high-risk students, and risk factors

📁 **Power BI File:** [Student Performance Analytics](powerbi/Student_Performance_Analytics.pbix)

---

## 🗂️ Project Structure

```text
student-performance-project/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── students.csv
│
├── reports/
│   ├── figures/
│   ├── analysis_report.txt
│   ├── at_risk_students.csv
│   ├── complete_student_risk_analysis.csv
│   └── validation_report.txt
│
├── src/
│   ├── __init__.py
│   ├── analysis.py
│   ├── config.py
│   ├── risk_analysis.py
│   └── validation.py
│
├── dashboard/
│   └── app.py
│
├── powerbi/                         ← NEW
│   └── Student_Performance_Analytics.pbix
│
├── generate_data.py
├── clean_data.py
├── main.py
├── visualization.py
├── requirements.txt
└── README.md