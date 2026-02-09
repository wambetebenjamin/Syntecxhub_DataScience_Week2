import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales_data.csv")

# Encode category
df_encoded = pd.get_dummies(df, drop_first=True)

# Correlation matrix
corr = df_encoded.corr()

# Heatmap
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("charts/correlation_heatmap.png")
plt.close()

# Pairplot
sns.pairplot(df_encoded)
plt.savefig("charts/pairplot.png")
plt.close()
