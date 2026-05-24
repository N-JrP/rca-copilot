import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/api/rca"

st.set_page_config(
    page_title="AI Root Cause Analysis | RCA Copilot",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Root Cause Analysis")
st.caption("AI-powered operational reasoning using local LLM inference.")

st.markdown("""
This module sends detected operational incident metrics to a local LLM through
the FastAPI backend and generates structured root-cause analysis.
""")

st.divider()

if st.button("Generate AI Root Cause Analysis", type="primary"):

    with st.spinner("Running local AI operational analysis..."):

        try:
            response = requests.get(API_URL, timeout=300)
            response.raise_for_status()

            data = response.json()

            summary = data["incident_summary"]

            st.subheader("Incident Overview")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Anomalies",
                    summary["anomaly_count"]
                )

            with col2:
                st.metric(
                    "Avg API Latency",
                    f"{summary['avg_api_latency']} ms"
                )

            with col3:
                st.metric(
                    "Avg Error Rate",
                    f"{summary['avg_error_rate']}%"
                )

            with col4:
                st.metric(
                    "Conversion Rate",
                    f"{summary['avg_conversion_rate']}%"
                )

            st.divider()

            st.subheader("AI Operational Analysis")

            st.markdown(data["ai_analysis"])

            st.success(
                "Local AI analysis completed successfully using Ollama."
            )

        except requests.exceptions.RequestException as error:

            st.error(
                "Could not connect to backend API. "
                "Make sure FastAPI and Ollama are running."
            )

            st.code(str(error))