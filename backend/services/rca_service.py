import pandas as pd

from backend.core.prompts import RCA_PROMPT_TEMPLATE
from backend.services.ollama_service import generate_with_ollama


def build_incident_summary(df: pd.DataFrame) -> dict:
    anomaly_df = df[df["anomaly"] == -1].copy()

    if anomaly_df.empty:
        return {
            "anomaly_count": 0,
            "incident_start": "N/A",
            "incident_end": "N/A",
            "avg_api_latency": 0,
            "avg_error_rate": 0,
            "avg_conversion_rate": 0,
            "max_api_latency": 0,
            "max_error_rate": 0,
            "min_conversion_rate": 0
        }

    return {
        "anomaly_count": int(len(anomaly_df)),
        "incident_start": str(anomaly_df["timestamp"].min()),
        "incident_end": str(anomaly_df["timestamp"].max()),
        "avg_api_latency": round(float(anomaly_df["api_latency"].mean()), 2),
        "avg_error_rate": round(float(anomaly_df["error_rate"].mean()), 2),
        "avg_conversion_rate": round(float(anomaly_df["conversion_rate"].mean()), 2),
        "max_api_latency": round(float(anomaly_df["api_latency"].max()), 2),
        "max_error_rate": round(float(anomaly_df["error_rate"].max()), 2),
        "min_conversion_rate": round(float(anomaly_df["conversion_rate"].min()), 2),
    }


def generate_root_cause_analysis(df: pd.DataFrame) -> dict:
    incident_summary = build_incident_summary(df)

    prompt = RCA_PROMPT_TEMPLATE.format(
        incident_summary=incident_summary
    )

    ai_analysis = generate_with_ollama(prompt)

    return {
        "incident_summary": incident_summary,
        "ai_analysis": ai_analysis
    }