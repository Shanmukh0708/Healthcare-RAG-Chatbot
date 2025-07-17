from fastapi import APIRouter, UploadFile, File
import pandas as pd
from io import StringIO
from app.services.anomaly_checker import detect_anomaly

router = APIRouter()

@router.post("/detect")
async def detect(file: UploadFile = File(...)):
    content = await file.read()
    df = pd.read_csv(StringIO(content.decode()))
    
    result = detect_anomaly(df)
    return {"result": result}
