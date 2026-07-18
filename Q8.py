import pandas as pd

df = pd.read_csv("car_price_dataset.csv")

X = df.drop("Price", axis=1)
y = df["Price"]

print("Independent Variables:")
print(X.head())

print("\nDependent Variable:")
print(y.head())