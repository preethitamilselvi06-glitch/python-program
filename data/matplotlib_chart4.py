import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv("data/transactions.csv")
transaction_count = df['transaction_type'].value_counts()
plt.figure(figsize=(8, 6))
transaction_count.plot(kind='bar')
plt.title("transaction type distribution", fontsize=16)
plt.xlabel("transaction type", fontsize=12)
plt.ylabel("count", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()