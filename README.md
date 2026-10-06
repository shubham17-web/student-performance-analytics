# Student Performance Analytics

An end-to-end Data Analytics project built with Python that analyzes student academic performance, identifies at-risk students using a transparent rule-based scoring system, generates visual reports, and presents results through an interactive **Streamlit** dashboard and a **Power BI** dashboard.

> **Note:** The dataset used in this project is **synthetic (generated) student data**. It does not contain real student information.

---

## Overview

This project transforms raw student data into cleaned and validated data, performs performance analysis, flags students who may need academic support, and delivers the findings through two separate presentation layers: a Python-based Streamlit app and a Power BI report.

## Project Objective

Build an end-to-end student analytics pipeline that:

1. Transforms raw student data into cleaned and validated data
2. Performs performance analysis (scores, grades, rankings, department and subject comparisons)
3. Identifies at-risk students using a transparent, rule-based risk scoring system
4. Creates visualizations and automated reports
5. Presents results through Streamlit and Power BI

## Features

- Synthetic data generation with raw and processed data stored separately
- Data cleaning and validation (missing values, duplicate IDs, schema, numeric checks, consistency)
- Performance metrics: total marks, average score, PASS / FAIL / INCOMPLETE status, grades, ranking
- Subject, department, and top-student analysis
- Rule-based risk scoring with human-readable risk reasons
- Correlation analysis between study habits and performance
- Six saved visualizations
- Automated CSV and text reports
- Interactive Streamlit dashboard with filters
- Multi-page Power BI dashboard with DAX measures

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Dashboards | Streamlit, Power BI |
| BI Calculations | DAX |
| Version Control | Git, GitHub |

## Project Architecture / Workflow

```
Raw Data
   → Data Cleaning
   → Data Validation
   → Performance Analysis
   → Risk Analysis
   → Visualization
   → Automated Reports
   → Streamlit Dashboard
   → Power BI Dashboard
```

**Workflow steps**

1. Generate student data
2. Store raw data
3. Clean the data
4. Validate the cleaned dataset
5. Calculate performance metrics
6. Assign grades and rankings
7. Analyze departments and subjects
8. Detect at-risk students
9. Calculate risk score and risk level
10. Generate visualizations
11. Generate reports
12. Load analytical data into Streamlit
13. Build Power BI dashboard
14. Publish and version the project using GitHub

## Dataset

- **Type:** Synthetic / generated student dataset
- **Size:** 200 student records
- **Student IDs:** `S001`, `S002`, ...
- **Fields:** Math, Science, English, Attendance, Study Hours, Assignments Completed, Previous Score, Department, Age
- **Storage:** Raw data (`data/raw/`) and processed data (`data/processed/`) are kept separately so the original data is never overwritten.

## Data Cleaning & Validation

The pipeline checks and handles:

- Missing values
- Duplicate Student IDs
- Required columns / schema
- Numeric data validation
- Data consistency
- Separation of incomplete records from the complete-student analysis

**Why it matters:** Analysis built on duplicated, malformed, or incomplete records produces unreliable averages, rankings, and risk flags. Validating the data before analysis helps ensure that downstream results are trustworthy and reproducible.

## Performance Analysis

The project calculates:

- Total marks and average score
- PASS / FAIL / INCOMPLETE status
- Grades
- Student ranking
- Subject averages
- Department performance
- Top-performing students

**Grade rules**

| Grade | Average |
|---|---|
| A+ | ≥ 90 |
| A | ≥ 80 |
| B | ≥ 70 |
| C | ≥ 60 |
| D | ≥ 50 |
| F | < 50 |
| N/A | Incomplete records |

**Status rules**

- **PASS:** Average ≥ 40
- **FAIL:** Average < 40
- **INCOMPLETE:** Required subject marks are missing

## Risk Detection

The project uses a **transparent rule-based risk scoring system** rather than a predictive model, so every flag can be traced back to a specific condition. This makes the results easy to explain and audit.

**Risk conditions**

| Condition | Points |
|---|---|
| Average < 50 | +3 |
| Attendance < 60 | +2 |
| Study Hours < 8 | +2 |
| Previous Score < 50 | +2 |

**Risk levels**

| Level | Rule |
|---|---|
| HIGH | Risk Score ≥ 5 |
| MEDIUM | Risk Score ≥ 3 |
| LOW | Risk Score < 3 |

The system also generates risk reasons for each student: *Low Average Score*, *Low Attendance*, *Low Study Hours*, and *Low Previous Score*.

## Visualizations

