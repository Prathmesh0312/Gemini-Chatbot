from google import genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
print(" ENV Test:", os.getenv("GEMINI_API_KEY"))
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print(" GEMINI_API_KEY not found. Check your .env file.")
    exit()

# Print to confirm
print(" API key loaded")

try:
    # Initialize Gemini client
    client = genai.Client(api_key=api_key)

    # Generate a fun fact
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Write a one-sentence fun fact about coffee."
    )

    print(" Gemini response:")
    print(response.text)

except Exception as e:
    print(" Error during API call:", e)
