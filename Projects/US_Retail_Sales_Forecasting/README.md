# U.S. Retail Sales Forecasting

## Overview
This project examines U.S. monthly retail sales from January 1992 through June 2021 and evaluates a simple linear-regression forecasting baseline. The model is intended to demonstrate time-series preparation, chronological validation, and error interpretation rather than production-grade forecasting.

## Research question
How accurately can a linear time-trend model predict retail sales over the final 12 months of the historical series?

## Dataset and preparation
- **Source file:** `data/raw/us_retail_sales.csv` (provided with the original analysis).
- The source is organized by year, with months as columns. The analysis reshapes it into one observation per month, constructs dates, and sorts chronologically.
- **Training:** January 1992–June 2020 (342 months).
- **Holdout test:** July 2020–June 2021 (12 months).

## Methodology
1. Load and visualize the monthly series.
2. Use a chronological training/test split to prevent look-ahead leakage.
3. Construct a numerical month index as the regression predictor.
4. Fit `LinearRegression` on training observations.
5. Predict the 12 holdout months, compare actual and predicted sales, and compute root mean squared error (RMSE).

## Findings
The original analysis reports a fitted slope of approximately **873.05 sales units per month** and holdout **RMSE of approximately 66,433 sales units**. Retail sales generally rise over time, but the trend-only model misses seasonality and the unusual changes around the COVID-19 period. The reported values should be verified by rerunning the notebook with the supplied dataset.

## Project structure
- `notebooks/US_Retail_Sales_Forecasting.ipynb`: documented exploratory analysis.
- `data/raw/us_retail_sales.csv`: original dataset.
- `data/processed/`: reserved for transformed datasets.
- `outputs/`: reserved for optional generated figures.
- `CLEANUP_LOG.md`: project-specific portfolio preparation record.

## Open the notebook in Google Colab
[**Open U.S. Retail Sales Forecasting notebook in Colab**](https://colab.research.google.com/github/josephine-ms/josephine-ms.github.io/blob/main/Projects/US_Retail_Sales_Forecasting/notebooks/US_Retail_Sales_Forecasting.ipynb)

Open the link and select **Runtime → Run all**. The notebook automatically loads `us_retail_sales.csv` from this public GitHub repository if the CSV is not available locally (internet access required). Full fresh-Colab execution has not yet been independently verified.

## Run locally
From the project root, install dependencies with `python -m pip install -r requirements.txt`. Then open `notebooks/US_Retail_Sales_Forecasting.ipynb` in Jupyter and run the cells in order. The notebook checks dataset paths relative to either the project root or the `notebooks/` folder.

## Limitations and future work
A single linear time feature does not model seasonality, changing growth rates, or economic shocks. Compare seasonal-naive forecasts, SARIMA, and other models using rolling-origin evaluation before using forecasts for decisions. The source data ends in June 2021 and does not represent current retail conditions.
