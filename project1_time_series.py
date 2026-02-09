import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

# 1. Line chart - Sales over time
sales_over_time = df.groupby("date")["sales"].sum()
sales_over_time.plot(title="Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("charts/sales_over_time.png")
plt.close()

# 2. Bar chart - Sales by category
category_sales = df.groupby("category")["sales"].sum()
category_sales.plot(kind="bar", title="Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("charts/category_sales.png")
plt.close()

# 3. Pie chart - Category share
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Share by Category")
plt.ylabel("")
plt.tight_layout()
plt.savefig("charts/category_share.png")
plt.close()

print("Project 1 charts created successfully!")
