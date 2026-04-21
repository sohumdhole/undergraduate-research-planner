import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

st.set_page_config(page_title="Supervisor Feedback Log", page_icon="💬", layout="wide")

st.markdown("""
    <style>
    h1, h2, h3 { color: #005F73; }
    </style>
""", unsafe_allow_html=True)

st.title("💬 Supervisor Feedback Log")

if "meetings" not in st.session_state:
    st.session_state.meetings = []

with st.expander("Log a Meeting"):
    with st.form("meeting_form"):
        col1, col2 = st.columns(2)
        with col1:
            m_date = st.date_input("Meeting Date", datetime.date.today())
            topics = st.text_area("Topics Discussed")
        with col2:
            action_items = st.text_area("Action Items")
            deadline = st.date_input("Deadline for Action Items", datetime.date.today() + datetime.timedelta(days=7))
            
        submit = st.form_submit_button("Log Meeting")
        
        if submit and topics:
            st.session_state.meetings.append({
                "Date": m_date,
                "Topics": topics,
                "Action Items": action_items,
                "Deadline": deadline
            })
            st.success("Meeting logged!")

num_meetings = len(st.session_state.meetings)
if num_meetings < 6:
    st.warning("⚠️ Minimum 6 supervisor meetings recommended throughout the project.")
else:
    st.success(f"Great! You have logged {num_meetings} meetings.")

if st.session_state.meetings:
    df_meetings = pd.DataFrame(st.session_state.meetings)
    df_meetings['Date'] = pd.to_datetime(df_meetings['Date'])
    
    st.subheader("Meeting Timeline")
    fig = px.scatter(
        df_meetings,
        x="Date",
        y=[1]*len(df_meetings),
        hover_data=["Topics", "Action Items"],
        color_discrete_sequence=["#005F73"]
    )
    fig.update_traces(marker=dict(size=15))
    fig.update_layout(
        yaxis=dict(visible=False, showticklabels=False),
        xaxis_title="Meeting Date",
        title="Supervisor Meeting Timeline"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Meeting Log & Action Items")
    
    today = datetime.date.today()
    for row in st.session_state.meetings:
        with st.container():
            st.markdown(f"**Date:** {row['Date'].strftime('%Y-%m-%d') if isinstance(row['Date'], datetime.date) else row['Date']}")
            st.markdown(f"**Topics Discussed:** {row['Topics']}")
            st.markdown(f"**Action Items:** {row['Action Items']}")
            
            deadline = row['Deadline']
            if isinstance(deadline, str):
                deadline = datetime.date.fromisoformat(deadline)
            if deadline < today:
                st.error(f"🔴 Overdue! Deadline was {deadline}")
            else:
                st.info(f"⏳ Deadline: {deadline}")
            st.markdown("---")
else:
    st.info("No meetings logged yet.")
