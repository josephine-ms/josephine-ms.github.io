# Portfolio Cleanup - TSA Passenger Complaints Analysis

## Original materials reviewed
- `Week 9&10 assignment.twb` — Tableau workbook
- `complaints-by-airport.xlsx`, `complaints-by-category.xlsx`, `complaints-by-subcategory.xlsx`, `iata-icao.xlsx` — source data
- `Josephine_DSC_640_Week9&10 Assignment.docx` — narrative and screenshot reference, **not included** in the GitHub package

## Standardization applied
- Renamed Tableau workbook to `TSA_Passenger_Complaints_Analysis.twb`.
- Organized source spreadsheets in `data/raw/`.
- Renamed two generic Tableau dashboard labels to `TSA Complaints Overview` and `TSA Complaints Details`.
- Replaced the workbook's four original machine-specific Excel source paths with project-relative `../data/raw/` paths.
- Added a professional project README and project-specific cleanup document.
- Excluded the academic submission document and other unnecessary deliverables.
- Did not invent a Python notebook or script for a Tableau-only project.

## Validation and remaining work
- Confirmed the Tableau workbook XML parses and contains **6 worksheets** and **2 dashboards**.
- Confirmed four Excel source connection references were rewritten.
- Tableau itself was **not run** in this environment. The workbook also contains references to local temporary `.hyper` extracts from the original authoring session; reconnect or refresh the Excel data in Tableau if prompted.
- The original report's findings were used for documentation, but its visualizations have not been independently recalculated here.

## GitHub placement
`Projects/TSA_Passenger_Complaints_Analysis/`
