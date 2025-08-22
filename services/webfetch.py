import requests
from fastapi import HTTPException

def fetch_main_text(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        if not response.text or len(response.text.strip()) == 0:
            raise HTTPException(status_code=500, detail="Fetched website has no readable content.")

        return response.text

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Could not fetch the website: {e}")
        raise HTTPException(status_code=500, detail=f"Could not fetch the website: {str(e)}")
