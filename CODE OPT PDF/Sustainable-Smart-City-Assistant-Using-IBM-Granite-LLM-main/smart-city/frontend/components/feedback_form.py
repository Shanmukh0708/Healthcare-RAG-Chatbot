import streamlit as st
import requests

def render():
    st.subheader("📝 Citizen Feedback")

    name = st.text_input("Your Name")
    category = st.selectbox("Feedback Category", ["Infrastructure", "Transport", "Pollution", "Energy", "Other"])
    message = st.text_area("Your Feedback")

    if st.button("Submit Feedback"):
        if not (name and message):
            st.warning("Please fill in all required fields.")
            return

        try:
            response = requests.post(
                "http://127.0.0.1:8000/feedback/submit",
                params={"name": name, "category": category, "message": message}
            )
            response.raise_for_status()
            result = response.json()
            st.success("Response from Smart City system:")
            st.info(result.get("response", "Thank you for your feedback!"))
        except requests.exceptions.RequestException as e:
            st.error("Failed to submit feedback.")
            st.caption(str(e))
