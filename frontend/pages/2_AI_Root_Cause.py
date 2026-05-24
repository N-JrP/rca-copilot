import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/api/rca"

st.set_page_config(
    page_title="AI Root Cause | RCA Copilot",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Root Cause Analysis")
st.caption("AI-powered operational reasoning using local LLM inference.")

st.markdown(
    """
    This page sends detected incident metrics to a local LLM through the FastAPI backend
    and generates a root-cause analysis.
    """
)

if st.button("Generate AI Root Cause Analysis", type="primary"):
    with st.spinner("Analyzing incident with local AI..."):
        try:
            response = requests.get(API_URL, timeout=240)
            response.raise_for_status()
            data = response.json()

            st.subheader("Incident Summary")
            st.code(data["incident_summary"])

            st.subheader("AI Analysis")
            st.markdown(data["ai_analysis"])

        except requests.exceptions.RequestException as error:
            st.error("Could not generate RCA. Make sure backend and Ollama are running.")
            st.code(str(error))