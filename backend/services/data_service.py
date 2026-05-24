import pandas as pd
import numpy as np


def generate_incident_data():
    np.random.seed(42)

    timestamps = pd.date_range(
        start="2026-01-01",
        periods=100,
        freq="h"
    )

    api_latency = np.random.normal(220, 15, 100)
    error_rate = np.random.normal(1.5, 0.3, 100)
    conversion_rate = np.random.normal(4.2, 0.4, 100)

    # Simulated incident spike
    api_latency[70:80] += 120
    error_rate[70:80] += 4
    conversion_rate[70:80] -= 1.8

    df = pd.DataFrame({
        "timestamp": timestamps,
        "api_latency": api_latency,
        "error_rate": error_rate,
        "conversion_rate": conversion_rate
    })

    return df