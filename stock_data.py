"""
stock_data.py
Dictionary containing hardcoded stock prices.
No external API needed - this acts as the "database".
"""

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 170,
    "MSFT": 420,
}


def get_price(stock_name):
    """Return the price for a given stock symbol, or None if not found."""
    return STOCK_PRICES.get(stock_name.upper())


def get_all_stocks():
    """Return the full stock price dictionary."""
    return STOCK_PRICES


def is_valid_stock(stock_name):
    """Check if a stock symbol exists in the database."""
    return stock_name.upper() in STOCK_PRICES


def get_stock_symbols():
    """Return a list of all available stock symbols."""
    return list(STOCK_PRICES.keys())
