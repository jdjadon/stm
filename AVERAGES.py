import yfinance as yf
import pandas as pd

# Define the correct stock symbol for HDFC Bank
stock_symbol = "HDFCBANK.NS"  # Use ".NS" for NSE-listed stocks

# Create a Ticker object for the stock
stock = yf.Ticker(stock_symbol)

# Fetch historical stock data for the last 1 year
historical_data = stock.history(period="1y")

# Select only the "Close" column
close_prices = historical_data["Close"]

# Calculate the exponential moving averages
ema_5 = close_prices.ewm(span=5, adjust=False).mean()
ema_10 = close_prices.ewm(span=10, adjust=False).mean()
ema_20 = close_prices.ewm(span=20, adjust=False).mean()
ema_50 = close_prices.ewm(span=50, adjust=False).mean()
ema_100 = close_prices.ewm(span=100, adjust=False).mean()

# Create a DataFrame to store the exponential moving averages
ema_data = pd.DataFrame({
    "Close": close_prices,
    "5-Day EMA": ema_5,
    "10-Day EMA": ema_10,
    "20-Day EMA": ema_20,
    "50-Day EMA": ema_50,
    "100-Day EMA": ema_100
})

# Display the DataFrame with exponential moving averages
print(ema_data)
