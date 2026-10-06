"""
main.py
Entry point for the Stock Portfolio Tracker application.
"""

from stock_data import get_all_stocks
from portfolio import get_stock_count, collect_portfolio, display_summary
from file_handler import prompt_save

SEPARATOR = "=" * 60
THIN_SEP = "-" * 60


def display_available_stocks():
    """Display all available stocks and their prices."""
    stocks = get_all_stocks()
    print(f"\n{SEPARATOR}")
    print("       AVAILABLE STOCKS & PRICES")
    print(SEPARATOR)
    print(f"  {'Stock':<10} {'Price per Share':>15}")
    print(THIN_SEP)
    for stock, price in stocks.items():
        print(f"  {stock:<10} ${price:>13,.2f}")
    print(SEPARATOR)


def main():
    """Entry point for the Stock Portfolio Tracker."""
    print(f"\n{SEPARATOR}")
    print("       STOCK PORTFOLIO TRACKER")
    print(SEPARATOR)

    display_available_stocks()

    stock_count = get_stock_count()
    portfolio = collect_portfolio(stock_count)
    total_investment = display_summary(portfolio)
    prompt_save(portfolio, total_investment)


if __name__ == "__main__":
    main()
