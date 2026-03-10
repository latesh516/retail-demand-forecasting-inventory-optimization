                                            Retail Demand Forecasting & Inventory Optimization
Project Overview :

This project develops an end-to-end retail demand forecasting and inventory optimization system using the Walmart Store Sales dataset.
The system analyzes historical demand patterns, builds time-series forecasting models, and derives inventory policies such as Safety Stock, Reorder Point, and Economic Order Quantity (EOQ) to simulate real-world retail demand planning workflows.
The objective is to improve inventory decisions by reducing stockouts while minimizing excess inventory.
The workflow replicates how retail supply chain teams perform demand planning and inventory optimization in real business environments.
________________________________________
Business Problem:

Retail companies commonly face two major inventory management challenges:
1.	Stockouts – Products run out of inventory, leading to lost sales and poor customer experience.
2.	Overstocking – Excess inventory increases holding costs and ties up working capital.
Demand forecasting combined with inventory optimization helps companies maintain optimal inventory levels while meeting customer demand efficiently.
________________________________________
Dataset

Source: Walmart Store Sales Forecasting Dataset

Dataset Characteristics

Records: ~421,000 weekly sales observations

Stores: 45

Departments: Multiple product categories

Time Period: 2010 – 2012

The dataset includes store-level and department-level weekly sales along with external factors such as temperature, fuel prices, CPI, and unemployment indicators.
________________________________________
Tools & Technologies

Python (Pandas, NumPy, Stats models)

SQL Server

Excel
Time-Series Forecasting (ARIMA)

Inventory Optimization Modelling
________________________________________
Project Architecture

The project follows a typical demand planning analytics pipeline used in supply chain analytics:

Raw Data → Data Cleaning → Exploratory Analysis → Demand Forecasting → Inventory Optimization → SQL Demand Analytics
________________________________________
Project Workflow

1. Data Cleaning
Merged and cleaned multiple retail datasets using Python and Pandas, ensuring consistent time-series structure and validating data quality across approximately 421,000 records.
________________________________________
2. Exploratory Demand Analysis
Conducted exploratory analysis to identify:
•	demand seasonality
•	store-level performance patterns
•	department-level demand concentration
This analysis helped identify key demand drivers and seasonal trends.
________________________________________
3. Demand Forecasting
Implemented and compared multiple time-series forecasting models:
•	Moving Average
•	Exponential Smoothing
•	ARIMA
Model performance was evaluated using standard forecasting accuracy metrics, and ARIMA was selected as the final forecasting model.
________________________________________
4. Inventory Optimization
Using forecasted demand, inventory policies were calculated to maintain optimal stock levels.
Key inventory metrics computed include:
•	Safety Stock
•	Reorder Point
•	Economic Order Quantity (EOQ)
These calculations simulate real supply chain replenishment strategies used in retail operations.
________________________________________
5. SQL Demand Analytics
SQL was used to perform demand analytics, including:
•	store-level sales performance analysis
•	department-level demand analysis
•	demand trend analysis across time periods
This step demonstrates how cleaned analytical data can be used for business reporting and operational insights.
________________________________________
Inventory Optimization Example

Average Weekly Demand: ~22,500 units

Demand Standard Deviation: ~9,850 units

Safety Stock: ~16,260 units

Reorder Point: ~38,770 units

EOQ: ~40,120 units

These values illustrate how demand forecasts translate into operational inventory policies used in retail supply chain planning.
________________________________________
Key Insights

Demand shows significant spikes during holiday periods, indicating strong seasonal demand patterns.

A small number of departments generate a large share of total revenue, suggesting demand concentration across specific product categories.

Sales performance varies significantly across stores, highlighting differences in regional demand patterns.

High demand variability requires adequate safety stock levels to maintain desired service levels.

Retail demand demonstrates clear seasonal behavior, with higher sales occurring during late-year months due to holiday-driven purchasing patterns.

