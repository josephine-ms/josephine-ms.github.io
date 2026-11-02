# ALS Patient Clustering Analysis

## Overview
Explore whether anonymized ALS patient observations form distinct groups using unsupervised learning. This is an exploratory analysis, not a clinical diagnostic tool.

## Research Question
Can standardized ALS-related measurements be grouped into meaningful clusters, and how well-separated are those clusters?

## Dataset
The provided `data/raw/als_data.csv` contains anonymized ALS-related measurements. The analysis excludes the `SubjectID` identifier from model features.

## Methods
1. Inspect the source data and remove `SubjectID`.
2. Standardize numeric measurements using `StandardScaler`.
3. Compare K-means silhouette scores for 2–10 clusters.
4. Fit K-means with two clusters (`random_state=42`, `n_init=10`).
5. Apply two-component PCA and visualize the cluster assignments.

## Results and Interpretation
The original analysis reports its highest silhouette score near **0.078** for **two clusters**. This indicates weak cluster separation. The PCA scatterplot also shows overlap between groups. The result should be interpreted as exploratory rather than evidence of clinically meaningful ALS subtypes.

## Files
- `notebooks/ALS_Patient_Clustering.ipynb` — interactive analysis with explanations
- `data/raw/als_data.csv` — original input data
- `data/processed/` — reserved for derived data
- `outputs/` — reserved for generated visualizations
- `requirements.txt` — dependencies

## Run
Install dependencies from the project directory:
```bash
python -m pip install -r requirements.txt
```
Open `notebooks/ALS_Patient_Clustering.ipynb` in Jupyter or Google Colab and run the cells in order. When running in Colab, the notebook automatically loads `als_data.csv` from this public GitHub repository if the CSV is not available locally. The local notebook data loader supports execution from either the project root or the `notebooks` folder.

## Open the notebook in Google Colab
[**Open ALS Patient Clustering notebook in Colab**](https://colab.research.google.com/github/josephine-ms/josephine-ms.github.io/blob/main/Projects/ALS_Patient_Clustering/notebooks/ALS_Patient_Clustering.ipynb)

Select **Runtime → Run all**. The notebook automatically loads `als_data.csv` from GitHub when the dataset is not found locally (internet access required). A complete fresh-Colab execution has not yet been independently verified.

## Limitations and Ethics
K-means is sensitive to scaling and assumes distance-based group structure. Low silhouette scores suggest substantial overlap. Anonymized patient data still require responsible handling. No clinical decisions should rely on these clusters without independent validation.
