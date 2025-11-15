from fastapi import FastAPI
from pydantic import BaseModel

from pymongo import MongoClient

# Replace with your MongoDB connection string
MONGODB_URL = "mongodb://localhost:27017" 
DATABASE_NAME = "volunteer-hub"

client = MongoClient(MONGODB_URL)
database = client[DATABASE_NAME]
collection = database["opportunities"]

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
    data_dict = data.model_dump()

    result = collection.insert_one(data_dict)
    print("Received:", data_dict)
    return {"status": "ok"}
