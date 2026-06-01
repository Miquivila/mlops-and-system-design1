DATASETS_FOLDER = "session_4/datasets"
MODELS_FOLDER = "session_4/models"
MODEL_NAME = "class_model"

COLUMNS_TO_DROP = ["RowNumber", "CustomerId", "Surname"]
BINARY_FEATURES = []
ONE_HOT_ENCODE_COLUMNS = ["Geography", "Gender"]

MODEL_PARAMS = {
    "max_depth": 5,
    "random_state": 42
}

