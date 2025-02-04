from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load ML model and scalers
model = joblib.load("random_forest_model.pkl")
scaler_x = joblib.load("scaler_x.pkl")
scaler_y = joblib.load("scaler_y.pkl")

# Updated Input Schema
class InputData(BaseModel):
    Power_Consumption_kW: float
    Machines: float
    Num_Employees: float
    Timestamp: float
    Mill_Size_Medium: bool
    Mill_Size_Small: bool
    Mill_Size_Large: bool        # Added this line
    Location_Ankleshwar: bool
    Location_Silvassa: bool
    Location_Surat: bool 
    Location_Vapi: bool 

@app.post("/predict")
def predict(data: InputData):
    # Convert input to numpy array
    features = np.array([[data.Power_Consumption_kW, data.Machines, data.Num_Employees,
                          data.Timestamp, data.Mill_Size_Medium, data.Mill_Size_Small,
                          data.Mill_Size_Large,                        # Added this line
                          data.Location_Ankleshwar, data.Location_Silvassa,
                          data.Location_Surat, data.Location_Vapi]])

    # Scale input features
    scaled_features = scaler_x.transform(features)

    # Make prediction (scaled output)
    scaled_prediction = model.predict(scaled_features)

    # Convert back to real bill amount
    final_prediction = scaler_y.inverse_transform(scaled_prediction.reshape(-1, 1))

    return {"prediction": round(final_prediction[0][0], 2)}
