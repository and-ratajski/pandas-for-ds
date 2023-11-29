import pandas as pd

# Set up the dataset
orchard = [
    {"name": "apple", "image": "🍏"},
    {"name": "pear", "image": "🍐"},
    {"name": "tomato", "image": "🍅"},
    {"name": "lemon", "image": "🍋"},
]

garden = [
    {"name": "tomato", "color": "red", "image": "🍅"},
    {"name": "potato", "color": "brown", "image": "🥔"},
    {"name": "carrot", "color": "orange", "image": "🥕"},
]

fruits = pd.DataFrame(orchard)
veggies = pd.DataFrame(garden)

print(fruits)
print(veggies)

# -------------------------------------------------
# ------------------- pd.concat -------------------
# -------------------------------------------------

# help(pd.concat)

pd.concat([fruits, veggies])
pd.concat([veggies, fruits])
pd.concat([fruits, veggies], axis="columns")
pd.concat([fruits, veggies], axis="columns", keys=["fruits", "veggies"])
pd.concat([fruits, veggies], axis="rows", keys=["fruits", "veggies"])

single = pd.concat([fruits, veggies])
print(single)

# single.loc[1:2, :]  # KeyError

multivitamin = pd.concat([fruits, veggies], keys=["fruits", "veggies"])
print(multivitamin)

multivitamin.loc[("fruits", 1):("fruits", 2), :]
multivitamin.loc[("veggies", 1):("veggies", 2), :]

pd.concat([fruits, veggies], ignore_index=True)
pd.concat([fruits, veggies], axis="columns", ignore_index=True)
pd.concat([fruits, veggies], axis="rows", join="outer")
pd.concat([fruits, veggies], axis="rows", join="inner")
pd.concat([fruits, veggies], axis="columns", join="inner")

# -------------------------------------------------
# ------------------- pd.merge --------------------
# -------------------------------------------------

# help(pd.merge)

pd.merge(fruits, veggies)
pd.merge(fruits, veggies, how="inner")
pd.merge(fruits, veggies, how="outer")
pd.merge(fruits, veggies, how="left")
pd.merge(fruits, veggies, how="right")

fruits["taste"] = ["sweet", "sweet", "sour", "sour"]
print(fruits)

pd.merge(fruits, veggies, how="right")
fruits = fruits.drop("taste", axis="columns")
print(fruits)

pd.merge(fruits, veggies, on=["name", "image"])
pd.merge(fruits, veggies, on="name")
pd.merge(fruits, veggies, on="image")
# pd.merge(fruits, veggies, on="color")  # KeyError
pd.merge(fruits, veggies, left_index=True, right_index=True)

# Add an additional column
orchard = [
    {"name": "apple", "image": "🍏", "amount": 1},
    {"name": "pear", "image": "🍐", "amount": 3},
    {"name": "tomato", "image": "🍅", "amount": 0},
    {"name": "lemon", "image": "🍋", "amount": 1},
]

garden = [
    {"name": "tomato", "color": "red", "image": "🍅"},
    {"name": "potato", "color": "brown", "image": "🥔"},
    {"name": "carrot", "color": "orange", "image": "🥕"},
]

fruits = pd.DataFrame(orchard)
veggies = pd.DataFrame(garden)

print(fruits)
print(veggies)

pd.merge(fruits, veggies, left_on="amount", right_index=True)
pd.merge(fruits, veggies, left_on="amount", right_index=True, suffixes=["_f", "_v"])

pd.merge(fruits, veggies, how="cross", suffixes=["_fruits", "_veggies"])
pd.merge(fruits, veggies)

print(fruits)
fruits = pd.concat(
    [fruits, pd.DataFrame([{"name": "orange", "image": "🍊", "amount": 10}])],
    ignore_index=True,
)
print(fruits)

pd.merge(fruits, veggies, left_on="name", right_on="color")
pd.merge(fruits, veggies, left_on="image", right_on="name")

merged = pd.merge(fruits, veggies, how="outer")
merged.dtypes
fruits.dtypes
print(merged)

pd.merge(fruits, veggies).dtypes
