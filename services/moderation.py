import os, httpx
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("PERSPECTIVE_API_KEY")

async def check_toxicity(text: str) -> float:
    if not API_KEY:
        return 0.0

    url = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze"
    payload = {
        "comment": {"text": text},
        "languages": ["en"],
        "requestedAttributes": {"TOXICITY": {}}
    }

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.post(url, params={"key": API_KEY}, json=payload)
        data = response.json()
        return data["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
