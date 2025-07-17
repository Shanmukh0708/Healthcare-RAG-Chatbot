# app/api/policy_router.py

from fastapi import APIRouter, Query
from app.services.granite_llm import query_granite

router = APIRouter()

@router.post("/summarize")
def summarize_policy(text: str = Query(...)):
    prompt = f"Summarize the following city policy in 1-2 sentences:\n\n{text}"
    summary = query_granite(prompt)
    return {"summary": summary}
