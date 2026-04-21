import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Literature Tracker", page_icon="📚", layout="wide")

st.markdown("""
    <style>
    h1, h2, h3 { color: #005F73; }
    </style>
""", unsafe_allow_html=True)

st.title("📚 Literature Tracker")

with st.expander("Add New Reference"):
    with st.form("add_ref_form"):
        col1, col2 = st.columns(2)
        with col1:
            author = st.text_input("Author")
            title = st.text_input("Title")
        with col2:
            year = st.number_input("Year", min_value=1900, max_value=2100, step=1, value=2024)
            relevance = st.selectbox("Relevance", ["High", "Medium", "Low"])
        
        finding = st.text_area("Key Finding")
        submit = st.form_submit_button("Add Reference")
        
        if submit and author and title:
            # Ensure session state is initialized
            if "references" not in st.session_state:
                st.session_state.references = []
                
            st.session_state.references.append({
                "Author": author,
                "Year": year,
                "Title": title,
                "Key Finding": finding,
                "Relevance": relevance
            })
            st.success("Reference added!")

if "references" not in st.session_state:
    st.session_state.references = []

num_refs = len(st.session_state.references)
if num_refs < 20:
    st.warning("⚠️ Minimum 20 references recommended.")
else:
    st.success(f"Great job! You have {num_refs} references logged.")

if st.session_state.references:
    df_refs = pd.DataFrame(st.session_state.references)
    st.dataframe(df_refs, use_container_width=True)
    
    st.subheader("Reference Relevance Summary")
    relevance_counts = df_refs['Relevance'].value_counts().reset_index()
    relevance_counts.columns = ['Relevance', 'Count']
    
    fig = px.pie(relevance_counts, names='Relevance', values='Count', color='Relevance',
                 color_discrete_map={"High": "#005F73", "Medium": "#0A9396", "Low": "#94D2BD"})
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No references added yet. Use the form above to add your first reference.")
