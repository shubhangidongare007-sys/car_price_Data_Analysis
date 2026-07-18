import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("car_price_dataset.csv")

numeric_columns = ["Year", "Kilometers_Driven", "Engine_CC", "Mileage", "Price"]

df[numeric_columns].hist(figsize=(10,8))

plt.suptitle("Histogram of Numerical Columns")
plt.show()