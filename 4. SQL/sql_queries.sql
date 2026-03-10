-- SUPPLY CHAIN DEMAND ANALYTICS PROJECT
-- SQL ANALYTICS SCRIPT

/* -------------------------------
CREATE DATABASE
-------------------------------- */
CREATE DATABASE Retail_Demand_Analytics;
Go

USE Retail_Demand_Analytics;
GO

/* -------------------------------
1. CREATE TABLE
   -------------------------------- */
   CREATE TABLE sales_data (
   Store INT,
   Dept INT,
   Date DATE,
   Weekly_Sales FLOAT,
   IsHoliday VARCHAR(5),
   Temperature FLOAT,
   Fuel_Price FLOAT,
   CPI FLOAT,
   Unemployment FLOAT,
   Type VARCHAR(10),
   Size INT
   );

/* -------------------------------
2. BULK IMPORT CSV
-------------------------------- */
BULK INSERT sales_data
FROM 'C:\Data\sales_data_cleaned.csv'
WITH (
FIRSTROW = 2,
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n',
TABLOCK
);

/* Retrieve all data*/
SELECT * FROM sales_data;

/* For top 20*/
SELECT TOP 20 *
FROM sales_data;

/* -----------------------------
4. DATA VALIDATION
------------------------------*/

/* Verify dataset size */

SELECT COUNT(*) AS Total_Rows
FROM sales_data;


/* Check duplicate demand records */

SELECT
    Store,
    Dept,
    Date,
    COUNT(*) AS Duplicate_Count
FROM sales_data
GROUP BY Store, Dept, Date
HAVING COUNT(*) > 1;


/* Check negative sales (returns) */

SELECT COUNT(*) AS Negative_Sales
FROM sales_data
WHERE Weekly_Sales < 0;


/* -----------------------------
5. DEMAND ANALYTICS
------------------------------*/

/* Total company demand */

SELECT
    SUM(Weekly_Sales) AS Total_Company_Sales
FROM sales_data;


/* Top performing stores */

SELECT
    Store,
    SUM(Weekly_Sales) AS Total_Sales
FROM sales_data
GROUP BY Store
ORDER BY Total_Sales DESC;

/* Weekly Demand Trend */
SELECT
Date,
SUM(Weekly_Sales) AS Weekly_Demand
FROM sales_data
GROUP BY Date
ORDER BY Date;

/* Top product departments */

SELECT
    Dept,
    SUM(Weekly_Sales) AS Total_Sales
FROM sales_data
GROUP BY Dept
ORDER BY Total_Sales DESC;


/* Monthly demand trend */

SELECT
    YEAR(Date) AS Year,
    MONTH(Date) AS Month,
    SUM(Weekly_Sales) AS Monthly_Sales
FROM sales_data
GROUP BY
    YEAR(Date),
    MONTH(Date)
ORDER BY
    Year,
    Month;


/* Holiday demand impact */

SELECT
    IsHoliday,
    AVG(Weekly_Sales) AS Avg_Sales
FROM sales_data
GROUP BY IsHoliday;