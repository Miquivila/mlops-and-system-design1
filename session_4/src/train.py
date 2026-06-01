from sklearn.tree import DecisionTreeClassifier
from metadata import MODEL_PARAMS
import pandas as pd


def train_model(df: pd.DataFrame, target_column: str) -> DecisionTreeClassifier:
    X = df.drop(columns=[target_column])
    y = df[target_column]
    model = DecisionTreeClassifier(**MODEL_PARAMS)
    model.fit(X, y)
    return model
