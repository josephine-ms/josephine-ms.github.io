"""MovieLens item-based collaborative filtering recommender."""
from pathlib import Path
from difflib import get_close_matches
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

ROOT = Path(__file__).resolve().parents[1] if "__file__" in globals() else Path.cwd()
DATA = ROOT / "data" / "raw"
if not DATA.exists():
    DATA = ROOT.parent / "data" / "raw"
movies = pd.read_csv(DATA / "movies.csv")
ratings = pd.read_csv(DATA / "ratings.csv")
movie_stats = ratings.groupby("movieId").agg(avg_rating=("rating", "mean"), rating_count=("rating", "count")).reset_index()
movie_details = movies.merge(movie_stats, on="movieId", how="left")
movie_details[["avg_rating", "rating_count"]] = movie_details[["avg_rating", "rating_count"]].fillna(0)

# Sparse movie-by-user matrix avoids creating a large all-pairs similarity matrix.
movie_ids = pd.Index(movies["movieId"])
user_ids = pd.Index(sorted(ratings["userId"].unique()))
rows = movie_ids.get_indexer(ratings["movieId"])
cols = user_ids.get_indexer(ratings["userId"])
valid = (rows >= 0) & (cols >= 0)
movie_user = csr_matrix((ratings.loc[valid, "rating"].to_numpy(), (rows[valid], cols[valid])), shape=(len(movie_ids), len(user_ids)))


def find_best_match(query, titles):
    """Return a title from a case-insensitive substring or fuzzy match."""
    query = query.strip().lower()
    if not query:
        return None
    titles = list(titles)
    substring = [title for title in titles if query in title.lower()]
    if substring:
        return substring[0]
    lowered = {title.lower(): title for title in titles}
    matches = get_close_matches(query, list(lowered), n=1, cutoff=0.4)
    return lowered[matches[0]] if matches else None


def recommend_movies(movie_title, n=10):
    """Return top N movies ranked by cosine similarity, excluding the input movie."""
    matching = movies.index[movies["title"] == movie_title]
    if len(matching) == 0:
        raise ValueError("Movie not found in dataset")
    idx = int(matching[0])
    scores = cosine_similarity(movie_user[idx], movie_user).ravel()
    scores[idx] = -1
    candidates = movie_details.copy()
    candidates["similarity"] = scores
    candidates = candidates[candidates["similarity"] > 0]
    return candidates.sort_values(["similarity", "rating_count"], ascending=[False, False]).head(n)[["title", "similarity", "avg_rating", "rating_count", "genres"]]


def recommend_from_query(query, n=10):
    matched = find_best_match(query, movies["title"])
    if matched is None:
        raise ValueError("No matching movie title found")
    return matched, recommend_movies(matched, n=n)


if __name__ == "__main__":
    selected, results = recommend_from_query("Toy Story", 10)
    print(f"Recommendations for: {selected}")
    print(results.to_string(index=False))
