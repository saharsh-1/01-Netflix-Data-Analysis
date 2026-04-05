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

df.drop(columns=['director'], inplace=True) # Removed 'director' column as it was containing many null values
df['country'] = df['country'].fillna("Unknown", inplace=True)   # Filled null values with 'Unknown'
df['cast'] = df['cast'].fillna("Not Available", inplace=True)   # Filled null values with 'Not Available'
df['date_added'] = df['date_added'].fillna(method='ffill', inplace=True)    # Data was filled with previous entry's date
df['rating'] = df['rating'].fillna(df['rating'].mode()[0], inplace=True)    # Filled wih mode of 'rating' column values
df.dropna(inplace=True) # Droped rest of columns with null entries

print(df.isna().sum())