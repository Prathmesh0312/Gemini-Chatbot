from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from db.session import Base, engine, SessionLocal
from db.models import RunLog
from services.webfetch import fetch_main_text
from services.llm import generate_response  # updated import
from services.moderation import check_toxicity
import os

if os.getenv("RENDER") is None:
    from dotenv import load_dotenv
    load_dotenv()

# Create the DB table if it doesn't exist
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI()

# request schema
class RequestIn(BaseModel):
    url: HttpUrl
    instruction: str

# Define response schema
class ResponseOut(BaseModel):
    output: str
    toxicity: float
    flagged: bool
    run_id: int

@app.post("/generate", response_model=ResponseOut)
async def generate(request: RequestIn):
    try:
        # Fetch webpage text
        source = fetch_main_text(request.url)

        #Generate response using Gemini
        result = generate_response(source, request.instruction)

        #Check toxicity usingAPI
        toxicity = await check_toxicity(result)
        flagged = toxicity >= 0.5

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Log to DB
    with SessionLocal() as session:
        log = RunLog(
            url=str(request.url),
            task_type=request.instruction,  
            model="gemini-2.5-flash",
            output_text=result,
            toxicity=toxicity,
            flagged=flagged
        )
        session.add(log)
        session.commit()
        session.refresh(log)

    # Return result
    return ResponseOut(
        output=result,
        toxicity=round(toxicity, 3),
        flagged=flagged,
        run_id=log.id
    )
