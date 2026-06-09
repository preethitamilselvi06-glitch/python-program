import pandas as pd 
data_dictionary = pd.read_csv(r"C:\Users\acer\Desktop\project\data\data_dictionary.csv")
print(data_dictionary)
print(data_dictionary.info())
print(data_dictionary.shape)
print(data_dictionary.describe)
print(data_dictionary.head(20))
print(data_dictionary.isnull().sum())
print(data_dictionary.duplicated().sum())
