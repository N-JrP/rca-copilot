import streamlit as st

st.set_page_config(
    page_title="RCA Copilot",
    page_icon="🧠",
    layout="wide"
)

st.sidebar.title("RCA Copilot")
st.sidebar.caption("AI Incident Intelligence Platform")

st.title("🧠 RCA Copilot")
st.subheader("AI-Powered Incident Intelligence for Startup Operations")

st.markdown("""
Modern startup infrastructure produces thousands of operational signals.

RCA Copilot helps engineering and operations teams:
- detect anomalies
- analyze root causes
- estimate business impact
- generate incident reports

using local AI models with zero cloud API cost.
""")

st.divider()

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:
    st.metric(
        label="Incident Accuracy",
        value="92%"
    )

with metric2:
    st.metric(
        label="AI Analysis Time",
        value="12 sec"
    )

with metric3:
    st.metric(
        label="Cloud API Cost",
        value="€0"
    )

with metric4:
    st.metric(
        label="Local AI",
        value="Enabled"
    )

st.divider()

left_col, right_col = st.columns([1.3, 1])

with left_col:

    st.markdown("## Platform Capabilities")

    st.markdown("""
### 🔍 AI Incident Analysis
- Root-cause reasoning with local LLMs
- AI-generated operational summaries
- Actionable remediation recommendations
- Incident postmortem generation

### 📊 Operational Intelligence
- Real-time anomaly detection
- API latency monitoring
- Error-rate tracking
- Conversion-impact analysis

### 🔒 Local-First AI
- Ollama local inference
- Zero cloud inference cost
- Offline AI capability
- Privacy-friendly architecture
""")

with right_col:

    st.markdown("## Product Positioning")

    st.info("""
RCA Copilot is designed as a lightweight AI operations platform for startups.

The system combines:
- FastAPI backend APIs
- Streamlit SaaS frontend
- Scikit-learn anomaly detection
- Local Ollama AI reasoning
- Operational business intelligence
""")

    st.success("""
Built for:
- AI Engineers
- Data Engineers
- Startup Infrastructure Teams
- Platform Operations
""")

st.divider()

st.caption(
    "Built with FastAPI · Streamlit · Ollama · Scikit-learn · Plotly"
)