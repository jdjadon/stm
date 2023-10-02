import yfinance as yf
import pandas as pd
import numpy as np

# Define the stock symbol for HDFC Bank
stock_symbol = "PREMEXPLN.NS"  # Use ".NS" for NSE-listed stocks

# Create a Ticker object for the stock
stock = yf.Ticker(stock_symbol)

# Fetch historical stock data for the desired date range
historical_data = stock.history(period="1y")

# Calculate daily percentage change in closing prices
historical_data['Close'] = historical_data['Close'].astype(float)
daily_pct_change = historical_data['Close'].pct_change().dropna()

# Define the RSI period (e.g., 14 days)
rsi_period = 14
# Calculate gains and losses based on percentage changes
gains = daily_pct_change.where(daily_pct_change > 0, 0)
losses = -daily_pct_change.where(daily_pct_change < 0, 0)

# Calculate average gains and losses over the RSI period
average_gains = gains.rolling(window=rsi_period).mean().dropna()
average_losses = losses.rolling(window=rsi_period).mean().dropna()

# Calculate relative strength (RS)
rs = average_gains / average_losses

# Calculate RSI
rsi = 100 - (100 / (1 + rs))

# Create a DataFrame to store the RSI values
rsi_data = pd.DataFrame({"RSI(14)": rsi})

# Display the DataFrame with RSI(14) values
print(rsi_data)
