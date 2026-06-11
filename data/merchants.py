import pandas as pd 
merchants = pd.read_csv(r"C:\Users\acer\Desktop\project\data\merchants.csv")
print(merchants)
print(merchants.info())
print(merchants.shape)
print(merchants.describe)
print(merchants.head(20))
print(merchants.isnull().sum())
print(merchants.duplicated().sum())