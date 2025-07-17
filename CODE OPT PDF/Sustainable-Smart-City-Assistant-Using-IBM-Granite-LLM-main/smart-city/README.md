# Sustainable Smart City Assistant 🏙️

A Streamlit-based AI-powered assistant that uses IBM Granite LLM from Hugging Face for:
- 💬 Chat Assistant
- 🌱 Eco Tips Generator
- 📄 Policy Summarization
- 📊 KPI Forecasting
- ⚠️ Anomaly Detection
- 📃 Sustainability Report Generation
##🔧 How to Run: Sustainable Smart City Assistant Using IBM Granite LLM

This guide explains how to set up and run the Smart City Assistant application on your local system. The project is divided into two parts:

Backend: FastAPI application

Frontend: Streamlit app for user interaction

✅ Prerequisites

Python 3.10 or higher

Hugging Face account with API key

## 🧪 How to Run

```bash
pip install -r requirements.txt
streamlit run frontend/smart_dashboard.py
🔐 Environment Setup

Create a .env file in the root directory with the following content:

HUGGINGFACE_API_KEY=your_huggingface_token
MODEL_ID=ibm-granite/granite-3.3-2b-instruct

Replace your_huggingface_token with your actual Hugging Face token.

🚀 Running the Project

✅ Step 1: Start Backend (FastAPI)

Command : uvicorn app.main:app --reload

Runs at: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

Ensure the backend is running without errors before proceeding.

✅ Step 2: Start Frontend (Streamlit)

Command : streamlit run frontend/smart_dashboard.py

Runs at: http://localhost:8501

🧪 Functional Modules

💬 Chat Assistant: Ask questions and get smart city solutions.

🌿 Eco Tips: Get sustainability tips based on topic.

📢 Citizen Feedback: Submit and acknowledge issues.

📊 KPI Report Generator: Paste CSV data to summarize performance.

📈 KPI Forecast: Upload .csv file and forecast next usage.

🚨 Anomaly Detection: Upload .csv to detect outlier values.

📄 Policy Summarizer: Paste policy text to get a summary.

🛠️ Common Issues

404 Errors: Make sure backend is running before frontend.

Model Errors: Ensure .env has correct model ID and valid Hugging Face API key.

CORS Issues: Handled by FastAPI and Streamlit; no extra setup needed locally.

✅ You’re Ready!

Your Smart City Assistant app should now be up and running locally. Interact with the dashboard and explore all features.

