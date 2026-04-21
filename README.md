# Undergraduate Research Project Planner

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://undergraduate-research-planner.streamlit.app)

A structured dissertation planning tool designed specifically for civil engineering final year students. This app guides students through every stage of the research process — from initial project setup through to final submission — while giving lecturers visibility into student progress.

---

## 📌 Overview

Final year dissertations are complex, long-running projects that require careful planning, consistent supervision, and structured progress tracking. This tool provides a five-module digital planner that keeps students organised and on track throughout the entire process.

---

## 🧰 Features

### 📋 Project Setup
- Enter project title, research area, start date, and submission date
- Automatically calculates total weeks available
- Generates a recommended chapter-by-chapter timeline
- Displays an interactive Gantt chart of the full dissertation schedule
- Research areas: Structural Engineering, Geotechnical, Environmental, Transportation, Construction Management

### 📚 Literature Review Tracker
- Log references with: Author, Year, Title, Key Finding, Relevance (High/Medium/Low)
- Displays all references as a sortable dataframe
- Pie chart showing reference distribution by relevance level
- Warns when fewer than 20 references have been logged

### 🔬 Methodology Selector
- Four-question decision tool to identify the correct research methodology
- Recommends one of five approaches:
  - Quantitative Experimental
  - Quantitative Survey-Based
  - Qualitative Case Study
  - Mixed Methods
  - Secondary Data Analysis
- Displays a Sankey decision flow diagram showing the chosen research path

### 💬 Supervisor Feedback Log
- Log supervisor meetings with: Date, Topics Discussed, Action Items, Deadline
- Visual meeting timeline using Plotly
- Flags overdue action items in red
- Warns when fewer than 6 meetings have been logged (recommended minimum)

### 📊 Progress Dashboard
- Overall completion percentage based on four components:
  - Chapters drafted (5 × 5% = 25% max)
  - References logged (target 20+, 25% max)
  - Meetings held (target 6+, 25% max)
  - Methodology confirmed (25%)
- Interactive circular gauge showing overall progress
- Weeks remaining countdown (pulls from Project Setup dates)
- Traffic light status per chapter: 🔴 Not Started / 🟡 In Progress / 🟢 Complete
- Motivational message based on progress level

---

## 🚀 Getting Started

### Run Locally

```bash
# Clone the repository
git clone https://github.com/sohumdhole/undergraduate-research-planner.git
cd undergraduate-research-planner

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### Requirements
```
streamlit
plotly
pandas
numpy
```

---

## 📁 Project Structure

```
undergraduate-research-planner/
├── app.py                              # Landing page and session state initialisation
├── requirements.txt
└── pages/
    ├── 1_📋_Project_Setup.py           # Project parameters and Gantt chart
    ├── 2_📚_Literature_Tracker.py      # Reference logging and relevance tracking
    ├── 3_🔬_Methodology.py             # Methodology recommendation engine
    ├── 4_💬_Feedback_Log.py            # Supervisor meeting log
    └── 5_📊_Progress_Dashboard.py      # Overall progress gauge and chapter status
```

---

## 🔗 Part of a Wider Teaching Platform

This app is the third component of a three-app civil engineering student support platform:

| App | Purpose | Link |
|---|---|---|
| Engineering Mathematics Toolkit | Interactive concept teaching across 5 maths modules | [Visit App](https://engineering-mathematics-toolkit-atx8ku78wlsyqoqqrzzgew.streamlit.app/) |
| Civil Eng Maths Assessment Tool | Applied problem bank, diagnostic testing, and cohort analytics | [Visit App](https://civil-eng-maths-assessment-8ftjbws28sni9fqkcjxeb2.streamlit.app/) |
| Undergraduate Research Project Planner | Dissertation planning, supervision tracking, and progress monitoring | This repository |

Students use all three apps across their degree — the Toolkit to learn mathematics, the Assessment Tool to test their knowledge, and this Planner to manage their final year dissertation.

---

## 👨‍💻 Author

**Sohum Dhole**
MSc Business Analytics | BE Electronics Engineering
[GitHub](https://github.com/sohumdhole) · [LinkedIn](https://linkedin.com/in/sohumdhole)
