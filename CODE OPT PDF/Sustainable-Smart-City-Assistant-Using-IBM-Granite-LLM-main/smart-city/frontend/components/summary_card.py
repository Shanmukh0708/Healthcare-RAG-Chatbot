import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

def render_card(title, value, unit=""):
    st.markdown(f"""
    <div style="background-color:#f0f2f6;padding:15px;border-radius:15px;text-align:center;">
        <h3>{title}</h3>
        <h1 style="color:green;">{value} {unit}</h1>
    </div>
    """, unsafe_allow_html=True)