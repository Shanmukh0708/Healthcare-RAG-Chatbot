from utils.request_handler import query_granite

def ask(prompt: str):
    return query_granite(prompt)

def generate_summary(text: str):
    prompt = f"Summarize the following policy:\n\n{text}"
    return query_granite(prompt)

def generate_eco_tip(topic: str):
    prompt = f"Give me 3 actionable eco-friendly tips about {topic}."
    return query_granite(prompt)

def generate_city_report(kpi_data: str):
    prompt = f"Based on this data, write a sustainability report:\n\n{kpi_data}"
    return query_granite(prompt, max_tokens=400)
