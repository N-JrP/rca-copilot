from fastapi import APIRouter
from backend.services.data_service import generate_incident_data
from backend.services.anomaly_service import detect_anomalies

router = APIRouter()


@router.get("/incidents")
def get_incidents():
    df = generate_incident_data()
    df = detect_anomalies(df)

    df["timestamp"] = df["timestamp"].astype(str)

    return {
        "records": df.to_dict(orient="records"),
        "total_records": len(df),
        "anomaly_count": int((df["anomaly"] == -1).sum())
    }