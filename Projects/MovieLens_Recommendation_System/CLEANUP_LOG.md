# MovieLens Recommendation System — Portfolio Cleanup

## Original source
`Josephine_jesuraj_DSC_630_Assignment_10.2.ipynb` and MovieLens `movies.csv`, `ratings.csv`, `tags.csv`, `links.csv`, `README.txt`.

## Changes
- Renamed project, notebook, and script to `MovieLens_Recommendation_System`.
- Removed course codes, student names, week and assignment references from the public notebook and filenames.
- Excluded checkpoint files, submission PDFs, unrelated churn notebooks, and duplicated artifacts.
- Organized original datasets under `data/raw/`, preserving the MovieLens source README and usage license.
- Replaced the memory-intensive full cosine-similarity matrix with sparse storage and on-demand similarity computation; this preserves the original item-based cosine recommendation approach.
- Replaced the blocking `input()` loop with a reproducible example and callable functions.
- Corrected the original narrative's Pearson-correlation references to cosine similarity, matching the actual implementation.
- Ranked recommendations by similarity (rather than re-sorting by average rating after selecting candidates).
- Added project README, dependencies, and standardized structure.

## Validation
- Standalone script and notebook code were syntax-checked.
- Full script execution is checked separately; see delivery message for outcome.

## Exclusions
Original assignment headers, PDF submissions, checkpoints, unrelated notebooks, and duplicate course files are not part of this package.
