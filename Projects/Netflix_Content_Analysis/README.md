# Netflix Content and Genre Analysis

## Project Overview
Exploratory data analysis of the Netflix titles catalog, focusing on content categories and audience ratings. **This dataset does not contain weekly Netflix Top 10 rankings or viewership metrics.**

## Research Questions
1. Which genres/categories are most common in the catalog?
2. How do content-rating distributions compare for movies and TV shows?

## Dataset
- Source: [Netflix Movies and TV Shows on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- File: `data/raw/netflix_titles.csv`
- Observations: **8,807**; fields: **12**
- Content fields include title, type, listed genres, rating, release year, country, and date added.

## Analysis
- Load and inspect the catalog and missing values.
- Split comma-separated `listed_in` categories to calculate category frequencies.
- Plot the top 15 categories.
- Summarize the number of categories per title using a box plot.
- Compare content ratings overall and by movie/TV-show type using bar charts and a heatmap.

## Key Observations
- Leading catalog categories include **International Movies, Dramas, Comedies**.
- The most frequent audience ratings include **TV-MA, TV-14**.
- These are catalog counts, **not viewing popularity or engagement**.

## Open the notebook in Google Colab
[**Open Netflix Content Analysis notebook in Colab**](https://colab.research.google.com/github/josephine-ms/josephine-ms.github.io/blob/main/Projects/Netflix_Content_Analysis/notebooks/Netflix_Content_Analysis.ipynb)

Select **Runtime → Run all**. The notebook retrieves `netflix_titles.csv` from the public GitHub repository if a local copy is unavailable (internet access required). Complete fresh-Colab execution has not yet been independently verified.

## Run locally
Install dependencies with `python -m pip install -r requirements.txt`, then open `notebooks/Netflix_Content_Analysis.ipynb` in Jupyter and run the cells.

## Project Structure
- `notebooks/` — annotated analysis notebook
- `data/raw/` — original dataset
- `data/processed/` — reserved for derived data
- `outputs/` — reserved for generated figures
- `CLEANUP_LOG.md` — project-specific cleanup record

## Limitations
The dataset is a historical snapshot of catalog titles, not current availability or user behavior. The `listed_in` field contains Netflix categories rather than a standardized genre taxonomy. Missing values and occasional inconsistent rating entries should be considered when interpreting distributions.
