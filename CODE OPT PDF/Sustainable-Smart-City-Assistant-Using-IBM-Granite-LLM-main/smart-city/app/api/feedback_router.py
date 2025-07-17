from fastapi import APIRouter, Query
from utils.request_handler import query_granite

router = APIRouter()

@router.post("/submit")
def submit_feedback(
    name: str = Query(...),
    category: str = Query(...),
    message: str = Query(...)
):
    prompt = (
        f"As a Smart City system, you've received feedback from a citizen.\n\n"
        f"Name: {name}\nCategory: {category}\nMessage: {message}\n\n"
        f"Write a polite and short response acknowledging their feedback and thanking them."
    )
    ai_response = query_granite(prompt)
    return {"response": ai_response}
