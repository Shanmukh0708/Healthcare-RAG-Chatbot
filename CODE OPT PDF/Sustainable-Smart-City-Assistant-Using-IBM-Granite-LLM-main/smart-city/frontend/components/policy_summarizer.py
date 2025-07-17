# frontend/components/policy_summarizer.py

import streamlit as st
import requests

def render():
    st.subheader("📄 Policy Summarizer")
    text = st.text_area("Paste policy or regulation text here:")

    if st.button("Summarize") and text:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/policy/summarize",
                params={"text": text}
            )
            response.raise_for_status()
            st.success(response.json()["summary"])
        except requests.exceptions.RequestException as e:
            st.error("Summarization failed.")
            st.caption(str(e))
