"""
portfolio.py
Investment calculation logic for the Stock Portfolio Tracker.
Handles collecting user input, computing values, and displaying the summary.
"""

from stock_data import get_price, is_valid_stock, get_stock_symbols

SEPARATOR = "=" * 60
THIN_SEP = "-" * 60


def get_stock_count():
    """Ask user how many different stocks they want to enter."""
    while True:
        try:
            count = int(input("\nHow many different stocks do you want to enter? "))
            if count <= 0:
                print("[!] Please enter a positive number.")
                continue
            return count
        except ValueError:
            print("[!] Invalid input. Please enter a whole number.")


def get_stock_name(index):
    """Prompt for a valid stock name, re-asking on invalid input."""
    while True:
        name = input(f"\n  Stock #{index} - Enter stock symbol: ").strip().upper()
        if is_valid_stock(name):
            return name
        print(f"  [!] '{name}' not found. Available: {', '.join(get_stock_symbols())}")


def get_stock_quantity(stock_name):
    """Prompt for the quantity of shares owned."""
    while True:
        try:
            qty = int(input(f"  Enter quantity of {stock_name} shares you own: "))
            if qty <= 0:
                print("  [!] Quantity must be a positive number.")
                continue
            return qty
        except ValueError:
            print("  [!] Invalid input. Please enter a whole number.")


def collect_portfolio(stock_count):
    """Collect all stock entries from the user and calculate values."""
    portfolio = []
    for i in range(1, stock_count + 1):
        name = get_stock_name(i)
        qty = get_stock_quantity(name)
        price = get_price(name)
        value = price * qty
        portfolio.append({
            "stock": name,
            "quantity": qty,
            "price": price,
            "value": value,
        })
    return portfolio


def calculate_total(portfolio):
    """Calculate the grand total investment value."""
    return sum(item["value"] for item in portfolio)


def display_summary(portfolio):
    """Print a formatted summary table of the portfolio and return the total."""
    total_investment = calculate_total(portfolio)

    print(f"\n{SEPARATOR}")
    print("       PORTFOLIO SUMMARY")
    print(SEPARATOR)
    print(f"  {'Stock':<8} {'Qty':>6} {'Price':>12} {'Value':>14}")
    print(THIN_SEP)
    for item in portfolio:
        print(
            f"  {item['stock']:<8} {item['quantity']:>6} "
            f"${item['price']:>10,.2f} ${item['value']:>12,.2f}"
        )
    print(THIN_SEP)
    print(f"  {'GRAND TOTAL':>28}  ${total_investment:>12,.2f}")
    print(SEPARATOR)

    return total_investment
