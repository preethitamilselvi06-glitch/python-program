import pandas as pd
import matplotlib.pyplot as plt 
df = pd.read_csv("data/data_dictionary.csv")
print(df.head())
x = df.iloc[:10, 0]
y=range(len(x))
plt.figure(figsize=(10, 5))
plt.bar(y, [1] * len(y))
plt.xticks(y, x, rotation=90)
plt.title("Data Dictionary Entries")
plt.xlabel("column names")
plt.ylabel("count")
plt.tight_layout()
plt.show()
