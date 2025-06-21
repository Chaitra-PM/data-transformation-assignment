# Python Data Cleaning Task

This task involved cleaning a messy sales dataset and computing a derived column.

## Approach:
- Used UDFs to clean and transform:
  - Converted types
  - Handled blanks and incorrect formats
  - Parsed various date formats
- Created a new column `total_price = quantity * price_per_unit`
- Saved cleaned data to `cleaned_sales.csv`

## Tools:
- pandas
- datetime
