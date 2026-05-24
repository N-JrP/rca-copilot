import requests
import pandas as pd
import plotly.express as px
import streamlit as st

API_URL = "http://127.0.0.1:8000/api/incidents"

st.set_page_config(
    page_title="Incident Dashboard | RCA Copilot",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Incident Operations Dashboard")
st.caption("Monitor operational health, detect anomalies, and inspect incident patterns.")

try:
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    data = response.json()

    df = pd.DataFrame(data["records"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["incident_status"] = df["anomaly"].apply(
        lambda x: "Anomaly" if x == -1 else "Normal"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total records", data["total_records"])

    with col2:
        st.metric("Anomalies detected", data["anomaly_count"])

    with col3:
        anomaly_rate = round((data["anomaly_count"] / data["total_records"]) * 100, 2)
        st.metric("Anomaly rate", f"{anomaly_rate}%")

    st.divider()

    st.subheader("API Latency Over Time")
    fig_latency = px.line(
        df,
        x="timestamp",
        y="api_latency",
        color="incident_status",
        markers=True,
        title="API latency trend"
    )
    fig_latency.update_layout(template="plotly_dark")
    st.plotly_chart(fig_latency, use_container_width=True)

    st.subheader("Error Rate Over Time")
    fig_error = px.line(
        df,
        x="timestamp",
        y="error_rate",
        color="incident_status",
        markers=True,
        title="Error rate trend"
    )
    fig_error.update_layout(template="plotly_dark")
    st.plotly_chart(fig_error, use_container_width=True)

    st.subheader("Conversion Rate Over Time")
    fig_conversion = px.line(
        df,
        x="timestamp",
        y="conversion_rate",
        color="incident_status",
        markers=True,
        title="Conversion rate trend"
    )
    fig_conversion.update_layout(template="plotly_dark")
    st.plotly_chart(fig_conversion, use_container_width=True)

    with st.expander("View raw incident records"):
        st.dataframe(df, use_container_width=True)

except requests.exceptions.RequestException:
    st.error(
        "Backend API is not running. Start it with: "
        "`uvicorn backend.main:app --reload`"
    )