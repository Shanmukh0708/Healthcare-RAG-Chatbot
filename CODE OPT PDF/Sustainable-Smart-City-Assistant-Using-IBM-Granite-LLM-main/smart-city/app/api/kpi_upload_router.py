# app/api/kpi_upload_router.py

from fastapi import APIRouter, UploadFile, File
import pandas as pd
from io import StringIO
from app.services.granite_llm import query_granite

router = APIRouter()

@router.post("/forecast")
async def forecast_kpi(file: UploadFile = File(...)):
    try:
        # Read and decode CSV content
        contents = await file.read()
        decoded = contents.decode("utf-8")
        df = pd.read_csv(StringIO(decoded))

        # Create the prompt from last 5 rows
        prompt = (
            f"You are a smart city analytics assistant. Forecast next month's KPIs from this data:\n\n"
            f"{df.tail(5).to_string(index=False)}"
        )

        response = query_granite(prompt)
        return {"forecast": response}

    except Exception as e:
        return {"error": f"Failed to process file: {str(e)}"}
