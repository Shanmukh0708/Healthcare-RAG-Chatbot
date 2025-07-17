from fastapi import APIRouter, Body
from app.services.granite_llm import query_granite

router = APIRouter()

@router.post("/ask")
def ask_chat(prompt: str = Body(..., embed=True)):
    response = query_granite(prompt)
    return {"response": response}