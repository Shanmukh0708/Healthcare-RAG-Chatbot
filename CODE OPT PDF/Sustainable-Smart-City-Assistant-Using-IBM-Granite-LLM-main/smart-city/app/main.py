from fastapi import FastAPI
from app.api import chat_router, eco_tips_router, report_router, policy_router, feedback_router, kpi_upload_router, anomaly_router

app = FastAPI(title="Smart City API")

app.include_router(chat_router.router, prefix="/chat")
app.include_router(eco_tips_router.router, prefix="/eco")
app.include_router(report_router.router, prefix="/report")
app.include_router(policy_router.router, prefix="/policy")
app.include_router(feedback_router.router, prefix="/feedback")
app.include_router(kpi_upload_router.router, prefix="/kpi")
app.include_router(anomaly_router.router, prefix="/anomaly")

@app.get("/")
def home():
    return {"message": "Smart City API is running"}
