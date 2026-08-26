import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
# -----------------------------------------------------
# 1. LOAD THE DATA
# -----------------------------------------------------
df = pd.read_csv(r"C:\Users\USER\OneDrive\Desktop\Netflix project\netflix_titles.csv")
 
print("Shape of dataset:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
 
print("\nColumn info:")
print(df.info())
 
# -----------------------------------------------------
# 2. CLEAN THE DATA
# -----------------------------------------------------
 
# Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())
 
# Common cleaning steps for this dataset:
# - 'director', 'cast', 'country' often have missing values -> fill with "Unknown"
# - 'date_added', 'rating', 'duration' have a few missing -> drop those rows
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df = df.dropna(subset=['date_added', 'rating', 'duration'])
 
# Remove exact duplicate rows, if any
df = df.drop_duplicates()
 
# Convert date_added to a proper datetime type
df['date_added'] = pd.to_datetime(df['date_added'].str.strip())
 
# Extract year and month added — useful for time-based analysis
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month
 
print("\nShape after cleaning:", df.shape)
 
# -----------------------------------------------------
# 3. ASK QUESTIONS OF THE DATA
# -----------------------------------------------------
 
# Q1: How many Movies vs TV Shows are there?
print("\nMovies vs TV Shows:")
print(df['type'].value_counts())
 
# Q2: Which countries produce the most content?
print("\nTop 10 countries by content count:")
print(df['country'].value_counts().head(10))
 
# Q3: What are the most common genres (listed_in)?
# Note: listed_in has multiple genres per row separated by commas
genres = df['listed_in'].str.split(', ').explode()
print("\nTop 10 genres:")
print(genres.value_counts().head(10))
 
# Q4: How has content added to Netflix changed over the years?
print("\nContent added per year:")
print(df['year_added'].value_counts().sort_index())
 
# Q5: What's the most common content rating (TV-MA, PG-13, etc.)?
print("\nContent rating distribution:")
print(df['rating'].value_counts())
 
 
# -----------------------------------------------------
# 4. VISUALIZE FINDINGS
# -----------------------------------------------------
sns.set_style("whitegrid")
 
# Chart 1: Movies vs TV Shows
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='type', palette='Set2')
plt.title('Movies vs TV Shows on Netflix')
plt.xlabel('')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('chart1_movies_vs_tv.png')
plt.show()
 
# Chart 2: Content added per year
plt.figure(figsize=(10, 5))
df['year_added'].value_counts().sort_index().plot(kind='bar', color='crimson')
plt.title('Netflix Content Added Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles Added')
plt.tight_layout()
plt.savefig('chart2_content_by_year.png')
plt.show()
 
# Chart 3: Top 10 genres
plt.figure(figsize=(10, 6))
genres.value_counts().head(10).plot(kind='barh', color='teal')
plt.title('Top 10 Genres on Netflix')
plt.xlabel('Count')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('chart3_top_genres.png')
plt.show()
 
# Chart 4: Top 10 countries
plt.figure(figsize=(10, 6))
df['country'].value_counts().head(10).plot(kind='barh', color='darkorange')
plt.title('Top 10 Countries by Content Count')
plt.xlabel('Count')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('chart4_top_countries.png')
plt.show()