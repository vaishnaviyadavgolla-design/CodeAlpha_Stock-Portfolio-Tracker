"""
file_handler.py
Save portfolio results to TXT or CSV files.
Files are saved into the 'data/' directory.
"""

import csv
import os
from datetime import datetime


# Ensure the data directory exists
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def _ensure_data_dir():
    """Create the data directory if it doesn't exist."""
    os.makedirs(DATA_DIR, exist_ok=True)


def save_as_txt(portfolio, total_investment):
    """Save portfolio summary to a .txt file in the data/ folder."""
    _ensure_data_dir()
    filename = os.path.join(DATA_DIR, "portfolio.txt")

    lines = []
    lines.append("Stock Portfolio Summary")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 50)
    lines.append(f"{'Stock':<8} {'Qty':>6} {'Price':>12} {'Value':>14}")
    lines.append("-" * 50)
    for item in portfolio:
        lines.append(
            f"{item['stock']:<8} {item['quantity']:>6} "
            f"${item['price']:>10,.2f} ${item['value']:>12,.2f}"
        )
    lines.append("-" * 50)
    lines.append(f"{'GRAND TOTAL':>28}  ${total_investment:>12,.2f}")
    lines.append("=" * 50)

    with open(filename, "w") as f:
        f.write("\n".join(lines))

    return filename


def save_as_csv(portfolio, total_investment):
    """Save portfolio summary to a .csv file in the data/ folder."""
    _ensure_data_dir()
    filename = os.path.join(DATA_DIR, "portfolio.csv")

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        for item in portfolio:
            writer.writerow([
                item["stock"],
                item["quantity"],
                item["price"],
                item["value"],
            ])
        writer.writerow([])
        writer.writerow(["", "", "GRAND TOTAL", total_investment])

    return filename


def prompt_save(portfolio, total_investment):
    """Ask user if they want to save, and in which format."""
    choice = input("\nWould you like to save the results? (yes/no): ").strip().lower()
    if choice not in ("yes", "y"):
        print("Results not saved. Goodbye!")
        return

    while True:
        fmt = input("Save as (txt / csv): ").strip().lower()
        if fmt == "txt":
            filename = save_as_txt(portfolio, total_investment)
            break
        elif fmt == "csv":
            filename = save_as_csv(portfolio, total_investment)
            break
        else:
            print("[!] Please choose 'txt' or 'csv'.")

    print(f"\n[OK] Results saved to '{filename}' successfully!")
