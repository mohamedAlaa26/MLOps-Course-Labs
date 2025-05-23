import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from src.preprocessing import preprocess
from src.train_model import train
from src.visualize import log_confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
def run_experiment(model_type):
    with mlflow.start_run():
        df = pd.read_csv("dataset/Churn_Modelling.csv")
        col_transf, X_train, X_test, y_train, y_test = preprocess(df)

        mlflow.set_tag("model_type", model_type)

        mlflow.log_param("model", model_type)
        model = train(X_train, y_train, model_type)

        y_pred = model.predict(X_test)

        mlflow.log_metric("accuracy", accuracy_score(y_test, y_pred))
        mlflow.log_metric("precision", precision_score(y_test, y_pred))
        mlflow.log_metric("recall", recall_score(y_test, y_pred))
        mlflow.log_metric("f1_score", f1_score(y_test, y_pred))

        conf_mat = log_confusion_matrix(y_test, y_pred, model)
        disp = ConfusionMatrixDisplay(confusion_matrix=conf_mat, display_labels=model.classes_)
        disp.plot()

        filename = f"{model_type}_confusion_matrix.png"
        plt.savefig(filename)  
        plt.close()  

        mlflow.log_artifact(filename) 
        


def main():
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment("churn_prediction_experement")

    for model in ["logistic", "random_forest"]:
        run_experiment(model)

if __name__ == "__main__":
    main()

