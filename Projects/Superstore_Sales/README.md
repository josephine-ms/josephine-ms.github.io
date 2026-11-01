# Superstore Sales and Business Performance Analysis

## Business problem
Evaluate retail sales and profitability across product categories, customer segments, regions, and time. Identify where revenue does not translate into profit.

## Dataset
The included `data/Superstore.csv` contains **9,994 line-item records** and 21 columns, including order dates, sales, profit, discount, category, region, and customer segment. Source cited in the original notebook: [Tableau Sample Superstore](https://www.tableau.com/sites/default/files/2021-05/Sample%20-%20Superstore.xls). This repository includes the CSV from the original coursework archive.

## Findings from the supplied dataset
- Total sales: **$2,297,200.86**; total profit: **$286,397.02**; overall profit margin: **12.47%**.
- **1,871** transaction lines have negative profit.
- Highest-profit category: **Technology** ($145,454.95). Lowest-profit category: **Furniture** ($18,451.27).
- Highest-profit region: **West** ($108,418.45).

These are descriptive findings, not causal estimates. The original notebook also explores statistical tests and predictive modeling; its model metrics have not been independently reproduced here.

## Run the reproducible analysis
From this folder in GitHub Codespaces, a local terminal, or another Python environment:

```bash
python -m pip install -r requirements.txt
python superstore_sales_analysis.py
```

The script reads `data/Superstore.csv` and creates summary CSV files and PNG charts in `outputs/`. The script was executed successfully against the included dataset during portfolio preparation.

## Original notebook
`superstore_exploratory_analysis.ipynb` preserves the original exploratory work and its statistical and machine-learning sections. It expects the three prepared CSV files at the project root. Its full cell-by-cell execution is **not yet verified**. The accompanying standalone script is the verified reproducible entry point.

## Files
- `superstore_sales_analysis.py`: verified sales and profitability analysis
- `superstore_exploratory_analysis.ipynb`: original coursework notebook, renamed for portfolio use
- `data/Superstore.csv`: original input data
- `superstore_cleaned.csv`, `superstore_cleaned_encoded.csv`, `superstore_encoded.csv`: prepared datasets used by original notebook
- `outputs/`: generated results and figures

## Limitations
This is a historical sample retail dataset. Discounts and profits may be associated but the analysis does not establish that discounts cause losses. Results are not forecasts of current retail performance.
<<<<<<< HEAD

## Run the notebook (professor/reviewer)

[**Open notebook in Google Colab**](https://colab.research.google.com/github/josephine-ms/josephine-ms.github.io/blob/main/Projects/Superstore_Sales/superstore_exploratory_analysis.ipynb)

1. Open the link above and choose **Runtime → Run all**.
2. The setup cell downloads missing project datasets from this public GitHub repository. No manual file upload or local path editing is required, provided the datasets have been committed to GitHub.
3. Wait for the analysis to finish. Some model tuning cells can take several minutes.

**Local alternative:** Clone the repository, change directory to `Projects/Superstore_Sales`, install dependencies using `python -m pip install -r requirements.txt`, then run the notebook in Jupyter or execute the included `.py` analysis script.

**Verification note:** These notebooks have been modified for portable data loading, but a complete fresh-Colab `Run all` has not been independently verified. Please report any remaining execution error for correction.

=======
>>>>>>> 5392c29ea4162752488bcc9bf6730d9100e2aaa8
