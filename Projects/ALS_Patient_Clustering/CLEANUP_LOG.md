# ALS Patient Clustering - Portfolio Cleanup Log

## Project organization

The ALS clustering analysis was reorganized for publication as a standalone data science portfolio project, using project-specific naming rather than course submission naming.

## Naming and documentation

- Standardized project folder: `ALS_Patient_Clustering/`.
- Standardized notebook: `notebooks/ALS_Patient_Clustering.ipynb`.
- Removed the redundant standalone script `scripts/ALS_Patient_Clustering.py` to keep the notebook as the single executable analysis.
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


## Google Colab compatibility update

- Updated `notebooks/ALS_Patient_Clustering.ipynb` to load `data/raw/als_data.csv` from the local project when available, or automatically retrieve it from the public GitHub repository when running in Google Colab.
- Standardized the notebook's internal Colab filename metadata to `ALS_Patient_Clustering.ipynb`.
- Updated `README.md` with the direct Google Colab launch link and automatic dataset-loading instructions.
- These changes remove the need to upload the CSV manually in a fresh Colab session when internet access is available.
- Full end-to-end execution in a fresh Colab session remains to be verified.

## Validation and remaining checks

- Notebook code cells previously passed Python syntax parsing.
- Full execution of the notebook has **not** been verified in a clean environment.
- Review dataset publication permissions and confirm no sensitive information is included before publishing.

## Publishing location

Place this project at `Projects/ALS_Patient_Clustering/` in the portfolio repository. This file is a **project-specific cleanup record**; it does not replace the repository-level `PORTFOLIO_CLEANUP.md`.
