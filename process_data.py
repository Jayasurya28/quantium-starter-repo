import pandas as pd
import glob

# Step 1: Load all CSVs
csv_files = glob.glob('data/daily_sales_data_*.csv')
dfs = [pd.read_csv(file) for file in csv_files]

# Step 2: Concatenate all dataframes
df = pd.concat(dfs, ignore_index=True)

# Step 3: Filter for 'pink morsel' only
df = df[df['product'] == 'pink morsel']

# Step 4: Calculate 'sales' column
df['sales'] = df['quantity'].astype(int) * df['price'].str.replace('$', '').astype(float)

# Step 5: Keep only the required columns
final_df = df[['sales', 'date', 'region']]

# Step 6: Export to CSV
final_df.to_csv('processed_sales_data.csv', index=False)

print("Data processing complete. Output saved to 'processed_sales_data.csv'")
