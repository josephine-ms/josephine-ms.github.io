# Portfolio Cleanup and Verification Log

This is the **single repository-wide cleanup record** for the data science portfolio. Project-specific READMEs describe research questions, data, methods, findings, and execution; cleanup decisions are documented here. This record is based on changes documented during portfolio preparation and the files currently visible in GitHub. Unverified work is explicitly identified.

## 1. Superstore Sales and Business Performance Analysis

**Source:** Original coursework archive `Final_Project.zip`.

### Renamed and organized
| Original item | Portfolio location / action |
|---|---|
| `Josephine_jesuraj_DSC_530_Final Project .ipynb` | Renamed to `Projects/Superstore_Sales/notebooks/superstore_exploratory_analysis.ipynb` |
| `Data/Superstore.csv` | Retained as `Projects/Superstore_Sales/data/Superstore.csv` |
| `superstore_cleaned.csv`, `superstore_cleaned_encoded.csv`, `superstore_encoded.csv` | Retained at project root for original-notebook compatibility |
| Original coursework report/drafts | Not published in current project folder pending content review |

### Corrected or added
- Created `superstore_sales_analysis.py` as a standalone reproducible analysis with paths relative to the script.
- Added `requirements.txt`, `.gitignore`, results tables, charts, and an expanded project README.
- Added portable dataset-loading changes and a Colab link to the original notebook workflow.
- Removed unresolved Git merge-conflict markers from the README during this repository cleanup.

### Excluded from portfolio package
- `.ipynb_checkpoints/` and older duplicate notebook copies.
- Older draft storytelling material, retained only in the original archive.

### Verification
- **Confirmed during portfolio preparation:** 9,994 records, 21 columns; standalone script executed and generated results.
- **Not confirmed:** complete original notebook execution from a fresh Colab session; review of the unpublished storytelling report.

## 2. Telecom Customer Churn Prediction

**Source:** Original DSC 680 milestone notebook and IBM Telco Customer Churn sample.

### Renamed and organized
- Notebook published as `Projects/Telecom_Customer_Churn/notebooks/telecom_customer_churn_prediction.ipynb`.
- Dataset published as `Projects/Telecom_Customer_Churn/data/telco_customer_churn.csv`.
- Standalone modeling script published as `Projects/Telecom_Customer_Churn/scripts/telecom_churn_modeling.py`.
- Model comparison outputs and contract churn chart published in `outputs/`.

### Corrected or added
- Added portable dataset retrieval in the notebook to address Colab's different working directory.
- Created a fixed-parameter standalone reproduction with preprocessing, SMOTE, and multiple classifiers.
- Expanded the README with real metrics, business interpretation, and local/Colab instructions.
- Documented the distinction between the faster standalone script and the original tuned notebook.

### Excluded from portfolio package
- Automatic notebook checkpoints and redundant notebook PDF export were excluded during preparation.

### Verification
- **Confirmed during portfolio preparation:** 7,043 records; standalone script executed and produced model comparison metrics.
- **Not confirmed:** complete original notebook execution from a fresh Colab session, including tuning and cross-validation.

## 3. Repository-wide maintenance

- **2026-11-01:** Consolidated separate project cleanup logs into this single root-level `PORTFOLIO_CLEANUP.md`.
- **2026-11-01:** Replaced short project READMEs with project-specific documentation following the supplied reference style.
- **2026-11-01:** Removed the repository root `README.md` as requested; project documentation is maintained in each project's README.
- **2026-11-01:** Removed redundant `Projects/Superstore_Sales/CLEANUP_LOG.md` and `Projects/Telecom_Customer_Churn/CLEANUP_LOG.md` after consolidating their relevant contents here.

- **2026-11-01:** Reorganized both published projects into consistent `notebooks/` and `scripts/` directories. Adjusted standalone script base paths and Colab README links. Retained original notebook bytes and prepared Superstore CSVs to avoid speculative notebook edits.

## Pending tasks
- Run both original notebooks end-to-end in fresh Colab runtimes and record any necessary fixes.
- Notebook and standalone-script files have been placed in common `notebooks/` and `scripts/` directories, and README links and script paths were updated. The three Superstore prepared CSVs remain at the project root for original-notebook compatibility until its complete execution is verified.
- Review and publish remaining portfolio projects as their original files become available.
- Record future verified fixes, renamed files, and removed materials **here**, not in separate project cleanup logs.

**Documentation rule:** Record only confirmed changes. An uploaded notebook or a previously executed standalone script does not, by itself, prove that a fresh Colab `Run all` succeeds.
