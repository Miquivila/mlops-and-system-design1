import pandas as pd
from metadata import COLUMNS_TO_DROP, ONE_HOT_ENCODE_COLUMNS


def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(columns=COLUMNS_TO_DROP)
    df = _one_hot_encoding(df)
    return df


def _one_hot_encoding(df: pd.DataFrame) -> pd.DataFrame:
    df = pd.get_dummies(df, columns=ONE_HOT_ENCODE_COLUMNS)
    return df
