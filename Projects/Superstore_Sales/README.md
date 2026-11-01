# Superstore Sales and Business Performance Analysis

## Project overview
This project examines **9,994 retail order line items** to understand sales, profitability, and performance differences across categories, customer segments, regions, and time. The objective is to turn descriptive retail data into business-relevant findings while preserving the original exploratory notebook and a simpler, reproducible Python analysis.

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
- **File:** `data/Superstore.csv`.
- **Size:** 9,994 records and 21 columns.
- **Unit of analysis:** Order line item, not unique customer or unique order.
- **Relevant fields:** `Order Date`, `Sales`, `Profit`, `Discount`, `Category`, `Region`, and `Segment`.
- **Prepared notebook inputs:** `superstore_cleaned.csv`, `superstore_cleaned_encoded.csv`, and `superstore_encoded.csv` are retained for compatibility with the original exploratory notebook.

## Tools and methods
Python, pandas, Matplotlib, Jupyter Notebook, and the additional packages listed in `requirements.txt`.

The verified standalone script reads the original CSV, validates required columns and order dates, calculates portfolio KPIs, aggregates category/region/segment performance, creates monthly summaries, and saves charts and tables. The preserved notebook contains broader exploratory, statistical, and modeling work; results from those additional sections are not presented as independently verified here.

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

## How to run from GitHub on a computer
Prerequisites: Python and Git. Run from a terminal:

```bash
git clone https://github.com/josephine-ms/josephine-ms.github.io.git
cd josephine-ms.github.io/Projects/Superstore_Sales
python -m pip install -r requirements.txt
python scripts/superstore_sales_analysis.py
```

The script reads `data/Superstore.csv` relative to the project directory and writes outputs to `outputs/`. It was successfully executed against the supplied dataset during portfolio preparation.

## Open the original notebook in Google Colab
[**Open Superstore notebook in Colab**](https://colab.research.google.com/github/josephine-ms/josephine-ms.github.io/blob/main/Projects/Superstore_Sales/notebooks/superstore_exploratory_analysis.ipynb)

Use **Runtime → Run all**. The notebook contains portable data-loading changes intended to retrieve missing inputs from the public repository. **Full fresh-Colab execution has not yet been independently verified**, and later statistical/modeling cells may require additional dependencies or time. If Colab cannot locate a file, first confirm the corresponding CSV is committed to this repository.

For local Jupyter, launch `python -m notebook` from this project directory and open `notebooks/superstore_exploratory_analysis.ipynb`.

## Project folder layout

- `data/`: original Superstore CSV
- `notebooks/`: original exploratory notebook
- `scripts/`: reproducible standalone analysis
- `outputs/`: saved figures and summary tables
- `requirements.txt`: dependencies
- **Notebook compatibility files:** the three prepared CSVs remain at the project root because the original notebook still refers to those paths; they will be moved only after its entire execution has been verified.

## Limitations and responsible interpretation
This is a historical sample dataset rather than live retail data. Line-item losses do not establish that discounting caused the loss. Findings should be interpreted alongside costs, product strategy, and current operational context before making decisions.

## Reproducibility status
- **Standalone Python script:** executed successfully with the included dataset.
- **Original exploratory notebook:** preserved; complete fresh-environment Run all remains unverified.
- **Cleanup and file provenance:** see the single [portfolio cleanup log](../../PORTFOLIO_CLEANUP.md).
