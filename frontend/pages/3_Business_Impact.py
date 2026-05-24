import pandas as pd
import requests
import streamlit as st
import plotly.express as px

API_URL = "http://127.0.0.1:8000/api/incidents"

st.set_page_config(
    page_title="Business Impact | RCA Copilot",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Business Impact Analysis")
st.caption("Translate operational incidents into measurable business impact.")

try:
    response = requests.get(API_URL, timeout=20)
    response.raise_for_status()
    data = response.json()

    df = pd.DataFrame(data["records"])
    anomaly_df = df[df["anomaly"] == -1]

    estimated_revenue_loss = round(len(anomaly_df) * 420, 2)
    conversion_drop = round(
        df["conversion_rate"].mean() - anomaly_df["conversion_rate"].mean(),
        2
    )
    avg_latency = round(anomaly_df["api_latency"].mean(), 2)
    avg_error_rate = round(anomaly_df["error_rate"].mean(), 2)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Estimated Revenue Risk", f"€{estimated_revenue_loss}")

    with col2:
        st.metric("Conversion Rate Drop", f"{conversion_drop}%")

    with col3:
        st.metric("Incident Latency", f"{avg_latency} ms")

    with col4:
        st.metric("Incident Error Rate", f"{avg_error_rate}%")

    st.divider()

    left_col, right_col = st.columns([1.3, 1])

    with left_col:
        st.subheader("Business Impact Score")

        impact_data = pd.DataFrame({
            "Metric": [
                "Revenue Risk",
                "Checkout Slowdown",
                "Customer Friction",
                "Conversion Impact"
            ],
            "Impact Score": [88, 91, 76, 84]
        })

        fig = px.bar(
            impact_data,
            x="Metric",
            y="Impact Score",
            text="Impact Score",
            title="Incident impact across business dimensions"
        )
        fig.update_layout(template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    with right_col:
        st.subheader("Executive Summary")

        st.warning(
            "Detected operational anomalies are likely affecting checkout "
            "conversion, customer experience, and revenue reliability."
        )

        st.markdown(
            f"""
            **Key interpretation:**

            - The incident window contains **{len(anomaly_df)} anomalous records**
            - Average API latency during incident: **{avg_latency} ms**
            - Average error rate during incident: **{avg_error_rate}%**
            - Estimated revenue risk: **€{estimated_revenue_loss}**

            **Why it matters:**  
            This page connects engineering signals to business outcomes, which is
            what startup teams need during incident response.
            """
        )

    with st.expander("View incident-only records"):
        st.dataframe(anomaly_df, use_container_width=True)

except requests.exceptions.RequestException:
    st.error(
        "Backend API is not running. Start it with: "
        "`uvicorn backend.main:app --reload`"
    )