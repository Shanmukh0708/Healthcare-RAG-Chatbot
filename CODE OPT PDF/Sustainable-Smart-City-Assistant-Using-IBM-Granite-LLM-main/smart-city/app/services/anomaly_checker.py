def detect_anomaly(df):
    anomalies = []

    for column in df.columns[1:]:
        values = df[column]
        mean = values.mean()
        std = values.std()

        for idx, value in enumerate(values):
            if abs(value - mean) > 2 * std:
                anomalies.append(f"Anomaly in {column} at {df.iloc[idx, 0]} (value: {value})")

    return anomalies if anomalies else "No anomalies detected."
