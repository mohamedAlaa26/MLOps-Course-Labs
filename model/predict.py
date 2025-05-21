
import joblib
import numpy as np
import os
from fastapi import FastAPI


model_path = os.path.join(os.path.dirname(__file__), "..", "model.pkl")
model_path = os.path.abspath(model_path)

model = joblib.load(model_path)

def predict_churn(data: dict):

    try:
        print("Input received:", data)
        features = np.array([list(data.values())]).reshape(1, -1)
        print("Prepared features:", features)
        prediction = model.predict(features)[0]
        return {"prediction": int(prediction)}
    except Exception as e:
        print("Prediction error:", e)
        return {"error": str(e)}
