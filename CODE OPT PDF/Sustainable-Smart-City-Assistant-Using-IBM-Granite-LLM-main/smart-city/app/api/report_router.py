from fastapi import APIRouter, Query
from app.services.granite_llm import query_granite

router = APIRouter()

@router.post("/generate")
def generate_report(kpi_data: str = Query(...)):
    prompt = (
        f"As a Smart City AI, analyze the following KPI data and provide a concise summary:\n\n"
        f"{kpi_data}"
    )
    summary = query_granite(prompt)
    return {"summary": summary}
