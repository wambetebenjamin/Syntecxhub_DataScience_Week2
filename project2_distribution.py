import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales_data.csv")

# Histogram + KDE
sns.histplot(df['sales'], kde=True)
plt.title("Sales Distribution")
plt.savefig("charts/sales_distribution.png")
plt.close()

# Boxplot
sns.boxplot(x='category', y='sales', data=df)
plt.title("Sales by Category")
plt.savefig("charts/sales_boxplot.png")
plt.close()
