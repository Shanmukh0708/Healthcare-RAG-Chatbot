import pandas as pd

def load_csv(file):
    try:
        return pd.read_csv(file)
    except Exception as e:
        return f"Error reading file: {e}"

def parse_text(file):
    try:
        return file.read().decode("utf-8")
    except Exception as e:
        return f"Error reading text file: {e}"
