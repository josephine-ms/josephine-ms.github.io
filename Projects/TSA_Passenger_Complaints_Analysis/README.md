# TSA Passenger Complaints Analysis

## Project overview
Interactive Tableau analysis of TSA passenger complaints across U.S. airports, complaint categories and subcategories, time, and geographic locations. The dashboard is intended for airport operations and passenger-experience stakeholders.

## Business questions
- Which airports have the highest recorded complaint volumes?
- Which categories and subcategories drive the most complaints?
- How do complaint volumes vary across months and locations?
- Where should operational teams prioritize investigation?

## Data
The project uses four original Excel files under `data/raw/`:
- `complaints-by-airport.xlsx`
- `complaints-by-category.xlsx`
- `complaints-by-subcategory.xlsx`
- `iata-icao.xlsx` (airport identifiers and location reference)

## View the interactive dashboard online
[**Open TSA Passenger Complaints Analysis in Tableau Public**](https://public.tableau.com/app/profile/josephine.jesuraj/viz/Week910assignment/TSAComplaintsAnalysis)

This publicly shared Tableau Public view lets visitors explore the visualization in a browser without installing Tableau. The published workbook is titled `Week910assignment` in its current Tableau Public URL; the portfolio presentation uses the professional project title above.

## Dashboard and visualizations
The Tableau workbook contains six worksheets and two dashboards, including:
1. Top 50 airports by complaint count (bar chart)
2. Monthly TSA complaint trends (line chart)
3. Complaint categories (bubble chart)
4. Seasonal category patterns (heat map)
5. Complaint subcategories (treemap)
6. Geographic airport complaint hotspots (map)

## Findings
The original analysis identifies high complaint volumes at major hubs including LAX, JFK, EWR, ATL, and MCO. Prominent themes include expedited passenger screening, customer service, screening, and passenger property concerns. These are **raw complaint counts**, not rates adjusted for passenger traffic.

## Open the editable workbook locally
1. Install Tableau Desktop or a compatible Tableau authoring environment.
2. Open `tableau/TSA_Passenger_Complaints_Analysis.twb`.
3. If Tableau reports missing data sources, use **Data > Edit Connection** to point each Excel connection to the matching file in `data/raw/`.
4. Refresh the data and review the two dashboards. Save as a packaged workbook (`.twbx`) in Tableau if you want to distribute it with embedded data.

**Portability note:** The original workbook referenced Windows-specific Excel paths and temporary Tableau `.hyper` extracts. The four Excel source paths have been updated to project-relative paths; Tableau may still require manual reconnection or refresh, depending on its version and environment. This workbook has not been opened in Tableau for end-to-end validation.

## Limitations and ethics
- Airports with more travelers may have more complaints simply because of higher passenger volume; the analysis does not calculate complaint rates.
- Complaints reflect reported experiences and should not be interpreted as a complete measure of airport service quality.
- The source report describes publicly available TSA complaint data without personally identifying passenger information.

## Repository contents
- `tableau/` — editable Tableau workbook
- `data/raw/` — four source datasets
- `outputs/` — optional exported dashboard images
- `CLEANUP_LOG.md` — project-specific standardization record

## Tools
Tableau Desktop and Excel data sources. No Python notebook, Python script, or `requirements.txt` is needed for this Tableau-native project.
