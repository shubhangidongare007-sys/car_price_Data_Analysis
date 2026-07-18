import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv("car_price_dataset.csv")

# ==========================
# Q3 - Data Cleaning
# ==========================

print("\n========== Q3 ==========")

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Missing Value Percentage
print("\nMissing Value Percentage:")
print((df.isnull().sum() / len(df)) * 100)

# Remove Duplicate Records
print("\nDuplicate Records:", df.duplicated().sum())
df = df.drop_duplicates()

print("\nShape After Removing Duplicates:")
print(df.shape)