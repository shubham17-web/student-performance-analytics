# Student Performance Analytics

A Python-based student performance analytics project built using Pandas, NumPy, Matplotlib, and Seaborn.

## Project Overview

This project analyzes student academic and behavioral data to identify performance patterns, department-level trends, and students who may be at academic risk.

The project includes data validation, performance analysis, risk detection, statistical analysis, visualization, and automated report generation.

## Features

- Data validation
- Missing-value detection
- Duplicate Student ID detection
- Marks validation
- Attendance validation
- Student performance calculation
- Grade classification
- Student ranking
- Subject-wise analysis
- Department performance analysis
- At-risk student detection
- Risk scoring
- Risk-level classification
- Correlation analysis
- Data visualization
- Automated analysis reports
- Data quality reports

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Dataset

The dataset contains 200 student records with information including:

- Student ID
- Name
- Age
- Department
- Math marks
- Science marks
- English marks
- Attendance
- Study hours
- Assignments completed
- Previous score

## Project Structure

```text
student-performance-project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── __init__.py
│   ├── analysis.py
│   ├── risk_analysis.py
│   ├── validation.py
│   └── config.py
│
├── reports/
│   ├── figures/
│   ├── analysis_report.txt
│   ├── validation_report.txt
│   ├── at_risk_students.csv
│   └── complete_student_risk_analysis.csv
│
├── main.py
├── visualization.py
├── requirements.txt
└── README.md