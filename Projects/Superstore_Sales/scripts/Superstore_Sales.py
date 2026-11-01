"""Reproducible Superstore sales analysis from the original retail dataset."""
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent.parent
DATA = BASE / "data" / "raw" / "Superstore.csv"
OUT = BASE / "outputs"

def main():
    if not DATA.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA}")
    OUT.mkdir(exist_ok=True)
    df = pd.read_csv(DATA, encoding="latin1")
    required = {"Order Date", "Sales", "Profit", "Category", "Region", "Segment", "Discount"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y", errors="coerce")
    if df["Order Date"].isna().any():
        raise ValueError("Some order dates could not be parsed")
    summary = pd.DataFrame([{
        "records": len(df), "total_sales": df["Sales"].sum(),
        "total_profit": df["Profit"].sum(), "profit_margin_pct": 100 * df["Profit"].sum() / df["Sales"].sum(),
        "loss_making_lines": int((df["Profit"] < 0).sum())
    }])
    summary.to_csv(OUT / "summary_metrics.csv", index=False)
    for group, filename in [("Category", "sales_profit_by_category.csv"), ("Region", "sales_profit_by_region.csv"), ("Segment", "sales_profit_by_segment.csv")]:
        df.groupby(group, as_index=False).agg(sales=("Sales", "sum"), profit=("Profit", "sum"), transactions=("Sales", "size")).to_csv(OUT / filename, index=False)
    monthly = df.set_index("Order Date").resample("MS")[["Sales", "Profit"]].sum()
    monthly.to_csv(OUT / "monthly_sales_profit.csv")
    ax = monthly["Sales"].plot(figsize=(10, 5), title="Monthly Superstore Sales")
    ax.set_ylabel("Sales (USD)")
    ax.figure.tight_layout()
    ax.figure.savefig(OUT / "monthly_sales.png", dpi=150)
    plt.close(ax.figure)
    category = pd.read_csv(OUT / "sales_profit_by_category.csv")
    ax = category.plot.bar(x="Category", y="profit", legend=False, figsize=(8, 5), title="Profit by Product Category")
    ax.set_ylabel("Profit (USD)")
    ax.figure.tight_layout()
    ax.figure.savefig(OUT / "profit_by_category.png", dpi=150)
    plt.close(ax.figure)
    print(summary.to_string(index=False))
    print(f"Saved analysis to {OUT}")

if __name__ == "__main__":
    main()
