# MovieLens Recommendation System

## Overview
An item-based collaborative filtering system that recommends movies with similar user-rating patterns. It supports partial and fuzzy movie-title matching and returns ten recommended titles with similarity scores and rating statistics.

## Research question
Can patterns in historical movie ratings help identify movies similar to a title selected by a user?

## Data
Uses the MovieLens `ml-latest-small` dataset from GroupLens: `movies.csv`, `ratings.csv`, `tags.csv`, and `links.csv`. The recommendation model uses **movies** and **ratings**; tags and links are retained as optional source metadata. The original dataset `README.txt` is preserved in `data/raw/` for attribution and license terms.

## Method
1. Load movie metadata and user ratings.
2. Compute movie-level rating averages and counts.
3. Construct a sparse movie-by-user rating matrix.
4. Find the closest title using partial and fuzzy matching.
5. Compute cosine similarity on demand for the selected movie.
6. Rank by similarity and return the ten nearest movies.

## Interpretation
Recommendations are based on similarities between observed rating vectors, not movie plots or genres. The original notebook described Pearson correlation in its narrative, but the implementation uses **cosine similarity**. The portfolio version aligns the documentation with the implemented method. The implementation does not establish held-out recommendation accuracy.

## Repository contents
- `notebooks/MovieLens_Recommendation_System.ipynb`: reproducible notebook with a noninteractive example
- `scripts/MovieLens_Recommendation_System.py`: standalone runnable version
- `data/raw/`: original MovieLens data and licensing notes
- `data/processed/`: reserved for generated data
- `outputs/`: reserved for exported results
- `PORTFOLIO_CLEANUP.md`: project-specific cleanup record

## Run
From the project folder:
```bash
python -m pip install -r requirements.txt
python scripts/MovieLens_Recommendation_System.py
```
The script prints ten recommendations for *Toy Story*. You can also run the notebook from the project root or `notebooks/` directory.

## Limitations and responsible use
Popularity bias, sparsity, cold-start limitations, and absence of offline validation mean this is a demonstration rather than a production-ready recommender. User identifiers are anonymized. MovieLens data are subject to the redistribution and noncommercial conditions in `data/raw/README.txt`; no endorsement by GroupLens or the University of Minnesota is implied.

## Dataset attribution
Harper, F. M., & Konstan, J. A. (2015). The MovieLens datasets: History and context. *ACM Transactions on Interactive Intelligent Systems, 5*(4). https://doi.org/10.1145/2827872
