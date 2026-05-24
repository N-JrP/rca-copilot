from fastapi import APIRouter

from backend.services.data_service import generate_incident_data
from backend.services.anomaly_service import detect_anomalies
from backend.services.rca_service import generate_root_cause_analysis
from backend.services.report_service import generate_incident_report

router = APIRouter()


@router.get("/rca")
def get_root_cause_analysis():
    df = generate_incident_data()
    df = detect_anomalies(df)

    result = generate_root_cause_analysis(df)

    return {
        "incident_summary": result["incident_summary"],
        "ai_analysis": str(result["ai_analysis"])
    }


@router.get("/report")
def get_incident_report():
    df = generate_incident_data()
    df = detect_anomalies(df)

    rca_result = generate_root_cause_analysis(df)

    report = generate_incident_report(
        ai_analysis=str(rca_result["ai_analysis"]),
        incident_summary=str(rca_result["incident_summary"])
    )

    return report