# %%

import pandas as pd


def read():
    return pd.read_csv("towns.csv", index_col=0).assign(
        state=lambda df: df.loc[:, "state"].str.removesuffix("[edit]"),
        town=lambda df: df.loc[:, "town"].str.extract(r"(.+) \(.*"),
    )


towns = read()
