import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("car_price_dataset.csv")

plt.figure(figsize=(6,4))
sns.countplot(x="Fuel_Type", data=df)
plt.title("Fuel Type Count")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x="Transmission", data=df)
plt.title("Transmission Count")
plt.show()

plt.figure(figsize=(8,4))
sns.countplot(x="Brand", data=df)
plt.xticks(rotation=45)
plt.title("Brand Count")
plt.show()