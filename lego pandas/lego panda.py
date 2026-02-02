import pandas as df
import matplotlib.pyplot as plt
import numpy as np

data = df.read_csv("lego_sets.csv")

rows = data.shape[0]
columns = data.shape[1]

print("Rows:", rows)
print("Columns:", columns)

datatypes = data.info()

print(f"Datatypes: {datatypes}")

cols_with_missing = data.columns[data.isna().any()]
print(cols_with_missing)

average = data["list_price"].mean()
print(f"Average : {average}")

max = data["list_price"].max()
print(f"Maximum : {max}")

plt.hist(data["list_price"])
plt.title("Prices")
plt.ylabel("number of sets")
plt.xlabel("price")
plt.show()

x = data["list_price"]
y = data["piece_count"]
 
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
 
plt.scatter(x, y)
plt.xlabel("Price")
plt.ylabel("Piece Count")
plt.title("Piece count vs Price")
 
plt.plot(x, p(x), "red")
 
plt.show()

