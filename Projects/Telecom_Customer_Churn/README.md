# Telecom Customer Churn Prediction

## Business problem
Identify customers at risk of leaving a telecommunications provider so retention teams can prioritize outreach. Predictions are associations, not evidence of causation.

## Data
IBM Telco Customer Churn sample, **7,043 customer records**. Local file: `data/telco_customer_churn.csv`. Target: `Churn` (Yes/No). The customer identifier is excluded from modeling. `TotalCharges` is converted to numeric and missing values are imputed within the training pipeline.

## Methods
The preserved notebook compares a dummy baseline, Logistic Regression, tuned Random Forest, and XGBoost. It uses an 80/20 stratified split, feature engineering, imputation, one-hot encoding, scaling, and training-only SMOTE. The notebook also includes cross-validation, threshold analysis, and feature importance.

The executable Python script runs a **faster, fixed-parameter reproduction** of the same modeling families; it does not repeat the notebook's Random Forest grid search or full cross-validation. Therefore its metrics may differ from those reported in the notebook.

## Verified results from the standalone script

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Dummy Baseline | 0.735 | 0.000 | 0.000 | 0.000 | 0.500 |
| Logistic Regression | 0.743 | 0.510 | 0.791 | 0.621 | 0.841 |
| Random Forest | 0.767 | 0.554 | 0.631 | 0.590 | 0.835 |
| XGBoost | 0.785 | 0.592 | 0.610 | 0.601 | 0.840 |

Observed churn by contract type:

- Month-to-month: 42.71% of 3,875 customers
- One year: 11.27% of 1,473 customers
- Two year: 2.83% of 1,695 customers

The Random Forest importance table is in `outputs/random_forest_feature_importance.csv`. These rankings describe predictive contributions, not causal drivers.

## How to run (GitHub Codespaces or locally)

```bash
cd Projects/Telecom_Customer_Churn
python -m pip install -r requirements.txt
python telecom_churn_modeling.py
```

To inspect the original analysis notebook:

```bash
jupyter notebook telecom_customer_churn_prediction.ipynb
```

Run notebook cells in order from this project folder. The notebook includes a more computationally expensive grid search and cross-validation, and has **not** been fully rerun as part of this packaging.

## Outputs
`outputs/model_metrics.csv`, `outputs/churn_by_contract.csv`, `outputs/churn_by_contract.png`, and `outputs/random_forest_feature_importance.csv`.

## Limitations and ethics
This public sample omits customer satisfaction, complaints, competitor pricing, and operational incidents. Test performance may not generalize to live customers. Use retention scores with fairness monitoring, privacy controls, and human review.

## Source and credit
Based on Josephine Jesuraj's original DSC 680 churn notebook. Dataset distributed as the IBM Telco Customer Churn sample. The public-facing filename removes course and milestone references; the original work is preserved in the cleaned notebook.
