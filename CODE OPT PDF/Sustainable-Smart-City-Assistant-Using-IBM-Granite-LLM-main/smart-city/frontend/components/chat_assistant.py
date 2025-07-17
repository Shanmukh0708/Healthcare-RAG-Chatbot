import streamlit as st
from utils.request_handler import query_granite
from frontend.readonly import read_only_config as cfg

def render():
    st.header(cfg.CHAT_TITLE)
    prompt = st.text_input("Ask a question:")
    if st.button("Send"):
        if prompt:
            response = query_granite(prompt)
            st.success(response)
        else:
            st.warning("Please enter a prompt.")
