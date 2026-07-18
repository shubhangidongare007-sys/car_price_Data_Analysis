import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("car_price_dataset.csv")

numeric_df = df.select_dtypes(include=["number"])

plt.figure(figsize=(8,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()