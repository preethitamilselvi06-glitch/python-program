import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv("data/fraud_labels.csv")
print(df.head())
label_col = df.columns[-1]
counts = df[label_col].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(counts.index.astype(str),counts.values)
plt.title("fraud vs non-fraud transactions")
plt.xlabel("label")
plt.ylabel("count")
plt.show()
