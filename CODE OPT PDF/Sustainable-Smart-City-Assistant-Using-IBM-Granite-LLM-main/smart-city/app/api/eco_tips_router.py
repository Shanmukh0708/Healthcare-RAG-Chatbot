from fastapi import APIRouter
from utils.request_handler import query_granite

router = APIRouter()

@router.get("/tip")
def get_eco_tip(topic: str):
    prompt = (
        f"You are an eco-assistant. Suggest one practical and topic-specific sustainability tip about '{topic}'."
    )
    tip = query_granite(prompt)
    return {"tip": tip}
