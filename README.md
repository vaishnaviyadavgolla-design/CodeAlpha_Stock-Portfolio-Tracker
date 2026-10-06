# Stock Portfolio Tracker

A simple console-based Stock Portfolio Tracker built in Python. Track your stock investments, view a formatted summary, and export results to TXT or CSV.

## Features

- Hardcoded stock price database (no external API needed)
- Interactive console input with validation
- Clean formatted portfolio summary table
- Export results to `.txt` or `.csv`
- Modular, well-structured codebase

## Project Structure

```
Stock-Portfolio-Tracker/
|
|-- README.md
|-- LICENSE
|-- requirements.txt
|-- .gitignore
|
|-- main.py                 # Main program
|-- stock_data.py           # Dictionary containing stock prices
|-- portfolio.py            # Investment calculation logic
|-- file_handler.py         # Save results to TXT/CSV
|
|-- data/
|   |-- portfolio.txt       # Generated after saving
|   |-- portfolio.csv       # Generated after saving
|
|-- screenshots/
|   |-- home.png
|   |-- calculation.png
|   |-- saved_file.png
|
|-- sample_output/
|   |-- output1.txt
|   |-- output2.txt
|
|-- docs/
    |-- Project_Report.pdf
    |-- Flowchart.png
```

## Available Stocks

| Symbol | Price per Share |
|--------|---------------|
| AAPL   | $180.00       |
| TSLA   | $250.00       |
| GOOG   | $140.00       |
| AMZN   | $170.00       |
| MSFT   | $420.00       |

## How to Run

1. Clone the repository or download the project folder.
2. Open a terminal and navigate to the `Stock-Portfolio-Tracker/` directory.
3. Run the program:

```bash
python main.py
```

4. Follow the on-screen prompts to:
   - Enter the number of stocks you want to track
   - Enter stock symbols and quantities
   - View your portfolio summary
   - Optionally save results to TXT or CSV

## Key Concepts Demonstrated

- **Dictionary** - Stock name to price lookup
- **Input/Output** - Getting user data, displaying formatted results
- **Basic Arithmetic** - Price x Quantity, running total
- **File Handling** - Optional `.txt` / `.csv` export
- **Modular Design** - Separated concerns across multiple files

## Requirements

- Python 3.6 or higher
- No external packages required (uses only standard library)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
