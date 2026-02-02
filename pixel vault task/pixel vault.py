import pandas as pd
import matplotlib.pyplot as mpl

csv = pd.read_csv("pixelvault game sales.csv")
print(f"First 5 rows: \n {csv.head}")
print(f"Last 5 rows: \n {csv.tail}")
print(f"Number of columns: \n {len(csv.columns)}")
print(f"Number of rows: \n {len(csv)}")

names = []
for col in csv.columns:
    names.append(col)

print(f" Column names : \n {names}")

print(f"Data types in the columns:\n")
print(f"{csv.info()}")

print(f" Missing values within the csv: \n {csv.isnull()}")

print(f" dupe'd values within the csv: \n {csv.duplicated()}")
