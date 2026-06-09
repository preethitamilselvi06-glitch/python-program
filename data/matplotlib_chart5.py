import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv("data/users.csv")
user_counts=df['user_id'].value_counts().head(10)
plt.figure(figsize=(10, 6))
user_counts.plot(kind='bar')
plt.title("top 10 users by transaction count", fontsize=16)
plt.xlabel("user id", fontsize=12)
plt.ylabel("transaction count", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()