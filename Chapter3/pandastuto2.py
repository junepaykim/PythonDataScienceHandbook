"""2022.10.16 study"""
import numpy as np
import pandas as pd


def main():
    """main function for pandas"""
    index = pd.MultiIndex.from_product(
        [[2013, 2014], [1, 2]], names=["year", "visit"]
    )
    columns = pd.MultiIndex.from_product(
        [["Bob", "Guido", "Sue"], ["HR", "Temp"]], names=["subject", "type"]
    )

    data = np.round(np.random.randn(4, 6), 1)
    data[:, ::2] *= 10
    data += 37

    health_data = pd.DataFrame(data, index=index, columns=columns)

    # data_mean = health_data.groupby(level='year').median()
    # data_mean = health_data.mean(axis=1, level='subject')
    data_mean = health_data.groupby(axis=1, level="subject").median()
    print(data_mean)


if __name__ == "__main__":
    main()
