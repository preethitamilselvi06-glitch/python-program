import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv("data/merchants.csv")
merchant_counts = df['merchant_name'].value_counts().head(10)
plt.figure(figsize=(10, 6))
merchant_counts.plot(kind='bar')
plt.title("top 10 merchants by transaction count", fontsize=16)
plt.xlabel("merchant name", fontsize=12)
plt.ylabel("transaction count", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()