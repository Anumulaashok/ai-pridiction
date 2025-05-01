import yfinance as yf

def fetch_stock_data(symbol, period="60d"):
    """Fetches the closing stock prices for a given symbol for the specified period."""
    data = yf.download(symbol, period=period, interval="1d")
    # Return only the 'Close' prices as a numpy array
    return data["Close"].values
