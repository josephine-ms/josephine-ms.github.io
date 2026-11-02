# Portfolio Cleanup - U.S. Retail Sales Forecasting

## Naming and organization
- Renamed the original course/assignment notebook to `US_Retail_Sales_Forecasting.ipynb`.
- Removed the redundant standalone Python script `scripts/US_Retail_Sales_Forecasting.py` so the notebook is the single executable workflow.
- Placed the original CSV under `data/raw/` and updated data-loading paths.
- Organized the remaining files into `notebooks/`, `data/`, and `outputs/`.
- Added a portfolio-oriented `README.md` and `requirements.txt`.

## Excluded content
- The Jupyter `-checkpoint.ipynb` backup, which is not needed when the primary notebook is retained.
- Assignment instructions, course identifiers, author/date submission metadata, and irrelevant academic framing.
- Stale notebook execution outputs (cleared to keep the notebook portable and reviewable).
- No final-submission PDF is included.

## Validation
- Earlier packaging checks confirmed notebook JSON loads and code cells parse as Python; the later Colab data-loading edit has not been executed independently.
- Full execution and metric reproduction have **not** been verified in this packaging step.
- Original research conclusions are retained; reported numerical findings remain subject to rerun verification.

## Google Colab compatibility
- Added a direct **Open in Google Colab** link and instructions to the project README, following the Telecom and ALS presentation style.
- Updated the notebook to load `data/raw/us_retail_sales.csv` locally when present, otherwise retrieve it automatically from this public GitHub repository.
- Set the notebook's internal Colab filename metadata to `US_Retail_Sales_Forecasting.ipynb`.
- Fresh Google Colab **Run all** verification remains pending.

## Repository location
`Projects/US_Retail_Sales_Forecasting/`
