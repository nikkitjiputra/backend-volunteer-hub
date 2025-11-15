from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Opportunity(BaseModel):
    title: str
    organization: str
    description: str
    email: str
    dateOfEvent: str
    timeOfEvent: str
    format: str
    address: str
    registrationLink: str
    keywords: str

@app.post("/submit")
def submit_opportunity(data: Opportunity):
    print("Received:", data.model_dump())
    return {"status": "ok"}
