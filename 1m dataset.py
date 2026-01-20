import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales_data.csv")

print(df.head())
print(df.info())

df["total_sale"] = df["quantity"] * df["price"]

total_revenue = df["total_sale"].sum()
print("\nTotal Revenue for the Shop:", total_revenue)
revenue_per_product = df.groupby("product")["total_sale"].sum()
print("\nTotal Revenue per product:", revenue_per_product)
revenue_per_category = df.groupby("category")["total_sale"].sum()
print("\nTotal Revenue per category:", revenue_per_category)
top_3_products = revenue_per_product.sort_values(ascending=False).head(3)
print("\nTop 3 products:", top_3_products)

plt.figure(figsize=(10, 6))
revenue_per_product.plot(kind="bar", color="skyblue")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

daily_revenue = df.groupby("date")["total_sale"].sum()

plt.figure(figsize=(10, 6))
plt.plot(daily_revenue.index, daily_revenue.values, marker="o")
plt.title("Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Total Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()
