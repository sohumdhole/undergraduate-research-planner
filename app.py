import streamlit as st

st.set_page_config(
    page_title="Undergraduate Research Project Planner",
    page_icon="🎓",
    layout="wide"
)

# Initialize Session State
if "project_details" not in st.session_state:
    st.session_state.project_details = {}
if "references" not in st.session_state:
    st.session_state.references = []
if "meetings" not in st.session_state:
    st.session_state.meetings = []
if "methodology_result" not in st.session_state:
    st.session_state.methodology_result = ""
if "chapter_status" not in st.session_state:
    st.session_state.chapter_status = {
        "Introduction": "Not Started",
        "Literature Review": "Not Started", 
        "Methodology": "Not Started",
        "Results & Analysis": "Not Started",
        "Conclusions": "Not Started"
    }

# ATU Teal Custom CSS
st.markdown("""
    <style>
    .stApp {
        --primary-color: #005F73;
    }
    h1, h2, h3 {
        color: #005F73;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎓 Undergraduate Research Project Planner")
st.subheader("A structured guide for civil engineering final year dissertation students")

st.markdown("""
### Modules Overview

1. **📋 Project Setup**: Define your project parameters and generate a recommended timeline.
2. **📚 Literature Tracker**: Keep track of your references and their relevance to your research.
3. **🔬 Methodology Selector**: Answer a few questions to find the best methodology for your project.
4. **💬 Supervisor Feedback Log**: Document your supervisor meetings and track action items.
5. **📊 Progress Dashboard**: Visualize your overall progress across chapters, references, meetings, and methodology.

---
### Related Tools
This planner complements the Engineering Mathematics Toolkit and the Civil Engineering Mathematics Assessment Tool — three apps designed to support civil engineering students throughout their degree.

* [Engineering Mathematics Toolkit](https://engineering-mathematics-toolkit-atx8ku78wlsyqoqqrzzgew.streamlit.app/)
* [Civil Engineering Mathematics Assessment Tool](https://civil-eng-maths-assessment-8ftjbws28sni9fqkcjxeb2.streamlit.app/)
""")
