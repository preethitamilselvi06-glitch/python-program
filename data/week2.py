import pandas as pd
import numpy as np

df = pd.read_csv("transactions.csv")
users = pd.read_csv("users.csv")

df["date"] = pd.to_datetime(df["date"])

snapshot_date = df["date"].max() + pd.Timedelta(days=1)

cap = df["amount"].quantile(0.99)
df["amount_capped"] = df["amount"].clip(upper=cap)

rfm = df.groupby("user_id").agg(
    Recency=("date", lambda x: (snapshot_date - x.max()).days),
    Frequency=("transaction_id", "count"),
    Monetary=("amount_capped", "sum")
).reset_index()

print(rfm.shape)
print(rfm.head())
rfm["Avg_Txn_Value"] = rfm["Monetary"] / rfm["Frequency"]

fav_type = df.groupby("user_id")["transaction_type"].agg(
    lambda x: x.mode()[0]
).rename("Fav_Txn_Type")

rfm = rfm.merge(fav_type, on="user_id")

weekend_ratio = df.groupby("user_id")["is_weekend"].mean().rename("Weekend_Ratio")
night_ratio = df.groupby("user_id")["is_night_transaction"].mean().rename("Night_Ratio")

rfm = rfm.merge(weekend_ratio, on="user_id")
rfm = rfm.merge(night_ratio, on="user_id")

rfm = rfm.merge(
    users[["user_id","age_group","city_tier","kyc_status","user_loyalty_score"]],
    on="user_id",
    how="left"
)

print(rfm.shape)
print(rfm.head())
import numpy as np

rfm["Monetary_log"] = np.log1p(rfm["Monetary"])

print(rfm[["Monetary", "Monetary_log"]].head())
print(rfm["Monetary_log"].skew())
from sklearn.preprocessing import StandardScaler

cluster_features = [
    "Recency",
    "Frequency",
    "Monetary_log",
    "Avg_Txn_Value",
    "Weekend_Ratio",
    "Night_Ratio"
]

scaler = StandardScaler()

rfm_scaled = scaler.fit_transform(rfm[cluster_features])

print(rfm_scaled.shape)
print(rfm_scaled.mean(axis=0))
print(rfm_scaled.std(axis=0))

import seaborn as sns
import matplotlib.pyplot as plt

numeric_cols = [
    "Recency",
    "Frequency",
    "Monetary_log",
    "Avg_Txn_Value",
    "Weekend_Ratio",
    "Night_Ratio",
    "user_loyalty_score"
]

corr = rfm[numeric_cols].corr()

plt.figure(figsize=(9, 7))
sns.heatmap(corr, annot=True, 
fmt=".2f", cmap='coolwarm', center=0)
plt.title("Feature Correlation Matrix")
plt.tight_layout()
plt.savefig('heatmap.png')
plt.show()
plt.close()
rfm.to_csv("rfm_features.csv", index=False)

print("Saved rfm_features.csv")
print(rfm.shape)