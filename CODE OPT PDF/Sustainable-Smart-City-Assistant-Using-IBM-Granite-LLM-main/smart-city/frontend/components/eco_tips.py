import streamlit as st
import requests

def render():
    st.subheader("🌿 Eco Tips")
    topic = st.text_input("Enter a sustainability topic (e.g., energy, water, plastic):")

    if st.button("Get Tip") and topic:
        try:
            response = requests.get(
                "http://127.0.0.1:8000/eco/tip",
                params={"topic": topic}
            )
            response.raise_for_status()

            # Handle plain text or JSON response
            try:
                data = response.json()
                if isinstance(data, dict) and "tip" in data:
                    st.success(data["tip"])
                else:
                    st.success(data if isinstance(data, str) else str(data))
            except ValueError:
                st.success(response.text)

        except requests.exceptions.RequestException as e:
            st.error("Failed to fetch eco tip.")
            st.caption(str(e))
