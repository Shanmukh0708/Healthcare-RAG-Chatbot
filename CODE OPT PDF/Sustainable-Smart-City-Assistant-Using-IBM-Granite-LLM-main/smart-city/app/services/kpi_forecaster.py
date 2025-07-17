import pandas as pd
from sklearn.linear_model import LinearRegression

def forecast_kpi(csv_file):
    df = pd.read_csv(csv_file)
    if df.shape[1] < 2:
        return "CSV must have at least 2 columns: [Year, Value]"

    X = df.iloc[:, 0].values.reshape(-1, 1)
    y = df.iloc[:, 1].values

    model = LinearRegression()
    model.fit(X, y)

    next_year = X[-1][0] + 1
    prediction = model.predict([[next_year]])

    return f"Forecast for {next_year}: {round(prediction[0], 2)}"
