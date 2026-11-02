"""Netflix catalog exploratory analysis."""
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, HTML

# 1.Load dataset
display(HTML("<h4 style='font-weight:bold;'> 1.Load Netflix titles dataset</h4>"))
from pathlib import Path

def find_dataset():
    candidates = [Path("data/raw/netflix_titles.csv"), Path("../data/raw/netflix_titles.csv"), Path(__file__).resolve().parents[1] / "data/raw/netflix_titles.csv"] if "__file__" in globals() else [Path("data/raw/netflix_titles.csv"), Path("../data/raw/netflix_titles.csv")]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("Run from the project root or notebooks directory, with data/raw/netflix_titles.csv present")

df = pd.read_csv(find_dataset())
# Data summary
display(HTML("<br><h5 style='font-weight:bold;'>Top 5 rows of Data </h5>"))
display(df.head())
display(HTML("<h5 style='font-weight:bold;'>Dataset Info</h5>"))
df.info()
display(HTML("<h5 style='font-weight:bold;'>Missing Values</h5>"))
print(df.isnull().sum())

# 2.Preprocess Genre Data for Analysis
# Split multiple genres per title into separate columns
display(HTML("<br><h4 style='font-weight:bold;'> 2.Data pre-processing</h4>"))
genre_counts = df['listed_in'].str.split(', ', expand=True).stack().value_counts()
print("Data preprocessing completed")

#3. Visualizations
display(HTML("<br><h3 style='font-weight:bold;'> 3.Visualizations</h3>"))
# Visualization 1-  BAR GRAPH showing top Genres
display(HTML("<h4 style='font-weight:bold;'> Visualization 1 - Most Common Genres Bar graph</h4>"))
# Bar charts are ideal for categorical data to show frequency counts. It allows to quickly identify the most common genres
plt.figure(figsize=(12,6))
genre_counts.head(15).plot(kind='bar', color='skyblue')
plt.title("Top 15 Most Common Genres on Netflix") # Bar chart showing top 15 genres
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45) # Rotate labels for readability
plt.tight_layout()
plt.show()
display(HTML(
    """
    <h5>Analysis:</h5>
    <ul>
        <li>The most frequent genres include International Movies, Dramas, and Comedies.</li>
        <li>There is a clear dominance of international and drama-focused genres, indicating Netflix’s strong emphasis on globally diverse content.</li>
        <li>Niche categories such as Classic Movies and Cult Movies appear far less frequently.</li>
    </ul>
    """
))

# Visualization 2 -  Box Plot showing Genre Count per Title
display(HTML("<br><h4 style='font-weight:bold;'>Visualization 2 -  Box Plot showing Genre Count per Title</h4>"))
# A box plot summarizes distribution, median, quartiles, and outliers
df['genre_count'] = df['listed_in'].fillna('').apply(lambda value: len([part for part in value.split(', ') if part])) # Create a new column with the count of genres per title
plt.figure(figsize=(6,6))
plt.boxplot(df['genre_count'], patch_artist=True, boxprops=dict(facecolor='lightgreen'))
plt.title("Boxplot of Number of Genres per Title")
plt.ylabel("Genre Count")
plt.show()
display(HTML(
    """
    <h5>Analysis:</h5>
    <ul>
        <li>Most titles have between one and three listed categories.</li>
        <li>Genre-count distribution is shown in the box plot.</li>
        <li>The majority of titles have fewer genres.Netflix categorizes most content into a small number of genres, keeping classifications simple for users.</li>
    </ul>
    """
))

# Visualization 3 - Rating Distribution Bar Chart
display(HTML("<br><h4 style='font-weight:bold;'>Visualization 3 - Rating Distribution Bar Chart</h4>"))
plt.figure(figsize=(10,5))
df['rating'].value_counts().plot(kind='bar', color='orange')
plt.title("Overall Distribution of Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
display(HTML(
    """
    <h5>Analysis:</h5>
    <ul>
        <li>TV-MA (Mature Audience) is the most common rating, followed by TV-14.</li>
        <li>Ratings such as PG, R, PG-13, G appear much less frequently. TV-specific ratings dominate the dataset.</li>
        <li>Netflix’s library leans heavily toward mature audiences, particularly in TV content.Indicates Netflix’s focus on producing teen and adult-oriented streaming content.</li>
    </ul>
    """
))

# Visualization 4 - Bivariate Bar Chart showing Rating by type (Movie Vs.TV Show)
display(HTML("<br><h4 style='font-weight:bold;'>Visualization 4 - Bivariate Bar Chart showing Rating by type (Movie Vs.TV Show)</h4>"))
rating_by_type = df.groupby(['type', 'rating']).size().unstack(fill_value=0)
plt.figure(figsize=(12,6))
rating_by_type.T.plot(kind='bar', figsize=(12,6))
plt.title("Rating Distribution for Movies vs TV Shows")
plt.xlabel("Rating Category")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
display(HTML(
    """
    <h5>Analysis:</h5>
    <ul>
        <li>Movies show greater diversity in ratings (PG, PG-13, R, etc.).</li>
        <li>TV Shows overwhelmingly fall into TV-MA and TV-14 categories. TV-Y and TV-G content is minimal compared to mature categories.</li>
        <li>TV Shows on Netflix focus heavily on mature audiences, while Movies cater to a wider range of rating categories.</li>
    </ul>
    """
))

# Additional Visualization - Heatmap of Ratings by Type
display(HTML("<br><h4 style='font-weight:bold;'>Additional Visualization - Heatmap of Ratings by Type </h4>"))
plt.figure(figsize=(10,6))
sns.heatmap(rating_by_type, annot=True, fmt='d', cmap='Blues')
plt.title("Heatmap of Ratings by Type")
plt.xlabel("Rating category")
plt.ylabel("Content type")
plt.show()
display(HTML(
    """
    <h5>Analysis:</h5>
    <ul>
        <li>Higher counts are visible in the TV-MA category for both movies and TV shows.</li>
        <li>Children’s and general-audience rating categories have lower counts than the leading mature-audience categories.</li>
        <li>The heatmap visually confirms Netflix's content rating imbalance, showing a strong emphasis on mature-rated programming. TV shows skew much more sharply toward adult audiences than movies.</li>
    </ul>
    """
))