import pandas as pd
from datetime import datetime

# Load raw data
df = pd.read_csv('raw_sales.csv')

# Cleaning function
def clean_sales_data(df):
    df = df.copy()
    
    def safe_int(val):
        try:
            return int(val)
        except:
            return 0
    
    def safe_float(val):
        try:
            return float(val)
        except:
            return 0.0
    
    def parse_date(val):
        for fmt in ("%Y/%m/%d", "%Y-%m-%d", "%d-%m-%Y"):
            try:
                return pd.to_datetime(val, format=fmt)
            except:
                continue
        return pd.NaT

    df['order_id'] = df['order_id'].apply(safe_int)
    df['product_id'] = df['product_id'].apply(safe_int)
    df['quantity'] = df['quantity'].apply(safe_int)
    df['price_per_unit'] = df['price_per_unit'].apply(safe_float)
    df['order_date'] = df['order_date'].apply(parse_date)

    return df

def calculate_total_price(row):
    return row['quantity'] * row['price_per_unit']

# Apply cleaning
cleaned_df = clean_sales_data(df)
cleaned_df['total_price'] = cleaned_df.apply(calculate_total_price, axis=1)

# Save result
cleaned_df.to_csv('cleaned_sales.csv', index=False)
cleaned_df

