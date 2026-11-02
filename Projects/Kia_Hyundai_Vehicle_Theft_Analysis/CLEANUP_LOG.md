# Portfolio Cleanup — Kia and Hyundai Vehicle Theft Analysis

## Scope
Standardized the supplied R analysis and data files into a standalone portfolio project without academic submission packaging.

## Renaming and Reorganization
- Renamed the academic R Markdown source to `notebooks/Kia_Hyundai_Vehicle_Theft_Analysis.Rmd`.
- Created `scripts/Kia_Hyundai_Vehicle_Theft_Analysis.R` from the original executable code chunks.
- Updated all four dataset references to use `data/raw/` relative to the project root.
- Replaced the original PDF-oriented R Markdown header with an HTML output configuration.
- Added `README.md`, `requirements.txt`, and organized `data/`, `notebooks/`, `scripts/`, and `outputs/` folders.

## Exclusions
- Removed course, assignment, week, student, and dated submission metadata from the published analysis header.
- Did not include any generated final-output PDF, temporary files, or unrelated coursework.
- Kept all four provided input datasets because they are referenced by the source workflow.

## Validation and Caveats
- Checked input file presence and inspected CSV schemas.
- Preserved six original chart analyses.
- Full R execution was **not** verified because R is not installed in the preparation environment.
- Confirm source data redistribution rights before publishing the workbook and datasets publicly.
- The cleaned project has not been uploaded to GitHub automatically.
