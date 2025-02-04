from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class TextData(BaseModel):
    powerConsumption: str
    millSize: str
    numberOfMachines: str
    numberOfEmployees: str
    location: str
    machineDescription: str

# File path where the message will be saved
MESSAGE_FILE = "message.json"

@app.post("/api")
async def submit_text(data: TextData):
    print(f"Received Data: {data.dict()}")  # Debugging
    logging.info(f"Received Data: {data.dict()}")  

    with open(MESSAGE_FILE, "w") as file:
        json.dump(data.dict(), file)
    
    print(f"Data written to {MESSAGE_FILE}")  # Debugging
    return {"message": "Data received successfully."}


