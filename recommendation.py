import pandas as pd

# ======================
# 1. Load Dataset
# ======================
df = pd.read_csv("netflix_titles.csv")
df = df[['title', 'listed_in', 'description']]
df.dropna(inplace=True)

# ======================
# 2. Data Processing
# ======================

# Combine Features
df['content'] = df['listed_in'] + " " + df['description']

# Convert Text to Numbers
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(stop_words='english')
matrix = cv.fit_transform(df['content'])

# Similarity Calculation
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(matrix)

print(similarity.shape)

# ======================
# 3. Build Recommendation Function
# ======================

# Create Index Mapping
df['title'] = df['title'].str.lower()
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

# Create Recommendation Function
def recommend(title):
    title = title.lower()

    if title not in indices:
        return "Movie not found"
    
    idx = indices[title]

    # Get similarity scores
    sim_scores = list(enumerate(similarity[idx]))

    # Sort based on similarity
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top 5 (excluding itself)
    sim_scores = sim_scores[1:6]

    # Get movie indices
    movie_indices = [i[0] for i in sim_scores]

    recommendations = df['title'].iloc[movie_indices]

    print("Reccomendations using CountVectorizer:")

    return recommendations

print(recommend("Narcos"))
print(recommend("Extraction"))
print(recommend("The Witcher"))
print(recommend("unknown movie"))

# Convert Text to Numbers using TF-IDf
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(df['content'])

# Similarity Calculation
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(matrix)

print(similarity.shape)

# Recommendation System using TF-IDF
def recommend(title):
    title = title.lower()

    if title not in indices:
        return "Movie not found"
    
    idx = indices[title]

    # Get similarity scores
    sim_scores = list(enumerate(similarity[idx]))

    # Sort based on similarity
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top 5 (excluding itself)
    sim_scores = sim_scores[1:6]

    # Get movie indices
    movie_indices = [i[0] for i in sim_scores]

    recommendations = df['title'].iloc[movie_indices]

    print("Recommendatins using TF-IDF:")

    return recommendations

print(recommend("Narcos"))
print(recommend("Extraction"))
print(recommend("The Witcher"))
print(recommend("unknown movie"))