import pandas as pd 
fraud_labels = pd.read_csv(r"C:\Users\acer\Desktop\project\data\fraud_labels.csv")
print(fraud_labels)
print(fraud_labels.info())
print(fraud_labels.shape)