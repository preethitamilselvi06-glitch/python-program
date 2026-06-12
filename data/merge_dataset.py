import pandas as pd

transactions = pd.read_csv("transactions.csv")
users = pd.read_csv("users.csv")
merchants = pd.read_csv("merchants.csv")
fraud = pd.read_csv("fraud_labels.csv")


df = transactions.merge(
    users,
    on="user_id",
    how="left",
    suffixes=("", "_user")
)


df = df.merge(
    merchants,
    left_on="receiver_id",
    right_on="merchant_id",
    how="left",
    suffixes=("", "_merchant")

)
df = df.merge(
    fraud[["transaction_id", "is_fraud"]],
    on="transaction_id",
    how="left",
    suffixes=("", "_fraud")
)

print(df.shape)
print(df.head())

import matplotlib.pyplot as plt
import seaborn as sns

sns.countplot(x='is_fraud', data=df)
plt.title('Fraud vs Non-Fraud Transactions')
plt.xticks([0, 1], ['Not Fraud', 'Fraud'])
plt.show()

print(df['is_fraud'].value_counts(normalize=True) * 100)

plt.figure(figsize=(10,5))
sns.boxplot(x='is_fraud', y='amount', data=df)
plt.yscale('log')  
plt.title('Transaction Amount by Fraud Status')
plt.show()

df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
fraud_by_hour = df.groupby('hour')['is_fraud'].mean() * 100

plt.figure(figsize=(12,5))
fraud_by_hour.plot(kind='bar')
plt.title('Fraud Rate by Hour of Day')
plt.ylabel('Fraud %')
plt.show()

plt.figure(figsize=(10,8))
corr = df[['amount', 'hour', 'avg_daily_transactions', 'is_fraud']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Feature Correlation')
plt.show()

print(df['is_fraud'].value_counts(normalize=True) * 100)

df['hour'] = pd.to_datetime(df['timestamp']).dt.hour

fraud_by_hour = df.groupby('hour')['is_fraud'].mean() * 100


print(df.shape)
print(df.info())
print(df.isnull().sum())