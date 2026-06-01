from src.source import load_data
from src.transform import transform
from src.train import train_model
from src.store import store_model


def main():
    df = load_data("Churn_Modelling_train_test.csv")
    df = transform(df)
    model = train_model(df, target_column="Exited")
    store_model(model)


if __name__ == "__main__":
    main()