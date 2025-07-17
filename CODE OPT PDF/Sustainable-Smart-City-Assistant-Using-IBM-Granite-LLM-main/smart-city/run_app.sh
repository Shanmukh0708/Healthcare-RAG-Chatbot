#!/bin/bash

echo "🔄 Starting FastAPI backend..."
uvicorn app.main:app --reload &

sleep 2

echo "🚀 Launching Streamlit frontend..."
streamlit run frontend/smart_dashboard.py
