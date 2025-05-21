
# Lab 2 - Churn Prediction API

This project is a FastAPI-based machine learning API for predicting customer churn. The model is trained using historical customer data and deployed with an interactive Swagger UI for testing and development. It includes Docker support for containerization and uses MLflow for model tracking.

---

## 🚀 Features

- ✅ FastAPI backend with automatic OpenAPI docs
- ✅ MLflow model integration for churn prediction
- ✅ Health check and root endpoint
- ✅ Dockerized for easy deployment
- ✅ Ready for use with Swagger UI or Postman

---

## 🧠 Model Info

- Model: Logistic Regression / XGBoost (customizable)
- Framework: Scikit-learn / MLflow
- Target: Binary classification – Will the customer churn?

---


## ⚙️ Installation

### Locally (with Python 3.10+)

1. Clone the repository:
   ```bash
   git clone https://github.com/mohamedAlaa26/lab2_api.git
   cd lab2_api
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```

### With Docker

```bash
docker build -t lab2_api .
docker run -d -p 8000:8000 lab2_api
```

---

## 🧪 API Endpoints

- `GET /` – Welcome message
- `GET /health` – Health check
- `POST /predict` – Submit customer data and get churn prediction

### Example `POST /predict` payload:
```json
{
  "gender": "Female",
  "senior_citizen": 0,
  "partner": "Yes",
  "dependents": "No",
  "tenure": 12,
  "phone_service": "Yes"
  ...
}
```

---

## 📊 MLflow Integration

Ensure your ML model is logged and served using MLflow. The app uses `mlflow.pyfunc.load_model` to load the model from a given directory or remote URI.

---

## 🐳 Docker Tips

To view logs:
```bash
docker logs <container_id>
```

To access Swagger UI:
- Open [http://localhost:8000/docs](http://localhost:8000/docs)

