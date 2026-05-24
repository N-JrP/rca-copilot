import streamlit as st

st.set_page_config(
    page_title="Architecture | RCA Copilot",
    page_icon="🏗️",
    layout="wide"
)

st.title("Platform Architecture")
st.caption("Local-first AI SaaS architecture for incident intelligence")

st.markdown("""
# RCA Copilot Architecture

RCA Copilot is designed as a lightweight local-first AI operations platform.

The system combines:
- FastAPI backend services
- Streamlit SaaS frontend
- Local Ollama LLM inference
- Scikit-learn anomaly detection
- Operational metrics analysis
- AI-generated incident reasoning

---

# Architecture Flow

Operational Metrics
↓
Anomaly Detection Engine
↓
Incident Classification
↓
Ollama Local LLM
↓
AI Root Cause Analysis
↓
Business Impact Estimation
↓
Incident Postmortem Report

---

# Backend Stack

- FastAPI
- Python
- Scikit-learn
- Pandas
- Requests
- Ollama Local API

---

# Frontend Stack

- Streamlit
- Plotly
- Interactive operational dashboards
- SaaS-style multi-page UI

---

# AI Layer

The AI reasoning layer uses local LLM inference through Ollama.

Benefits:
- Zero cloud API cost
- Local data privacy
- Offline AI capability
- Startup-friendly infrastructure cost

---

# Product Vision

RCA Copilot explores how local AI systems can help startups:
- detect operational incidents
- understand root causes
- estimate business impact
- accelerate incident response
""")