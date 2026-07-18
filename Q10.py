import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("car_price_dataset.csv")

numeric_cols = ["Year","Kilometers_Driven","Engine_CC","Mileage"]

scaler = StandardScaler()

df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

print(df.head())