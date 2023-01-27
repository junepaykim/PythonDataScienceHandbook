import numpy as np
import pandas as pd


def main():
    train = pd.read_csv("./train.csv")
    test = pd.read_csv("./test.csv")

    train_x = train.drop(["Survived"], axis=1)
    train_y = train["Survived"]
    test_x = test.copy()


if __name__ == "__main__":
    main()
