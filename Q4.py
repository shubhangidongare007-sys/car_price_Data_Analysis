import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv("car_price_dataset.csv")

# ==========================
# Q4 - Statistical Summary
# ==========================

print("========== Q4 ==========")

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Target Variable = Price
print("\nMinimum Price:", df["Price"].min())
print("Maximum Price:", df["Price"].max())
print("Mean Price:", df["Price"].mean())
print("Median Price:", df["Price"].median())

print("\nObservations:")
print("1. Price is the target variable.")
print("2. Mean price shows the average car price.")
print("3. Minimum and maximum prices show the price range.")
print("4. Median price represents the middle value of the dataset.")