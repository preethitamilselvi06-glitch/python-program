import pandas as pd 
users = pd.read_csv(r"C:\Users\acer\Desktop\project\data\users.csv")
print(users)
print(users.info())
print(users.shape)
print(users.describe())
print(users.isnull().sum())
print(users.duplicated().sum())
print(users)

