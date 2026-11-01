# Telecom Customer Churn Prediction

## Project overview
This project uses **7,043 customer records** from the IBM Telco Customer Churn sample to investigate customer attrition and compare predictive models. The business objective is to identify customers who may benefit from proactive retention outreach while balancing model accuracy with the ability to detect actual churners.

## Business problem
Retention teams have limited time and resources. A model that achieves high accuracy but misses many customers who churn may be less useful than one with stronger recall. This project examines that trade-off rather than selecting a model on accuracy alone.

## Research questions
1. How common is churn in the sample?
2. How does churn vary by contract type?
3. How do Logistic Regression, Random Forest, and XGBoost compare against a simple baseline?
4. Which model offers the best trade-off among accuracy, recall, F1, and ROC-AUC?
5. What limitations matter before applying predictions to retention decisions?

## Dataset
- **Source:** IBM Telco Customer Churn sample.
- **File:** `data/telco_customer_churn.csv`.
- **Records:** 7,043; **churned:** 1,869 (approximately 26.54%).
- **Target:** `Churn` (Yes/No).
- **Example predictors:** `tenure`, `Contract`, `MonthlyCharges`, `TotalCharges`, payment method, and service subscriptions.
- **Data preparation:** Customer identifier excluded; `TotalCharges` converted to numeric; missing values imputed within the modeling pipeline.

## Tools and methodology
Python, pandas, NumPy, scikit-learn, imbalanced-learn (SMOTE), XGBoost, Matplotlib, and Jupyter.

The standalone analysis uses an **80/20 stratified train/test split**, feature engineering, numeric scaling, categorical one-hot encoding, and SMOTE applied to the training data. It compares a dummy majority-class baseline with Logistic Regression, Random Forest, and XGBoost. The original notebook contains additional cross-validation, tuning, and threshold analysis.

**Important:** The reproducible script uses fixed model parameters and does not repeat every tuning step in the original notebook; results can therefore differ.

## Model results from the executed standalone script
| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Dummy baseline | 73.46% | 0.00% | 0.00% | 0.000 | 0.500 |
| Logistic Regression | 74.31% | 51.03% | **79.14%** | **0.621** | **0.841** |
| Random Forest | 76.72% | 55.40% | 63.10% | 0.590 | 0.835 |
| XGBoost | **78.50%** | **59.22%** | 60.96% | 0.601 | 0.840 |

**Interpretation:** XGBoost has the highest accuracy in this execution. Logistic Regression has higher recall, finding more of the customers who actually churned. Which model is preferable depends on the cost of missed churners versus unnecessary outreach.

## Observed churn by contract
| Contract type | Customers | Churn rate |
|---|---:|---:|
| Month-to-month | 3,875 | **42.71%** |
| One year | 1,473 | 11.27% |
| Two year | 1,695 | 2.83% |

These are descriptive associations and should not be interpreted as proof that contract length causes churn.

## Outputs
- [Model comparison metrics](outputs/model_metrics.csv)
- [Churn by contract chart](outputs/churn_by_contract.png)
- [Churn by contract table](outputs/churn_by_contract.csv)
- [Random Forest feature importance](outputs/random_forest_feature_importance.csv)

## How to run from GitHub on a computer
Prerequisites: Python and Git.

```bash
git clone https://github.com/josephine-ms/josephine-ms.github.io.git
cd josephine-ms.github.io/Projects/Telecom_Customer_Churn
python -m pip install -r requirements.txt
python telecom_churn_modeling.py
```

The script reads `data/telco_customer_churn.csv` relative to its own location and writes results to `outputs/`. It was previously executed successfully with the supplied dataset.

## Open the original notebook in Google Colab
[**Open Telecom notebook in Colab**](https://colab.research.google.com/github/josephine-ms/josephine-ms.github.io/blob/main/Projects/Telecom_Customer_Churn/telecom_customer_churn_prediction.ipynb)

Select **Runtime → Run all**. The notebook includes a setup cell intended to retrieve the dataset from the public repository when it is missing locally. **Full fresh-Colab execution, including tuning and cross-validation, has not yet been independently verified.** Model fitting may take several minutes.

For local Jupyter, from this project directory run `python -m notebook` and open `telecom_customer_churn_prediction.ipynb`.

## Limitations, ethics, and future work
The dataset is a public sample and lacks customer satisfaction, competitor pricing, service incidents, and other potentially important factors. Predictive importance is not causation. In real deployments, protect customer privacy, review fairness across customer groups, monitor performance drift, and use human judgment for retention interventions. Future work includes threshold calibration, cost-sensitive evaluation, and external validation.

## Reproducibility status
- **Standalone Python script:** executed successfully with the supplied dataset.
- **Original notebook:** preserved; full fresh-environment Run all remains unverified.
- **Cleanup and file provenance:** see the single [portfolio cleanup log](../../PORTFOLIO_CLEANUP.md).
