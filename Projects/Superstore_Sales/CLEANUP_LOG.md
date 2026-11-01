<<<<<<< HEAD
## Reproducibility update (2026-11-01)

- Added notebook setup cell to fetch missing datasets from the public GitHub repository.
- Added Colab link and execution instructions to README.
- Replaced a hard-coded Windows CSV path with `data/Superstore.csv`.
- Full notebook execution in fresh Colab remains to be verified.
=======
# Portfolio Cleanup and Verification Log

## Superstore Sales and Business Performance Analysis

Source: uploaded `Final_Project.zip` (local coursework folder). Changes below were made to the **portfolio copy**, not to the originals on the user's computer.

| Original file/path | Portfolio action | New location / name |
|---|---|---|
| `Josephine_jesuraj_DSC_530_Final Project .ipynb` | Retained; renamed and replaced course/week header with descriptive title | `Projects/Superstore_Sales/superstore_exploratory_analysis.ipynb` |
| `Data/Superstore.csv` | Retained, unchanged input | `Projects/Superstore_Sales/data/Superstore.csv` |
| `superstore_cleaned.csv` | Retained for notebook compatibility | `Projects/Superstore_Sales/superstore_cleaned.csv` |
| `superstore_cleaned_encoded.csv` | Retained for notebook compatibility | `Projects/Superstore_Sales/superstore_cleaned_encoded.csv` |
| `superstore_encoded.csv` | Retained for notebook compatibility | `Projects/Superstore_Sales/superstore_encoded.csv` |
| `Part 2 - Data Storytelling.docx` | Not included in public package pending content/privacy review | Original archive only |
| `Data Storytelling_old.docx` | Excluded as old draft | Original archive only |
| `archive/` | Excluded as duplicate/older notebook versions | Original archive only |
| `.ipynb_checkpoints/` | Excluded as automatic checkpoint files | Original archive only |

## New portfolio files
- `superstore_sales_analysis.py`: standalone analysis with explicit relative paths and reproducible CSV/PNG outputs.
- `README.md`: business question, real descriptive findings, data information, how to run, limitations.
- `requirements.txt`: installation dependencies.
- `.gitignore`: prevents temporary notebook and Python files from being committed.

## Testing
- [x] Source ZIP inspected and original notebook identified (48 cells).
- [x] Original `Superstore.csv` inspected (9,994 rows, 21 columns).
- [x] Standalone Python analysis executed successfully with supplied dataset.
- [x] Summary tables and plots generated.
- [ ] Original Jupyter notebook executed end-to-end in a clean environment.
- [ ] Files uploaded to GitHub and public project link verified.
- [ ] Storytelling report reviewed for public release.

No claims are made that the user's original local folder or GitHub repository has already been modified.
>>>>>>> 5392c29ea4162752488bcc9bf6730d9100e2aaa8
