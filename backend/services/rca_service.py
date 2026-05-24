import pandas as pd

from backend.core.prompts import RCA_PROMPT_TEMPLATE
from backend.services.ollama_service import generate_with_ollama


def build_incident_summary(df: pd.DataFrame) -> str:
    anomaly_df = df[df["anomaly"] == -1].copy()

    if anomaly_df.empty:
        return "No anomalies detected."

    summary = {
        "anomaly_count": len(anomaly_df),
        "incident_start": str(anomaly_df["timestamp"].min()),
        "incident_end": str(anomaly_df["timestamp"].max()),
        "avg_api_latency": round(anomaly_df["api_latency"].mean(), 2),
        "avg_error_rate": round(anomaly_df["error_rate"].mean(), 2),
        "avg_conversion_rate": round(anomaly_df["conversion_rate"].mean(), 2),
        "max_api_latency": round(anomaly_df["api_latency"].max(), 2),
        "max_error_rate": round(anomaly_df["error_rate"].max(), 2),
        "min_conversion_rate": round(anomaly_df["conversion_rate"].min(), 2),
    }

    return str(summary)


def generate_root_cause_analysis(df: pd.DataFrame) -> dict:
    incident_summary = build_incident_summary(df)

    prompt = RCA_PROMPT_TEMPLATE.format(
        incident_summary=incident_summary
    )

    ai_response = generate_with_ollama(prompt)

    return {
        "incident_summary": incident_summary,
        "ai_analysis": ai_response
    }