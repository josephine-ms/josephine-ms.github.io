# Data Science & Analytics Portfolio

A portfolio of applied analytics, business intelligence, and machine-learning work, with an emphasis on translating data into decisions. The repository supports the public website at **https://josephine-ms.github.io/**.

## Featured projects

| Project | Business focus | Reproducible entry point |
|---|---|---|
| [Superstore Sales and Business Performance Analysis](Projects/Superstore_Sales/README.md) | Retail profitability, loss-making transactions, and category/region performance | `Projects/Superstore_Sales/superstore_sales_analysis.py` |
| [Telecom Customer Churn Prediction](Projects/Telecom_Customer_Churn/README.md) | Customer retention, churn classification, and model trade-offs | `Projects/Telecom_Customer_Churn/telecom_churn_modeling.py` |

The public website also describes planned portfolio projects. A project description on the website does **not** mean that its source code has already been published in this repository.

## Repository organization

```text
index.html
README.md                    # Portfolio overview (this file)
PORTFOLIO_CLEANUP.md         # One repository-wide cleanup and verification log
Projects/
  Superstore_Sales/
    README.md
    requirements.txt
    data/
    outputs/
    superstore_exploratory_analysis.ipynb
    superstore_sales_analysis.py
  Telecom_Customer_Churn/
    README.md
    requirements.txt
    data/
    outputs/
    telecom_customer_churn_prediction.ipynb
    telecom_churn_modeling.py
```

## How to run a project

1. Clone this repository: `git clone https://github.com/josephine-ms/josephine-ms.github.io.git`.
2. Enter the relevant project folder under `Projects/`.
3. Install dependencies: `python -m pip install -r requirements.txt`.
4. Execute the project's standalone Python script, or open its notebook using the **Open in Colab** link in its README.

Each project README documents its dataset, methods, results, outputs, limitations, and exact commands. The standalone scripts have previously been executed with their supplied data; full fresh-environment execution of the original notebooks remains a separate verification step.

## Portfolio maintenance

All repository cleanup and verification history is maintained in [PORTFOLIO_CLEANUP.md](PORTFOLIO_CLEANUP.md). Project READMEs describe the research and implementation, rather than repeating cleanup logs.

## Contact

See the [portfolio website](https://josephine-ms.github.io/) for professional background and contact information.
