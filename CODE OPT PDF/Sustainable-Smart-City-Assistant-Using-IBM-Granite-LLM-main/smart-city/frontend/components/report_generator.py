import streamlit as st
import requests

def render():
    st.subheader("📊 KPI Report Generator")

    kpi_data = st.text_area("Enter KPI data (comma-separated):")
    
    if st.button("Generate Report") and kpi_data:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/report/generate",
                params={"kpi_data": kpi_data}
            )
            response.raise_for_status()
            summary = response.json().get("summary", "")
            st.success(summary)
        except requests.exceptions.RequestException as e:
            st.error("Failed to generate report.")
            st.caption(str(e))
