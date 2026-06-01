import joblib
from datetime import datetime
from metadata import MODELS_FOLDER, MODEL_NAME


def store_model(model) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    model_path = f"{MODELS_FOLDER}/{MODEL_NAME}-miqi-{timestamp}.joblib"
    joblib.dump(model, model_path)
    print(f"Model stored as: {model_path}")