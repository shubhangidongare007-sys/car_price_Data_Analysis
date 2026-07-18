import pandas as pd

df = pd.read_csv("car_price_dataset.csv")

encoded_df = pd.get_dummies(df, columns=["Brand","Fuel_Type","Transmission","Owner"])

print(encoded_df.head())