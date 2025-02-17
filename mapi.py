from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load the ML model and scalers
with open("random_forest_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("scaler_x.pkl", "rb") as x_scaler_file:
    x_scaler = pickle.load(x_scaler_file)

with open("scaler_y.pkl", "rb") as y_scaler_file:
    y_scaler = pickle.load(y_scaler_file)

class PredictionInput(BaseModel):
    Power_Consumption_kW: float
    Machines: int
    Num_Employees: int
    Timestamp: float
    Mill_Size_Medium: bool
    Mill_Size_Small: bool
    Mill_Size_Large: Optional[bool] = False  # Kept here but not used in ML input
    Location_Ankleshwar: bool
    Location_Silvassa: bool
    Location_Surat: bool
    Location_Vapi: bool

@app.post("/predict")
async def predict(input_data: PredictionInput):
    try:
        input_array = np.array([
            input_data.Power_Consumption_kW,
            input_data.Machines,
            input_data.Num_Employees,
            input_data.Timestamp,
            int(input_data.Mill_Size_Medium),
            int(input_data.Mill_Size_Small),
            # Removed Mill_Size_Large (it was already one-hot encoded)
            int(input_data.Location_Ankleshwar),
            int(input_data.Location_Silvassa),
            int(input_data.Location_Surat),
            int(input_data.Location_Vapi)
        ]).reshape(1, -1)

        # Apply the scalers
        scaled_input = x_scaler.transform(input_array)
        scaled_prediction = model.predict(scaled_input)
        prediction = y_scaler.inverse_transform(scaled_prediction.reshape(-1, 1))[0][0]

        return {"prediction": float(round(prediction, 2))}
    
    except Exception as e:
        return {"error": str(e)}