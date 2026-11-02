# Superstore Sales and Business Performance Analysis

## Project overview
This project examines **9,994 retail order line items** to understand sales, profitability, and performance differences across categories, customer segments, regions, and time. The objective is to turn descriptive retail data into business-relevant findings while preserving a documented exploratory notebook and reproducible analytical outputs.

## Business problem
Strong revenue does not necessarily imply strong profit. A retailer needs to identify where sales generate losses, which product categories contribute profit, and which regions deserve closer investigation.

## Research questions
1. What are the overall sales, profit, and profit margin?
2. How many transaction lines show a loss?
3. Which product categories and regions contribute the most profit?
4. How do sales and profit vary over time?
5. Which areas warrant follow-up investigation before operational decisions are made?

## Dataset
- **Source:** Tableau Sample Superstore, used in the original coursework. [Original source](https://www.tableau.com/sites/default/files/2021-05/Sample%20-%20Superstore.xls).
- **File:** `data/raw/Superstore.csv`.
- **Size:** 9,994 records and 21 columns.
- **Unit of analysis:** Order line item, not unique customer or unique order.
- **Relevant fields:** `Order Date`, `Sales`, `Profit`, `Discount`, `Category`, `Region`, and `Segment`.
- **Prepared notebook inputs:** `data/processed/superstore_cleaned.csv`, `data/processed/superstore_cleaned_encoded.csv`, and `data/processed/superstore_encoded.csv` are retained for compatibility with the original exploratory notebook.

## Tools and methods
Python, pandas, Matplotlib, Jupyter Notebook, and the additional packages listed in `requirements.txt`.

The historical project generated summary KPIs, category/region/segment aggregates, and charts. The preserved notebook contains broader exploratory, statistical, and modeling work; results from those sections have not been independently revalidated.

## Key findings
| Measure | Result |
|---|---:|
| Total sales | **$2,297,200.86** |
| Total profit | **$286,397.02** |
| Overall profit margin | **12.47%** |
| Loss-making transaction lines | **1,871** |
| Highest-profit category | **Technology: $145,454.95** |
| Lowest-profit category | **Furniture: $18,451.27** |
| Highest-profit region | **West: $108,418.45** |

These findings come from the supplied historical sample. They indicate where to investigate product mix, pricing, and discount patterns; they do not establish causal explanations for losses.

## Visualizations and generated results
- [Monthly sales chart](outputs/monthly_sales.png)
- [Profit by category](outputs/profit_by_category.png)
- [Summary KPIs](outputs/summary_metrics.csv)
- [Category breakdown](outputs/sales_profit_by_category.csv)
- [Region breakdown](outputs/sales_profit_by_region.csv)
- [Segment breakdown](outputs/sales_profit_by_segment.csv)
- [Monthly sales and profit](outputs/monthly_sales_profit.csv)

## Run locally
Install dependencies with `python -m pip install -r requirements.txt`, then open `notebooks/Superstore_Sales.ipynb` in Jupyter and run the cells. Some dataset paths may require adjustment to the reorganized folders.

## Open the original notebook in Google Colab
[**Open Superstore notebook in Colab**](https://colab.research.google.com/github/josephine-ms/josephine-ms.github.io/blob/main/Projects/Superstore_Sales/notebooks/Superstore_Sales.ipynb)

Use **Runtime → Run all**. The original notebook has older dataset paths and may require path updates after this reorganization. **Full fresh-Colab execution has not yet been independently verified**, and later statistical/modeling cells may require additional dependencies or time. If Colab cannot locate a file, first confirm the corresponding CSV is committed to this repository.

For local Jupyter, launch `python -m notebook` from this project directory and open `notebooks/Superstore_Sales.ipynb`.

## Project folder layout

- `data/raw/`: original Superstore CSV
- `data/processed/`: three prepared and encoded CSVs
- `notebooks/`: original exploratory notebook
- `outputs/`: saved figures and summary tables
- `requirements.txt`: dependencies
- **Notebook compatibility files:** three prepared CSVs are stored in `data/processed/`. The notebook's full Run all is **not verified**, and its paths may need further adjustments.

## Limitations and responsible interpretation
This is a historical sample dataset rather than live retail data. Line-item losses do not establish that discounting caused the loss. Findings should be interpreted alongside costs, product strategy, and current operational context before making decisions.

## Reproducibility status
- **Historical output verification:** existing outputs were generated using a prior standalone workflow; that redundant script is no longer retained.
- **Original exploratory notebook:** preserved; complete fresh-environment Run all remains unverified.
- **Cleanup and file provenance:** see this project's [cleanup log](CLEANUP_LOG.md).
