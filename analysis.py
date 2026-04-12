import pandas as pd
import matplotlib.pyplot as plt

# ======================
# 1. Load Dataset
# ======================
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

# ======================
# 2. Data Cleaning
# ======================
df.drop(columns=['director'], inplace=True) # Removed 'director' column as it was containing many null values

df['country'] = df['country'].fillna("Unknown")   # Filled null values with 'Unknown'
df['cast'] = df['cast'].fillna("Not Available")   # Filled null values with 'Not Available'
df['date_added'] = df['date_added'].ffill()    # Data was filled with previous entry's date
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])    # Filled wih mode of 'rating' column values
df.dropna(inplace=True) # Droped rest of columns with null entries

print(df.isna().sum())

# ======================
# 3. Data Analysis
# ======================

# Movies vs TV Shows
print("Type count:\n", df['type'].value_counts())

# Ratings
print("Ratings Count:\n", df['rating'].value_counts())

# Top Countries
print("Top Countries:\n", df['country'].value_counts().head(10))

# Release Year Trend
print("Release Year Trend:\n", df['release_year'].value_counts().sort_index())

# Most Popular Genres
print("Most Popular Genres:\n", df['listed_in'].value_counts().head(10))

# ======================
# 4. Visualization
# ======================

df['type'].value_counts().plot(kind='bar')
plt.title("Movies vs TV Shows")
plt.show()