- Department performance bar chart
- Grade distribution chart
- Risk distribution chart
- Attendance vs Performance scatter plot
- Study Hours vs Performance scatter plot
- Correlation heatmap

Figures are saved to `reports/figures/`. Automated outputs also include the at-risk student CSV, the complete student risk analysis CSV, and a text analysis report.

## Streamlit Dashboard

**Why Streamlit:** It provides an interactive web interface for exploring the Python-based analysis without requiring a separate frontend framework.

**KPI cards:** Total Students, Average Score, Passed Students, At-Risk Students, High-Risk Students, Top Student

**Filters:** Department, Grade, Risk Level, Status

**Views:**
- Department performance
- Grade distribution
- Study Hours vs Average Score
- Attendance vs Average Score
- Risk distribution
- Risk factor analysis
- High-risk student table
- Student details table

## Power BI Dashboard

The Power BI report is a separate presentation layer built on the processed analytical dataset.

**Pages:** Overview Dashboard, Risk Analysis, Performance Analysis

**Content:** KPI cards, department performance, grade distribution, risk level distribution, student details, high-risk student analysis, risk factor analysis, interactive slicers, and page navigation.

**DAX concepts used:** `CALCULATE`, `COUNTROWS`, `AVERAGE`, `DIVIDE`, `SELECTEDVALUE`, `SWITCH`, `VAR / RETURN`

**Why DAX:** DAX is used to create dynamic measures and calculations that respond to Power BI filter context.

Power BI can load the generated processed and report CSV files (for example, `complete_student_risk_analysis.csv`).

## Key Results

| Metric | Value |
|---|---|
| Total students | 200 |
| Passed | 197 |
| Failed | 3 |
| Incomplete (final complete analysis output) | 0 |
| Overall average | 64.99 |
| Math average | 65.36 |
| Science average | 65.07 |
| English average | 64.54 |
| Best department | ME (approx. 67.47 average) |
| At-risk students | 92 |
| Risk levels | LOW: 170 · MEDIUM: 11 · HIGH: 19 |

**Correlation analysis**

| Relationship | Correlation |
|---|---|
| Attendance vs Performance | 0.23 |
| Study Hours vs Performance | 0.59 |

> These values describe **associations only**. Correlation does not imply causation, and no causal conclusion about attendance or study hours is made. The data is also synthetic, so these figures should not be generalized to real student populations.

## Project Structure

```
student-performance-project/
│
├── data/
│   ├── raw/
│   │   └── students_raw.csv
│   └── processed/
│       └── students_cleaned.csv
│
├── reports/
│   ├── figures/
│   ├── at_risk_students.csv
│   ├── complete_student_risk_analysis.csv
│   └── analysis_report.txt
│
├── dashboard/
│   └── app.py
│
├── generate_data.py
├── clean_data.py
├── main.py
├── visualization.py
├── requirements.txt
├── .gitignore
└── README.md
```

**Main files**

| File | Purpose |
|---|---|
| `generate_data.py` | Generates the synthetic student dataset |
| `clean_data.py` | Cleans and validates the raw dataset |
| `main.py` | Performs analysis, ranking, grading, and risk analysis |
| `visualization.py` | Generates charts and automated analysis reports |
| `dashboard/app.py` | Streamlit interactive dashboard |
| `reports/` | Stores generated analytical outputs |
| `data/raw/` | Original generated dataset |
| `data/processed/` | Cleaned dataset |

## Installation

```bash
# Create a virtual environment
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## How to Run

Run the scripts in this order, since each step depends on the output of the previous one:

```bash
python generate_data.py
python clean_data.py
python main.py
python visualization.py
streamlit run dashboard/app.py
```

For Power BI, load the generated processed/report CSV files from `data/processed/` and `reports/`.

## GitHub / Live Demo

- **GitHub Repository:** [Add GitHub URL]
- **Live Streamlit Dashboard:** [Add Streamlit URL]

## Learning Outcomes

This project demonstrates:

- Python data analysis
- Pandas data manipulation
- NumPy numerical operations
- Data cleaning and validation
- Exploratory analysis
- Statistical correlation
- Data visualization
- Rule-based risk analysis
- Dashboard development (Streamlit)
- Power BI and DAX
- Git / GitHub
- End-to-end analytics workflow

## Future Improvements

- Add automated tests for the cleaning and validation steps
- Make risk thresholds configurable instead of fixed in code
- Validate the approach on real, anonymized data
- Deploy the Streamlit dashboard publicly

---

*This is a Data Analytics / BI portfolio project. Risk detection is rule-based and does not use machine learning.*
