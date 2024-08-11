# Importing libraries
import pandas as pd

# Load data
df = pd.read_csv("Basket.csv", header=None, names=range(20))

# Loop to convert all values to string and discard NaN values
items = []
for i in range(len(df)):
    items.append([str(df.values[i, j]) for j in range(20) if str(df.values[i, j]) != "nan"])
