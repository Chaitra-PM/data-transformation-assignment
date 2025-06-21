# SQL Task: Product Table Comparison

This task compares two versions of a product catalog using SQL in Python.

## Approach:
- Used SQLite via Python to import CSVs as SQL tables.
- Identified added and removed products.
- Compared matching rows to detect column-level changes (e.g., price, stock).
- Output saved as `added_removed_rows.csv` and `column_level_diff.csv`.

## Tools:
- pandas
- sqlite3

