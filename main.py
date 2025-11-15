from fastapi import FastAPI
from pydantic import BaseModel
import os
from pymongo import MongoClient

# Replace with your MongoDB connection string
DATABASE_NAME = "volunteer-hub"
MONGODB_URL = os.environ.get("MONGO_URI")
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
