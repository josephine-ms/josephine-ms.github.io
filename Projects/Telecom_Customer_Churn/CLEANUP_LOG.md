# Telecom Portfolio Cleanup Log

## Changes completed in this prepared package

| Original | Portfolio version | Action |
|---|---|---|
| `Josephine_jesuraj_DSC_680_Milestone2_Telecom_Churn_Integrated.ipynb` | `telecom_customer_churn_prediction.ipynb` | Renamed and updated title/data loading to local project-relative path; retained original analysis |
| `WA_Fn-UseC_-Telco-Customer-Churn.csv` | `data/telco_customer_churn.csv` | Copied and renamed dataset |
| `Josephine_jesuraj_DSC_680_Milestone2_Telecom_Churn_Integrated - JupyterLab.pdf` | Not published | Excluded duplicate notebook export from streamlined public project |
| `.ipynb_checkpoints/` and `*-checkpoint.ipynb` | Not published | Excluded automatic backups and outdated checkpoint variants |
| No standalone execution script | `telecom_churn_modeling.py` | Added runnable, fixed-parameter reproduction |
| No project-specific documentation in uploaded ZIP | `README.md`, `requirements.txt`, `.gitignore` | Added instructions and dependency listing |

## Validation performed
- Verified uploaded archive includes one primary notebook, the original dataset, PDF export, and checkpoint copies.
- Standalone Python script executed successfully on the included dataset and generated metrics, feature importance, and chart outputs.
- Original notebook preserved and modified for relative data path, but **not executed end-to-end**; its grid search and cross-validation may require additional time.
- No changes have been made directly to the live GitHub repository.

## Naming standard
Use lowercase snake_case for analysis files; descriptive titles for projects; keep conventional `README.md` and `requirements.txt`. Avoid week numbers, course codes, milestones, assignments, and duplicate copy suffixes in published names.
