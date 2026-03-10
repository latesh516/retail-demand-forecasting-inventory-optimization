import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path

# -----------------------------------------
# 1. SET PROJECT PATHS (PORTABLE)
# -----------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

clean_data_path = BASE_DIR / "data" / "cleaned"
output_path = BASE_DIR / "outputs"

data_file = clean_data_path / "sales_data_cleaned.csv"

# create outputs folder automatically
output_path.mkdir(parents=True, exist_ok=True)

# -----------------------------------------
# 2. LOAD CLEAN DATASET
# -----------------------------------------

df = pd.read_csv(data_file)

print("Dataset shape:", df.shape)
print(df.head())

# -----------------------------------------
# 3. CONVERT DATE COLUMN
# -----------------------------------------

df['Date'] = pd.to_datetime(df['Date'])

# -----------------------------------------
# 4. CREATE TIME FEATURES
# -----------------------------------------

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Week'] = df['Date'].dt.isocalendar().week

# -----------------------------------------
# 5. TOTAL SALES TREND
# -----------------------------------------

weekly_sales = df.groupby('Date')['Weekly_Sales'].sum()

plt.figure(figsize=(12,6))
weekly_sales.plot()

plt.title("Total Weekly Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")

plt.savefig(output_path / "weekly_sales_trend.png")

plt.show()

# -----------------------------------------
# 6. MONTHLY SEASONALITY
# -----------------------------------------

monthly_sales = df.groupby('Month')['Weekly_Sales'].mean()

plt.figure(figsize=(10,5))
sns.barplot(x=monthly_sales.index, y=monthly_sales.values)

plt.title("Average Sales by Month")
plt.xlabel("Month")
plt.ylabel("Average Weekly Sales")

plt.savefig(output_path / "monthly_seasonality.png")

plt.show()

# -----------------------------------------
# 7. HOLIDAY IMPACT
# -----------------------------------------

holiday_sales = df.groupby('IsHoliday')['Weekly_Sales'].mean()

plt.figure(figsize=(6,4))
sns.barplot(x=holiday_sales.index, y=holiday_sales.values)

plt.title("Holiday vs Non-Holiday Sales")
plt.xlabel("Is Holiday")
plt.ylabel("Average Weekly Sales")

plt.savefig(output_path / "holiday_impact.png")

plt.show()

# -----------------------------------------
# 8. STORE PERFORMANCE
# -----------------------------------------

store_sales = df.groupby('Store')['Weekly_Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(12,6))
store_sales.head(10).plot(kind='bar')

plt.title("Top 10 Stores by Sales")
plt.xlabel("Store")
plt.ylabel("Total Sales")

plt.savefig(output_path / "top_stores.png")

plt.show()

# -----------------------------------------
# 9. DEPARTMENT PERFORMANCE
# -----------------------------------------

dept_sales = df.groupby('Dept')['Weekly_Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(12,6))
dept_sales.head(10).plot(kind='bar')

plt.title("Top Departments by Sales")
plt.xlabel("Department")
plt.ylabel("Total Sales")

plt.savefig(output_path / "top_departments.png")

plt.show()

# -----------------------------------------
# 10. EXTERNAL FACTORS CORRELATION
# -----------------------------------------

corr = df[['Weekly_Sales','Temperature','Fuel_Price','CPI','Unemployment']].corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm')

plt.title("Demand Correlation with External Factors")

plt.savefig(output_path / "correlation_matrix.png")

plt.show()