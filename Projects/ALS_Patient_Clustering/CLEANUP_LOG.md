# ALS Patient Clustering — Portfolio Cleanup Log

## Project organization

The ALS clustering analysis was reorganized for publication as a standalone data science portfolio project, using project-specific naming rather than course submission naming.

## Naming and documentation

- Standardized project folder: `ALS_Patient_Clustering/`.
- Standardized notebook: `notebooks/ALS_Patient_Clustering.ipynb`.
- Created corresponding script: `scripts/ALS_Patient_Clustering.py`.
- Replaced academic assignment framing in the notebook introduction with a project overview.
- Added `README.md` describing the research question, dataset, approach, results, limitations, and execution instructions.
- Added `requirements.txt` for Python dependencies.

## File cleanup

- Retained the source dataset as `data/raw/als_data.csv`.
- Created `data/processed/` and `outputs/` for future generated artifacts.
- Excluded coursework submission PDFs, redundant deliverables, and checkpoint files from the GitHub-ready package.
- Adjusted dataset-loading paths for the reorganized project layout.

## Analysis retained

- Feature preparation and scaling.
- K-means clustering and silhouette-score comparison.
- PCA-based cluster visualization.
- Original interpretation of weak cluster separation.

## Validation and remaining checks

- Notebook code cells and standalone Python script passed Python syntax parsing.
- Full execution of the notebook and script has **not** been verified in a clean environment.
- Review dataset publication permissions and confirm no sensitive information is included before publishing.

## Publishing location

Place this project at `Projects/ALS_Patient_Clustering/` in the portfolio repository. This file is a **project-specific cleanup record**; it does not replace the repository-level `PORTFOLIO_CLEANUP.md`.
