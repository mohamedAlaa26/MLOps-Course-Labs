# Lab - Monitoring API

This project is a FastAPI-based machine learning API for predicting customer churn. The model is trained using historical customer data and deployed with an interactive Swagger UI for testing and development. It includes **Docker support**, **MLflow for model tracking**, and **monitoring with Prometheus and Grafana**.

---

## 🚀 Features

- ✅ FastAPI backend with automatic OpenAPI docs
- ✅ MLflow model integration for churn prediction
- ✅ Health check and root endpoint
- ✅ Prometheus metrics endpoint (`/metrics`)
- ✅ Grafana dashboard integration for API monitoring
- ✅ Dockerized using `docker-compose` for easy deployment
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
   git clone https://github.com/mohamedAlaa26/MLOps-Course-Labs.git
   cd MLOps-Course-Labs/monitoring_lab
