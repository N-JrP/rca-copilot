from sklearn.ensemble import IsolationForest


def detect_anomalies(df):

    features = df[[
        "api_latency",
        "error_rate",
        "conversion_rate"
    ]]

    model = IsolationForest(
        contamination=0.1,
        random_state=42
    )

    df["anomaly"] = model.fit_predict(features)

    return df