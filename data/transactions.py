import pandas as pd 
transactions =pd.read_csv(r"C:\Users\acer\Desktop\project\data\transactions.csv")
print(transactions)
print(transactions.info())
print(transactions.shape)
print(transactions.describe)
print(transactions.head(20))
print(transactions.isnull().sum())
print(transactions.duplicated().sum())