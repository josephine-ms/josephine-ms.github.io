# Kia and Hyundai Vehicle Theft Analysis

## Overview
Exploratory R analysis of Kia/Hyundai vehicle theft patterns and comparisons with other vehicle thefts across U.S. cities, including a focused view of Milwaukee. The project uses CSV datasets and a multi-city Excel workbook to create six visualizations.

## Research Focus
- How did Kia/Hyundai theft counts change over time across the cities in the supplied data?
- How do Kia/Hyundai theft counts compare with other vehicle thefts?
- Which cities account for the largest recorded counts in the analyzed dataset?
- What was the 2022 vehicle-theft composition in Milwaukee?

## Methods and Visualizations
1. **Area chart:** Kia/Hyundai theft trends in the multi-city Excel dataset.
2. **Stacked area chart:** Kia/Hyundai thefts versus other vehicle thefts by year.
3. **Donut chart:** Milwaukee's 2022 theft composition.
4. **Treemap:** Total Kia/Hyundai theft counts by city.
5. **Stacked bar chart:** Vehicle theft composition for the ten highest-total cities in 2022.
6. **Pie chart:** Share of Kia/Hyundai theft counts among the five highest-count cities.

The R workflow parses date and numeric fields, reshapes wide Excel data to long format, aggregates counts, and produces graphics using `ggplot2` and `treemapify`.

## Project Structure
- `notebooks/Kia_Hyundai_Vehicle_Theft_Analysis.Rmd` — documented R Markdown analysis
- `scripts/Kia_Hyundai_Vehicle_Theft_Analysis.R` — executable R script extracted from the analysis
- `data/raw/` — original four input datasets
- `data/processed/` — reserved for optional derived data
- `outputs/` — reserved for exported visualizations
- `PORTFOLIO_CLEANUP.md` — project-specific cleanup record

## Reproduce
Install R and the packages listed in `requirements.txt`. Open the project root as the RStudio working directory, then run:

```r
rmarkdown::render("notebooks/Kia_Hyundai_Vehicle_Theft_Analysis.Rmd", output_dir = "outputs")
```

Or run `source("scripts/Kia_Hyundai_Vehicle_Theft_Analysis.R")` from the project root. R Markdown generates an HTML report rather than a submission PDF.

## Interpretation and Limitations
The charts summarize the provided data, not a complete census of all vehicle thefts. City-level counts should not be interpreted as per-capita risk without population and reporting adjustments. Trends may reflect differences in coverage, reporting, and data completeness. The analysis is descriptive, not causal; it does not establish why thefts occurred or whether any specific security measure caused changes.

## Data Attribution
The included workbook is labeled *Motherboard VICE News Kia Hyundai Theft Data*. Confirm original publication and redistribution permissions before making the underlying datasets publicly available. The source files have been retained without altering their contents.

## Validation
The CSV column schemas and file presence were inspected, and the R Markdown chunks were extracted to a standalone R script. Full R execution could not be verified in the preparation environment because an R runtime was unavailable.
