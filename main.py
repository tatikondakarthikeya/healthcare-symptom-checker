
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import traceback

app = FastAPI()

class SymptomRequest(BaseModel):
    symptoms: str

class CheckerResponse(BaseModel):
    probable_conditions: list
    next_steps: list
    disclaimer: str

# Dummy inference logic, to be replaced by LLM integration (Hugging Face)
def analyze_symptoms_llm(symptoms: str):
    # For now, hardcoded outputs; replace with actual inference
    return {
        "probable_conditions": ["Migraine", "Tension Headache"],
        "next_steps": ["Stay hydrated", "Rest in a quiet room"],
        "disclaimer": "Educational purposes only. Not a medical diagnosis. Consult a doctor for professional advice."
    }

@app.post("/check-symptoms", response_model=CheckerResponse)
async def check_symptoms(req: SymptomRequest):
    try:
        result = analyze_symptoms_llm(req.symptoms)
        return CheckerResponse(**result)
    except Exception as e:
        # Robust error handling
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Internal Server Error: "+str(e))

# Health check endpoint
@app.get("/ping")
def ping():
    return {"status": "API running"}
