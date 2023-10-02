import yfinance as yf

# Define the correct stock symbol for HDFC Bank
stock_symbol = "PREMEXPLN.NS"  # Use ".NS" for NSE-listed stocks

# Create a Ticker object for the stock
stock = yf.Ticker(stock_symbol)

# Fetch historical stock data for the last 1 year
historical_data = stock.history(period="1y")

# Select only the columns you want (excluding "Dividends" and "Stock Splits")
filtered_data = historical_data.loc[:, ["Open", "High", "Low", "Close", "Volume"]]

# Remove the time part from the date and keep only the date
filtered_data.index = filtered_data.index.date

# Display the filtered historical data with date only
print(filtered_data)
