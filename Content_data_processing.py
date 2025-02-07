import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csr_matrix
from sqlalchemy import create_engine, inspect

# 1. Import the data needed in from SQL and vectorize it potentially using pd.DataFrame

## Create a database connection
engine = create_engine("sqlite:///instance/movies.db")

## Query the Content related subfields from SQL and then execute query
query = "SELECT id, certification, overview, genre, director, star1, star2, star3, star4 FROM movie"
df = pd.read_sql(query, con=engine, dtype={"certification": str})

## Convert to DataFrame
movies_df = pd.DataFrame(df, columns=["id", "certification", "overview", "genre", "director", "star1", "star2", "star3", "star4"])

#-------------------------
# Content Vectors
#------------------------
# Combine the features into a single text column
movies_df['combined_features'] = movies_df['genre'] + ' ' + movies_df['overview'] + ' ' + movies_df['director']

# Vectorize the combined features related to the content vectors
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies_df["combined_features"])

# Calculate the cosine similarity between movies
cosine_sim_content = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Create DataFrame for easier analysis
cosine_sim_content_df = pd.DataFrame(cosine_sim_content, index=movies_df['id'], columns=movies_df["id"])

# Similar movies
similar_movies = cosine_sim_content_df[7].sort_values(ascending=False)[1:]

print(similar_movies)