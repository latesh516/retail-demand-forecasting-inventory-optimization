import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA

from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error

# -----------------------------------------
# 1. SET PROJECT PATHS (PORTABLE)
# -----------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

clean_data_path = BASE_DIR / "data" / "cleaned"
output_chart_path = BASE_DIR / "outputs"

data_file = clean_data_path / "sales_data_cleaned.csv"

# create output folder automatically
output_chart_path.mkdir(parents=True, exist_ok=True)

# -----------------------------------------
# 2. LOAD CLEAN DATASET
# -----------------------------------------

df = pd.read_csv(data_file)

df['Date'] = pd.to_datetime(df['Date'])

print("Dataset loaded:", df.shape)

# -----------------------------------------
# 3. SELECT ONE DEMAND SERIES
# -----------------------------------------

series = df[(df['Store'] == 1) & (df['Dept'] == 1)]

series = series[['Date', 'Weekly_Sales']]

series = series.sort_values('Date')

series.set_index('Date', inplace=True)

series = series.asfreq('W-FRI')

# -----------------------------------------
# 4. VISUALIZE DEMAND SERIES
# -----------------------------------------

plt.figure(figsize=(12,6))

plt.plot(series)

plt.title("Store 1 Dept 1 Weekly Demand")

plt.xlabel("Date")
plt.ylabel("Sales")

plt.savefig(output_chart_path / "demand_series.png")

plt.show()

# -----------------------------------------
# 5. SPLIT TRAIN / TEST DATA
# -----------------------------------------

train_size = int(len(series) * 0.8)

train = series[:train_size]

test = series[train_size:]

# -----------------------------------------
# 6. MODEL 1 — MOVING AVERAGE
# -----------------------------------------

window = 4

moving_avg = train['Weekly_Sales'].rolling(window).mean()

forecast_ma = moving_avg.iloc[-1]

forecast_ma = [forecast_ma] * len(test)

# -----------------------------------------
# 7. MODEL 2 — EXPONENTIAL SMOOTHING
# -----------------------------------------

model_es = ExponentialSmoothing(
    train['Weekly_Sales'],
    trend='add',
    seasonal='add',
    seasonal_periods=52
)

fit_es = model_es.fit()

forecast_es = fit_es.forecast(len(test))

# -----------------------------------------
# 8. MODEL 3 — ARIMA
# -----------------------------------------

model_arima = ARIMA(train['Weekly_Sales'], order=(1,1,1))

fit_arima = model_arima.fit()

forecast_arima = fit_arima.forecast(len(test))

# -----------------------------------------
# 9. EVALUATE FORECAST ACCURACY
# -----------------------------------------

def evaluate(actual, forecast):

    mape = mean_absolute_percentage_error(actual, forecast)

    rmse = np.sqrt(mean_squared_error(actual, forecast))

    return mape, rmse


mape_ma, rmse_ma = evaluate(test['Weekly_Sales'], forecast_ma)

mape_es, rmse_es = evaluate(test['Weekly_Sales'], forecast_es)

mape_arima, rmse_arima = evaluate(test['Weekly_Sales'], forecast_arima)

# -----------------------------------------
# 10. PRINT RESULTS
# -----------------------------------------

print("Moving Average")

print("MAPE:", mape_ma)

print("RMSE:", rmse_ma)

print()

print("Exponential Smoothing")

print("MAPE:", mape_es)

print("RMSE:", rmse_es)

print()

print("ARIMA")

print("MAPE:", mape_arima)

print("RMSE:", rmse_arima)

# -----------------------------------------
# 11. PLOT FORECAST COMPARISON
# -----------------------------------------

plt.figure(figsize=(12,6))

plt.plot(test.index, test['Weekly_Sales'], label='Actual')

plt.plot(test.index, forecast_es, label='Exponential Smoothing')

plt.plot(test.index, forecast_arima, label='ARIMA')

plt.legend()

plt.title("Forecast vs Actual")

plt.savefig(output_chart_path / "forecast_vs_actual.png")

plt.show()