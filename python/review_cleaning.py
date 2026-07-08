import pandas as pd
import os

# Override with the OLIST_PROJECT_DIR environment variable if the layout differs.
PROJECT_DIR = os.environ.get(
    'OLIST_PROJECT_DIR',
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

input_path  = os.path.join(PROJECT_DIR, 'data', 'raw', 'olist_order_reviews_dataset.csv')
output_path = os.path.join(PROJECT_DIR, 'data', 'cleaned', 'olist_order_reviews_cleaned.csv')

# Read the problematic CSV using pandas which handles embedded newlines properly
df = pd.read_csv(input_path, on_bad_lines='skip')

print(f"Rows loaded: {len(df)}")
print(f"Columns: {list(df.columns)}")

# Remove embedded newlines and carriage returns from text columns
df['review_comment_title']   = df['review_comment_title'].astype(str).str.replace('\n', ' ').str.replace('\r', ' ')
df['review_comment_message'] = df['review_comment_message'].astype(str).str.replace('\n', ' ').str.replace('\r', ' ')

os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print(f"Cleaned file saved to: {output_path}")
