import pandas as pd
import html
import re

# --- Step 1: Load Anime.csv ---
anime_df = pd.read_csv('Anime.csv')

# --- Step 2: Clean Anime Names ---
def clean_name(name):
    name = html.unescape(str(name))
    name = re.sub(r'[°\x00-\x1F\x7F]', "'", name)
    name = re.sub(r'[;\x00-\x1F\x7F]', ":", name)
    return name.strip()

anime_df['name'] = anime_df['name'].apply(clean_name)
print("✅ Anime names cleaned.")

# --- Step 3: Extract and Normalize Genres ---
# Drop missing genres
anime_genres = anime_df[['anime_id', 'genre']].dropna().copy()

# Split and explode
anime_genres['genre'] = anime_genres['genre'].str.split(',')
anime_genres = anime_genres.explode('genre')
anime_genres['genre'] = anime_genres['genre'].str.strip()

# Save exploded genres
anime_genres.to_csv('anime_genres.csv', index=False)
print("✅ Exploded anime genres saved to anime_genres.csv.")

# --- Step 4: Create Genre Lookup Table ---
# Create a DataFrame with unique genres and IDs
genre_lookup = pd.DataFrame({'genre': sorted(anime_genres['genre'].unique())})
genre_lookup['genre_id'] = range(1, len(genre_lookup) + 1)

# Save genre lookup table
genre_lookup.to_csv('genre_lookup.csv', index=False)
print("✅ Genre lookup table saved to genre_lookup.csv.")

# --- Step 5: Add Clean Genre String to Anime Dataset ---

# Load the dataset
df = pd.read_csv("Anime_final_cleaned.csv")

# Keep only anime name and genre
df_genre_only = df[['name', 'genre_cleaned']].dropna().copy()

# Split genres into lists
df_genre_only['genre_cleaned'] = df_genre_only['genre_cleaned'].apply(
    lambda x: [g.strip() for g in x.split(",")]
)

# Explode into multiple rows (one anime per genre)
df_genre_only = df_genre_only.explode('genre_cleaned').reset_index(drop=True)

# Rename the column for clarity
df_genre_only = df_genre_only.rename(columns={'genre_cleaned': 'genre_single'})

# Save the result to a new CSV
df_genre_only.to_csv("Anime_genre_split.csv", index=False)

print("✅ New dataset saved as Anime_genre_split.csv")
