import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from components import (
    chat_assistant,
    eco_tips,
    feedback_form,
    report_generator,
    policy_summarizer,
    kpi_forecast,
    anomaly_checker
)

st.set_page_config(page_title="Smart City Assistant", layout="wide")

# Define modules
modules = {
    "💬 Chat Assistant": chat_assistant.render,
    "🌿 Eco Tips": eco_tips.render,
    "📢 Citizen Feedback": feedback_form.render,
    "📊 KPI Report Generator": report_generator.render,
    "📄 Policy Summarizer": policy_summarizer.render,
    "📈 KPI Forecast": kpi_forecast.render,
    "🚨 Anomaly Detection": anomaly_checker.render,
}

# Initialize state
if "selected_module" not in st.session_state:
    st.session_state.selected_module = list(modules.keys())[0]

# Layout: Vertical menu + content pane
menu_col, content_col = st.columns([1, 3])

with menu_col:
    st.markdown("## 📂 Modules")
    for name in modules.keys():
        if st.button(name, use_container_width=True):
            st.session_state.selected_module = name

with content_col:
    st.markdown(f"### {st.session_state.selected_module}")
    modules[st.session_state.selected_module]()
