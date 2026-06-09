import pandas as pd 
fraud_labels = pd.read_csv(r"C:\Users\acer\Desktop\project\data\fraud_labels.csv")
print(fraud_labels)
print(fraud_labels.info())
print(fraud_labels.shape)
print(fraud_labels.describe)
print(fraud_labels.head(20))
print(fraud_labels.isnull().sum())
print(fraud_labels.duplicated().sum())
