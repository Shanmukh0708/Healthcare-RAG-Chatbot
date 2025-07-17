import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")
MODEL_ID = os.getenv("MODEL_ID")
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def query_granite(prompt: str, max_tokens=100):
    system_prompt = (
        "You are an AI Smart City Assistant. Your job is to provide helpful, clear, and accurate information "
        "about energy-saving, eco-tips, city reports, policies, KPIs, and citizen help. "
        "Always answer as a Smart City guide.\n\n"
        f"User: {prompt}\nAI:"
    )

    payload = {
        "inputs": system_prompt,
        "parameters": {
            "temperature": 0.3,          # Lower = faster and more accurate
            "max_new_tokens": max_tokens,
            "do_sample": False           # Disable sampling for speed
        }
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        result = response.json()

        if isinstance(result, list) and 'generated_text' in result[0]:
            generated = result[0]['generated_text']
            return generated.replace(system_prompt, "").strip()
        return "No generated_text found in response."
    except requests.exceptions.RequestException as e:
        return f"Request error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

