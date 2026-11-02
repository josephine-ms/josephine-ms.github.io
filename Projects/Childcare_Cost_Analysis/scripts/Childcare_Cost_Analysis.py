"""Exploratory childcare cost and affordability analysis."""

import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, HTML, Markdown
from pathlib import Path
import warnings
import squarify

warnings.filterwarnings("ignore")

# paths relative to notebook location
# Resolve project files from the repository root or notebooks directory.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_FOLDER = PROJECT_ROOT / "data" / "raw"
GRAPH_FOLDER = PROJECT_ROOT / "outputs"
GRAPH_FOLDER.mkdir(parents=True, exist_ok=True)

# Load the source dataset
file_path = DATA_FOLDER / "nationaldatabaseofchildcareprices.xlsx"
df = pd.read_excel(file_path)

# 2. Basic structure review
print("Shape:", df.shape)
print("Number of columns:", len(df.columns))
print("Years:", df["StudyYear"].min(), "to", df["StudyYear"].max())
print("States:", df["State_Name"].nunique())
print("Counties:", df["County_FIPS_Code"].nunique())
display(HTML("<h3 style='font-weight:bold;'>Dataset outputs</h3>"))
display(df.head())

# 3. Group columns by meaning
geo_cols = ["State_Name", "State_Abbreviation", "County_Name", "County_FIPS_Code", "StudyYear"]
demographic_examples = [
    "UNR_16", "UNR_20to64", "FLFPR_20to64", "MLFPR_20to64",
    "PR_F", "PR_P", "MHI", "ME", "FME", "MME",
    "TotalPop", "Households", "Hispanic"
]
childcare_broad_cols = [
    "MCInfant", "MCToddler", "MCPreschool",
    "MFCCInfant", "MFCCToddler", "MFCCPreschool",
    "_75CInfant", "_75CToddler", "_75CPreschool",
    "_75FCCInfant", "_75FCCToddler", "_75FCCPreschool"
]

# 4. Create a field dictionary
field_meanings = {
    "State_Name": "State name",
    "State_Abbreviation": "State abbreviation",
    "County_Name": "County name",
    "County_FIPS_Code": "County FIPS code",
    "StudyYear": "Year of the childcare market rate study",
    "MHI": "Median household income",
    "ME": "Median earnings",
    "FME": "Female median earnings",
    "MME": "Male median earnings",
    "PR_P": "Poverty rate / poverty-related measure for population",
    "PR_F": "Poverty-related measure for families",
    "UNR_16": "Unemployment rate age 16+",
    "UNR_20to64": "Unemployment rate age 20 to 64",
    "FLFPR_20to64": "Female labor force participation rate age 20 to 64",
    "MLFPR_20to64": "Male labor force participation rate age 20 to 64",
    "MCInfant": "Median weekly center-based childcare price for infants",
    "MCToddler": "Median weekly center-based childcare price for toddlers",
    "MCPreschool": "Median weekly center-based childcare price for preschoolers",
    "MFCCInfant": "Median weekly family child care price for infants",
    "MFCCToddler": "Median weekly family child care price for toddlers",
    "MFCCPreschool": "Median weekly family child care price for preschoolers",
    "_75CInfant": "75th percentile weekly center-based childcare price for infants",
    "_75CToddler": "75th percentile weekly center-based childcare price for toddlers",
    "_75CPreschool": "75th percentile weekly center-based childcare price for preschoolers",
    "_75FCCInfant": "75th percentile weekly family child care price for infants",
    "_75FCCToddler": "75th percentile weekly family child care price for toddlers",
    "_75FCCPreschool": "75th percentile weekly family child care price for preschoolers"
}

field_dictionary = pd.DataFrame(
    [{"Field": k, "Meaning": v} for k, v in field_meanings.items() if k in df.columns]
)

# 5. Missing data review

missing_summary = (
    df[childcare_broad_cols + ["MHI", "PR_P", "UNR_20to64", "FLFPR_20to64"]]
    .isna()
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)
missing_summary.columns = ["Field", "Missing_Rate"]

# 6. National summary of childcare prices
price_summary = df[childcare_broad_cols].describe().T

# 7. Trend analysis by year
yearly_medians = (
    df.groupby("StudyYear")[["MCInfant", "MCPreschool", "MFCCInfant", "MFCCPreschool"]]
    .median()
    .round(2)
)
display(HTML("<h3 style='font-weight:bold;'>Yearly median childcare prices</h3>"))
display(yearly_medians)

