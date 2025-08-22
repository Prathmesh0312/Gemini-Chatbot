import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_NAME = "gemini-2.5-flash"

def generate_response(content: str, instruction: str) -> str:
    full_prompt = f"Instruction: {instruction}\n\nWebsite Content:\n{content[:6000]}"

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=full_prompt
    )

    return response.text if hasattr(response, "text") else str(response)
