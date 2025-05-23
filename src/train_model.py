from sklearn.linear_model import LogisticRegression
import mlflow.sklearn
from mlflow.models.signature import infer_signature

def train(X_train, y_train, model_type="logistic"):
    if model_type == "logistic":
        model = LogisticRegression(max_iter=1000)
    elif model_type == "random_forest":
        model = RandomForestClassifier(n_estimators=100, random_state=42)
    else:
        raise ValueError("Unsupported model type")

    model.fit(X_train, y_train)

    # Log model
    signature = infer_signature(X_train, model.predict(X_train))
    mlflow.sklearn.log_model(model, f"{model_type}_model", signature=signature)

    return model