# Plot trend: center infant vs family infant
plt.figure(figsize=(10, 6))
plt.plot(yearly_medians.index, yearly_medians["MCInfant"], marker="o", label="Center Infant")
plt.plot(yearly_medians.index, yearly_medians["MFCCInfant"], marker="o", label="Family Child Care Infant")
plt.title("Median Weekly Infant Childcare Price by Year")
plt.xlabel("Study Year")
plt.ylabel("Weekly Price ($)")
plt.legend()
plt.tight_layout()
# Save and display Graph
plt.savefig(GRAPH_FOLDER / "infant_childcare_price_trends.png", dpi=300, bbox_inches="tight")
plt.show()

# 8. Compare child age groups
age_compare = pd.DataFrame({
    "Center-Based Median": [
        df["MCInfant"].median(),
        df["MCToddler"].median(),
        df["MCPreschool"].median()
    ],
    "Family Child Care Median": [
        df["MFCCInfant"].median(),
        df["MFCCToddler"].median(),
        df["MFCCPreschool"].median()
    ]
}, index=["Infant", "Toddler", "Preschool"]).round(2)

display(HTML("<h3 style='font-weight:bold;'>Median prices by age group</h3>"))
display(age_compare)
#plot graph
age_compare.plot(kind="bar", figsize=(10, 6))
plt.title("Median Weekly Childcare Price by Age Group and Provider Type")
plt.xlabel("Age Group")
plt.ylabel("Weekly Price ($)")
plt.xticks(rotation=0)
plt.tight_layout()
# Save and display Graph
plt.savefig(GRAPH_FOLDER / "childcare_prices_by_age_and_provider.png", dpi=300, bbox_inches="tight")
plt.show()

# 9. State comparison for latest year
latest_year = df["StudyYear"].max()
df_latest = df[df["StudyYear"] == latest_year].copy()
state_rank = (
    df_latest.groupby("State_Name")[["MCInfant", "MCPreschool", "MFCCInfant", "MFCCPreschool"]]
    .median()
    .sort_values("MCInfant", ascending=False)
    .round(2)
)
display(HTML("<h3 style='font-weight:bold;'>State comparison for latest year</h3>"))

display(Markdown(f"Top 10 states by median center-based infant price in {latest_year}:"))
display(state_rank.head(10))

display(Markdown(f"Bottom 10 states by median center-based infant price in {latest_year}:"))
display(state_rank.tail(10))

# 10. Affordability burden
# Convert weekly prices to annual estimate
for col in ["MCInfant", "MCPreschool", "MFCCInfant", "MFCCPreschool"]:
    df_latest[f"{col}_annual"] = df_latest[col] * 52
    df_latest[f"{col}_share_income"] = df_latest[f"{col}_annual"] / df_latest["MHI_2018"]

affordability_cols = [c for c in df_latest.columns if c.endswith("_share_income")]
affordability_summary = df_latest[affordability_cols].median().sort_values(ascending=False).round(3)

display(HTML("<h3 style='font-weight:bold;'>Affordability burden</h3>"))
display(Markdown(f"Median affordability burden in {latest_year} (annual childcare / median household income)"))
display(affordability_summary)

top_burden = (
    df_latest[["State_Name", "County_Name", "MCInfant", "MHI_2018", "MCInfant_share_income"]]
    .dropna()
    .sort_values("MCInfant_share_income", ascending=False)
    .head(15)
)
display(Markdown(f"Counties with highest center-based infant affordability burden in {latest_year}:"))
display(top_burden)

# 11. Relationship with income, poverty, and labor force participation
corr_cols = [
    "MCInfant", "MCPreschool", "MFCCInfant", "MFCCPreschool",
    "MHI_2018", "PR_P", "UNR_20to64", "FLFPR_20to64"
]
corr_matrix = df_latest[corr_cols].corr().round(2)
display(HTML("<h3 style='font-weight:bold;'>Relationship with income, poverty, and labor force participation</h3>"))
display(Markdown("Correlation matrix:"))
display(corr_matrix)

# Scatter plot: center infant price vs median household income
plot_df = df_latest[["MCInfant", "MHI_2018"]].dropna()
plt.figure(figsize=(8, 6))
plt.scatter(plot_df["MHI_2018"], plot_df["MCInfant"], alpha=0.4)
plt.title(f"Center-Based Infant Price vs Median Household Income ({latest_year})")
plt.xlabel("Median Household Income (2018 dollars)")
plt.ylabel("Weekly Center-Based Infant Price ($)")
plt.tight_layout()
# Save and display Graph
plt.savefig(GRAPH_FOLDER / "infant_price_vs_household_income.png", dpi=300, bbox_inches="tight")
plt.show()
display(Markdown("Analysis complete!"))