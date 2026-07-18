import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================
# Q2 - Load Dataset
# ==========================

df = pd.read_csv("car_price_dataset.csv")

print("========== Q2 ==========")
print("\nFirst 10 Rows")
print(df.head(10))

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nDataset Information")
print(df.info())