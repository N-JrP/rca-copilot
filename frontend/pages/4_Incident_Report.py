import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/api/report"

st.set_page_config(
    page_title="Incident Report | RCA Copilot",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Incident Postmortem Report")
st.caption("Generate structured postmortem reports from AI-powered incident analysis.")

st.markdown(
    """
    This page turns detected incident metrics and AI root-cause analysis into a
    postmortem-style operational report.
    """
)

if st.button("Generate Incident Report", type="primary"):
    with st.spinner("Generating incident report with local AI..."):
        try:
            response = requests.get(API_URL, timeout=300)
            response.raise_for_status()
            data = response.json()

            st.success(f"Report generated: {data['report_id']}")

            st.markdown(data["report_markdown"])

            st.download_button(
                label="Download Report as Markdown",
                data=data["report_markdown"],
                file_name=f"{data['report_id']}.md",
                mime="text/markdown"
            )

        except requests.exceptions.RequestException as error:
            st.error("Could not generate report. Make sure backend and Ollama are running.")
            st.code(str(error))