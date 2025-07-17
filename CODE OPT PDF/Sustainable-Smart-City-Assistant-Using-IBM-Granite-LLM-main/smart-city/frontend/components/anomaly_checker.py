import streamlit as st
import requests
from frontend.readonly import read_only_config as cfg

def render():
    st.header(cfg.ANOMALY_DETECT_TITLE)
    uploaded_file = st.file_uploader("Upload KPI CSV file for anomaly check")
    if uploaded_file:
        if st.button("Check Anomalies"):
            try:
                files = {"file": uploaded_file.getvalue()}
                res = requests.post("http://127.0.0.1:8000/anomaly/detect", files=files)
                st.success(res.json()["result"])
            except:
                st.error("Anomaly check failed.")
