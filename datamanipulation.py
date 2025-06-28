
import kagglehub
import os
import pandas as pd
import numpy as np

# Step 1: Download dataset from Kaggle
path = kagglehub.dataset_download("mobile phone usage .csv")
print("📁 Dataset downloaded to:", path)

# Step 2: Locate CSV file inside the downloaded folder
csv_file = next((f for f in os.listdir(path) if f.endswith('.csv')), None)

if not csv_file:
    raise FileNotFoundError("❌ No CSV file found in downloaded dataset folder!")

full_csv_path = os.path.join(path, csv_file)

# Step 3: Load data into Pandas DataFrame
df = pd.read_csv(full_csv_path)
print("\n🔍 First 5 rows of the dataset:")
print(df.head())

# Step 4: Clean column names (remove spaces and make lowercase)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Step 5: Show basic information
print("\n📊 Dataset Info:")
print(df.info())

# Step 6: Describe numeric columns
print("\n📈 Statistics:")
print(df.describe())

# Step 7: Fill missing values (if any) with median (for numeric columns)
df.fillna(df.median(numeric_only=True), inplace=True)

# Step 8: Add a derived column: log of data usage (if applicable)
if 'data_usage_gb' in df.columns:
    df['log_data_usage'] = np.log1p(df['data_usage_gb'])

# Step 9: Filter heavy users (> 5 GB)
if 'data_usage_gb' in df.columns:
    heavy_users = df[df['data_usage_gb'] > 5]
    print("\n🚀 Users with >5GB usage:")
    print(heavy_users.head())

# Step 10: Group average data usage by region (if applicable)
if 'region' in df.columns and 'data_usage_gb' in df.columns:
    region_usage = df.groupby('region')['data_usage_gb'].mean()
    print("\n🌍 Average data usage by region:")
    print(region_usage)

# Step 11: Save cleaned version of dataset
output_file = "cleaned_mobile_usage.csv"
df.to_csv(output_file, index=False)
print(f"\n✅ Cleaned data saved to: {output_file}")
