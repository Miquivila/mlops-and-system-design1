import pandas as pd
from src.transform import transform, _one_hot_encoding


def test_drop_columns():
    df = pd.DataFrame({
        "RowNumber": [1, 2],
        "CustomerId": [123, 456],
        "Surname": ["Smith", "Jones"],
        "Geography": ["France", "Spain"],
        "Gender": ["Male", "Female"],
        "Age": [30, 40],
        "Exited": [0, 1]
    })
    result = transform(df)
    assert "RowNumber" not in result.columns
    assert "CustomerId" not in result.columns
    assert "Surname" not in result.columns


def test_one_hot_encoding():
    df = pd.DataFrame({
        "Geography": ["France", "Spain"],
        "Gender": ["Male", "Female"],
        "Age": [30, 40]
    })
    result = _one_hot_encoding(df)
    assert "Geography" not in result.columns
    assert "Gender" not in result.columns
    assert "Geography_France" in result.columns or "Geography_Spain" in result.columns