from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_predict():
    response = client.post("/predict", json={"CreditScore": 600, "Age": 40, "Balance": 50000})
    assert response.status_code == 200
    assert "prediction" in response.json()
