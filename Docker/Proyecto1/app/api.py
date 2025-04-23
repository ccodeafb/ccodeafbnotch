# api.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("app/model.joblib")

class Features(BaseModel):
    data: list  # lista de listas (múltiples muestras)

@app.post("/predict")
def predict(features: Features):
    X = np.array(features.data)
    predictions = model.predict(X)
    return {"predictions": predictions.tolist()}
