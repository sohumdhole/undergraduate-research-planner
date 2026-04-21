import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Methodology Selector", page_icon="🔬", layout="wide")

st.markdown("""
    <style>
    h1, h2, h3 { color: #005F73; }
    </style>
""", unsafe_allow_html=True)

st.title("🔬 Methodology Selector")

st.markdown("Answer the questions below to receive a methodology recommendation.")

if "methodology_result" not in st.session_state:
    st.session_state.methodology_result = ""

with st.form("methodology_form"):
    q1 = st.radio("1. Are you collecting new data?", ["Yes", "No"])
    q2 = st.radio("2. Is your data numerical or descriptive?", ["Quantitative", "Qualitative", "Mixed"])
    q3 = st.selectbox("3. Primary data collection method?", ["Surveys", "Experiments", "Existing Data", "Site Observations"])
    q4 = st.radio("4. Do you need statistical analysis?", ["Yes", "No"])
    
    submit_btn = st.form_submit_button("Get Recommendation")

if submit_btn:
    recommendation = ""
    explanation = ""
    
    if q1 == "No":
        recommendation = "Secondary Data Analysis"
        explanation = "Since you are not collecting new data, you will be analysing existing datasets or literature."
    elif q2 == "Mixed":
        recommendation = "Mixed Methods"
        explanation = "You are working with both numerical and descriptive data, requiring a combination of quantitative and qualitative analytical approaches."
    elif q2 == "Qualitative" or q3 == "Site Observations":
        recommendation = "Qualitative Case Study"
        explanation = "Your focus is on descriptive data and potentially observing specific cases or sites without emphasis on numerical modeling."
    elif q3 == "Surveys":
        recommendation = "Quantitative Survey-Based"
        explanation = "You are collecting numerical data primarily through surveys to gather responses from a sample."
    else:
        recommendation = "Quantitative Experimental"
        explanation = "You are gathering numerical data through experiments, typical for physical or structural tests needing statistical validation."
        
    st.session_state.methodology_result = recommendation
    
    st.success(f"### Recommended Approach: {recommendation}")
    st.info(explanation)
    
    node_labels = ["Start", q1, q2, q3, q4, recommendation]
    fig = go.Figure(data=[go.Sankey(
        node = dict(
          pad = 15,
          thickness = 20,
          line = dict(color = "black", width = 0.5),
          label = node_labels,
          color = "#005F73"
        ),
        link = dict(
          source = [0, 1, 2, 3, 4],
          target = [1, 2, 3, 4, 5],
          value = [1, 1, 1, 1, 1],
          color = "#94D2BD"
        )
    )])
    fig.update_layout(title_text="Decision Flow", font_size=10)
    st.plotly_chart(fig, use_container_width=True)

elif st.session_state.methodology_result:
    st.info(f"Previously selected methodology: **{st.session_state.methodology_result}**")
