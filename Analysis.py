import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("sales_data.csv")

# Show first 5 rows
print(df.head())

# Show basic info
print(df.info())
import pandas as pd

df = pd.read_csv("sales_data.csv")

# Cleaning
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df["Date"] = pd.to_datetime(df["Date"])

# Create Revenue
df["Revenue"] = df["Quantity"] * df["Price"]

# Standardize text
df["Product"] = df["Product"].str.strip().str.title()
df["Region"] = df["Region"].str.strip().str.title()

print(df.head())
print("Total Revenue:", df["Revenue"].sum())
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print(top_products)
region_sales = df.groupby("Region")["Revenue"].sum()
print(region_sales)
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Revenue"].sum()
print(monthly_sales)



# Top products
top_products.plot(kind='bar', title="Top Products by Revenue")
plt.show()

# Region sales
region_sales.plot(kind='bar', title="Sales by Region")
plt.show()

# Monthly trend
monthly_sales.plot(kind='line', title="Monthly Sales Trend")
plt.show()