import streamlit as st
import datetime
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Project Setup", page_icon="📋", layout="wide")

st.markdown("""
    <style>
    h1, h2, h3 { color: #005F73; }
    </style>
""", unsafe_allow_html=True)

st.title("📋 Project Setup")

col1, col2 = st.columns(2)

with col1:
    title = st.text_input("Project Title", st.session_state.project_details.get("title", ""))
    
    selected_area = st.session_state.project_details.get("area", "Structural Engineering")
    areas = [
        "Structural Engineering", 
        "Geotechnical", 
        "Environmental", 
        "Transportation", 
        "Construction Management"
    ]
    area = st.selectbox("Research Area", areas, index=areas.index(selected_area) if selected_area in areas else 0)
    
with col2:
    start_date = st.date_input("Start Date", st.session_state.project_details.get("start_date", datetime.date.today()))
    end_date = st.date_input("Submission Date", st.session_state.project_details.get("end_date", datetime.date.today() + datetime.timedelta(days=7*16)))

if start_date and end_date:
    total_weeks = (end_date - start_date).days // 7
    st.info(f"**Total weeks available:** {total_weeks}")

if st.button("Save & Generate Timeline"):
    st.session_state.project_details = {
        "title": title,
        "area": area,
        "start_date": start_date,
        "end_date": end_date,
        "total_weeks": total_weeks
    }
    st.success("Project details saved!")

if st.session_state.project_details:
    st.subheader("Recommended Chapter Structure")
    st.markdown("""
    - **Chapter 1: Introduction** (Week 1-2)
    - **Chapter 2: Literature Review** (Week 3-6)
    - **Chapter 3: Methodology** (Week 7-9)
    - **Chapter 4: Results & Analysis** (Week 10-13)
    - **Chapter 5: Conclusions** (Week 14-15)
    - **Final Review & Submission** (Week 16)
    """)
    
    st.subheader("Project Timeline")
    s_date = st.session_state.project_details.get("start_date", datetime.date.today())
    
    tasks = [
        {"Task": "Introduction", "Start": s_date, "Finish": s_date + datetime.timedelta(days=14)},
        {"Task": "Literature Review", "Start": s_date + datetime.timedelta(days=14), "Finish": s_date + datetime.timedelta(days=42)},
        {"Task": "Methodology", "Start": s_date + datetime.timedelta(days=42), "Finish": s_date + datetime.timedelta(days=63)},
        {"Task": "Results & Analysis", "Start": s_date + datetime.timedelta(days=63), "Finish": s_date + datetime.timedelta(days=91)},
        {"Task": "Conclusions", "Start": s_date + datetime.timedelta(days=91), "Finish": s_date + datetime.timedelta(days=105)},
        {"Task": "Final Review", "Start": s_date + datetime.timedelta(days=105), "Finish": s_date + datetime.timedelta(days=112)}
    ]
    df_gantt = pd.DataFrame(tasks)
    
    fig = px.timeline(df_gantt, x_start="Start", x_end="Finish", y="Task", color_discrete_sequence=['#005F73']*len(df_gantt))
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(fig, use_container_width=True)
