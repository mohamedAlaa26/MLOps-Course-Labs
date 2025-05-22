from fastapi import FastAPI
from model.predict import predict_churn
from api.schema import InputData
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()


Instrumentator().instrument(app).expose(app)

@app.get("/")
def home():
    return {"message": "Welcome to the Churn Prediction API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: InputData):  
    return predict_churn(data.dict())
