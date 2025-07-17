# frontend/components/kpi_forecast.py

import streamlit as st
import requests

def render():
    st.subheader("📈 KPI Forecast")
    uploaded_file = st.file_uploader("Upload KPI CSV File", type="csv")

    if uploaded_file and st.button("Generate Forecast"):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/kpi/forecast",
                files={"file": uploaded_file.getvalue()}
            )
            response.raise_for_status()
            data = response.json()

            if "forecast" in data:
                st.success(data["forecast"])
            else:
                st.warning("No forecast generated.")
        except Exception as e:
            st.error(f"Request failed: {str(e)}")
