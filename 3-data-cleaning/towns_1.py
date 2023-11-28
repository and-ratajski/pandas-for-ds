# %%

import pandas as pd


def read():
    towns = []
    state = ""
    with open("data-sets/university_towns.txt") as file:
        for line in file:
            if "[edit]" in line:
                state = line.strip()
            else:
                towns.append([state, line])

    return pd.DataFrame(towns, columns=["state", "town"])


towns = read()
towns.to_csv("towns.csv")
