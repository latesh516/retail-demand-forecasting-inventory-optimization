import pandas as pd
import numpy as np
from pathlib import Path

# -----------------------------------------
# 1. SET PROJECT PATHS (PORTABLE)
# -----------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

raw_data_path = BASE_DIR / "Raw data"
clean_data_path = BASE_DIR / "data" / "cleaned"

train_path = raw_data_path / "train.csv"
features_path = raw_data_path / "features.csv"
stores_path = raw_data_path / "stores.csv"

output_path = clean_data_path / "sales_data_cleaned.csv"

# -----------------------------------------
# 2. LOAD DATA
# -----------------------------------------

train = pd.read_csv(train_path)
features = pd.read_csv(features_path)
stores = pd.read_csv(stores_path)

print("Train shape:", train.shape)
print("Features shape:", features.shape)
print("Stores shape:", stores.shape)

# -----------------------------------------
# 3. CONVERT DATE FORMAT
# -----------------------------------------

train['Date'] = pd.to_datetime(train['Date'], format='%d-%m-%Y')
features['Date'] = pd.to_datetime(features['Date'], format='%d-%m-%Y')

# -----------------------------------------
# 4. HANDLE MISSING VALUES
# -----------------------------------------

markdown_cols = [
    'MarkDown1', 'MarkDown2', 'MarkDown3',
    'MarkDown4', 'MarkDown5'
]

features[markdown_cols] = features[markdown_cols].fillna(0)

features['CPI'] = features['CPI'].ffill()
features['Unemployment'] = features['Unemployment'].ffill()

# -----------------------------------------
# 5. CHECK NEGATIVE SALES
# -----------------------------------------

negative_sales = train[train['Weekly_Sales'] < 0]
print("Negative sales rows:", negative_sales.shape[0])

# -----------------------------------------
# 6. MERGE DATASETS
# -----------------------------------------

data = pd.merge(
    train,
    features,
    on=['Store', 'Date', 'IsHoliday'],
    how='left'
)

data = pd.merge(
    data,
    stores,
    on='Store',
    how='left'
)

print("Merged dataset shape:", data.shape)

# -----------------------------------------
# 7. DROP PROMOTION COLUMNS
# -----------------------------------------

data = data.drop(columns=[
    'MarkDown1', 'MarkDown2', 'MarkDown3',
    'MarkDown4', 'MarkDown5'
])

# -----------------------------------------
# 8. SORT DATA
# -----------------------------------------

data = data.sort_values(['Store', 'Dept', 'Date'])

# -----------------------------------------
# 9. SAVE CLEAN DATA
# -----------------------------------------

# -----------------------------------------
# 9. SAVE CLEAN DATA
# -----------------------------------------

clean_data_path.mkdir(parents=True, exist_ok=True)

data.to_csv(output_path, index=False)

print("Clean dataset saved to:", output_path)
print("Final shape:", data.shape)

# -----------------------------------------
# 10. CHECK MISSING VALUES
# -----------------------------------------

df = pd.read_csv(output_path)

print(df.isnull().sum())

# -----------------------------------------
# 11. CHECK DUPLICATES
# -----------------------------------------

duplicates = df.duplicated(subset=['Store', 'Dept', 'Date']).sum()

print("Duplicate rows:", duplicates)