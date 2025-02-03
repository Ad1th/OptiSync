from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class TextData(BaseModel):
    text: str

# Global variable to store the received text
Message = ""

# File path where the message will be saved
MESSAGE_FILE = "message.json"

@app.post("/submit")
async def submit_text(data: TextData):
    global Message
    Message = data.text  # Update the global variable
    
    # Save the message to a file
    with open(MESSAGE_FILE, "w") as file:
        json.dump({"message": Message}, file)
    
    print(f"Received text: {Message}")
    return {"message": "Text received"}
