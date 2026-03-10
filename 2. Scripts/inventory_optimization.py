# -----------------------------------------
# Import Libraries
# -----------------------------------------

import pandas as pd
import numpy as np

# -----------------------------------------
# Load Dataset
# -----------------------------------------
df = pd.read_csv(r"C:\Data\sales_data_cleaned.csv")

df['Date'] = pd.to_datetime(df['Date'])

# -----------------------------------------
# 1. Select Forecasted Product
# -----------------------------------------
series = df[(df['Store']==1) & (df['Dept']==1)]

# -----------------------------------------
# 2. Calculate Demand Statistics
# -----------------------------------------
avg_demand = series['Weekly_Sales'].mean()

std_demand = series['Weekly_Sales'].std()

annual_demand = series['Weekly_Sales'].sum()

print("Average Weekly Demand:", avg_demand)

print("Demand Std Dev:", std_demand)

print("Annual Demand:", annual_demand)

# -----------------------------------------
# 3. Define Inventory Parameters
# -----------------------------------------
service_level = 0.95

Z = 1.65

lead_time = 1   # week

ordering_cost = 50

holding_cost = 0.2

# -----------------------------------------
# 4. Safety Stock Calculation
# -----------------------------------------
safety_stock = Z * std_demand * np.sqrt(lead_time)

print("Safety Stock:", safety_stock)

# -----------------------------------------
# 5. Reorder Point
# -----------------------------------------
reorder_point = (avg_demand * lead_time) + safety_stock

print("Reorder Point:", reorder_point)

# -----------------------------------------
# 6. EOQ Calculation
# -----------------------------------------
EOQ = np.sqrt((2 * annual_demand * ordering_cost) / holding_cost)

print("Economic Order Quantity:", EOQ)

# -----------------------------------------
# 7. Inventory Results
# -----------------------------------------
results = pd.DataFrame({

"Metric": [
"Average Weekly Demand",
"Demand Std Dev",
"Safety Stock",
"Reorder Point",
"EOQ"
],

"Value": [
avg_demand,
std_demand,
safety_stock,
reorder_point,
EOQ
]

})

results.to_csv(r"C:\Data\inventory_results.csv", index=False)