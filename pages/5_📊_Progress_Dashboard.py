import streamlit as st
import plotly.graph_objects as go
import datetime

st.set_page_config(page_title="Progress Dashboard", page_icon="📊", layout="wide")

st.markdown("""
    <style>
    h1, h2, h3 { color: #005F73; }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Progress Dashboard")

if "chapter_status" not in st.session_state:
    st.session_state.chapter_status = {
        "Introduction": "Not Started",
        "Literature Review": "Not Started", 
        "Methodology": "Not Started",
        "Results & Analysis": "Not Started",
        "Conclusions": "Not Started"
    }

# Update Chapter Status
st.subheader("Update Chapter Status")
col1, col2, col3, col4, col5 = st.columns(5)
chapters = list(st.session_state.chapter_status.keys())

for i, col in enumerate([col1, col2, col3, col4, col5]):
    with col:
        status = st.selectbox(chapters[i], ["Not Started", "In Progress", "Complete"], 
                              index=["Not Started", "In Progress", "Complete"].index(st.session_state.chapter_status[chapters[i]]),
                              key=f"status_{i}")
        st.session_state.chapter_status[chapters[i]] = status

# Calculate Progress Breakdown
chapter_score = sum(1 for status in st.session_state.chapter_status.values() 
                    if status == "Complete") * 5

num_refs = len(st.session_state.get("references", []))
ref_score = min(25, (num_refs / 20) * 25) if num_refs > 0 else 0

num_meetings = len(st.session_state.get("meetings", []))
meet_score = min(25, (num_meetings / 6) * 25) if num_meetings > 0 else 0

methodology_selected = st.session_state.get("methodology_result", "")
method_score = 25 if methodology_selected != "" else 0

total_progress = int(chapter_score + ref_score + meet_score + method_score)

col_dash1, col_dash2 = st.columns([1, 2])

with col_dash1:
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = total_progress,
        number = {"suffix": "%"},
        title = {'text': "Overall Progress"},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "#005F73"},
            'steps': [
                {'range': [0, 25], 'color': "#e0e0e0"},
                {'range': [25, 50], 'color': "#c0c0c0"},
                {'range': [50, 75], 'color': "#a0a0a0"},
                {'range': [75, 100], 'color': "#808080"}
            ],
        }
    ))
    # Make chart slightly smaller
    fig.update_layout(height=350, margin=dict(l=20, r=20, t=50, b=20))
    st.plotly_chart(fig, use_container_width=True)

with col_dash2:
    st.subheader("Progress Breakdown")
    
    if "project_details" in st.session_state and "end_date" in st.session_state.project_details:
        weeks_rem = (st.session_state.project_details["end_date"] - datetime.date.today()).days // 7
        st.metric("Weeks Remaining", weeks_rem)
    else:
        st.info("Set project dates in the Project Setup page to see weeks remaining.")
        
    st.markdown("### Chapter Status")
    status_html = ""
    for ch, stat in st.session_state.chapter_status.items():
        color = "🔴" if stat == "Not Started" else ("🟡" if stat == "In Progress" else "🟢")
        status_html += f"**{ch}**: {color} {stat}<br>"
    st.markdown(status_html, unsafe_allow_html=True)
    
st.markdown("---")
# Motivational message
if total_progress <= 25:
    st.info("Every great dissertation starts with a single step. You've got this!")
elif total_progress <= 50:
    st.success("Good momentum. Keep pushing forward.")
elif total_progress <= 75:
    st.success("You're over halfway. The finish line is in sight.")
else:
    st.balloons()
    st.success("Outstanding progress. Final push now!")
