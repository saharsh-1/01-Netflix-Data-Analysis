import pandas as pd

df = pd.read_csv("netflix_titles.csv")

# print(df.head())
# print(df.shape)      # rows, columns
# print(df.columns)    # column names
# print(df.info())     # data types
# print(df.describe()) # statistics

print(df.head(10))
print(df.shape)
print(df.columns)
print(df.isna().sum())