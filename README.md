### Stock Dividend Info Fetcher

This Python script fetches stock information for a list of tickers provided in a CSV file, including the following details:

- **Name**: The name of the stock.
- **Ticker**: The stock ticker symbol.
- **Last Close Price**: The last closing price of the stock (rounded to 3 decimal places).
- **Upcoming Dividend Amount**: The next expected dividend amount for the stock.
- **Upcoming Dividend Date**: The date of the next expected dividend.

The output is saved in a CSV file named `stock_dividend_info.csv`.

## Features
- Fetches data using the `yfinance` library.
- Handles missing data gracefully by defaulting to `N/A`.
- Outputs clean, formatted data ready for analysis or reporting.

---

## Installation

1. **Clone or download the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required dependencies:**

   Make sure you have Python 3.7 or newer installed on your machine.

   Install the required Python libraries using `pip`:

   ```bash
   pip install yfinance pandas
   ```

---

## Usage

1. **Prepare the Input CSV File:**

   Create a CSV file containing the stock tickers you want to fetch information for. The file should have a column named `Ticker`, and each row should have one stock ticker.

   Example `stock_tickers.csv`:

   ```csv
   Ticker
   AAPL
   MSFT
   TSLA
   ```

2. **Run the Script:**

   Execute the script with the input CSV file as an argument:

   ```bash
   python fetch_dividends.py stock_tickers.csv
   ```

   Replace `stock_tickers.csv` with the path to your input file if it’s in a different location.

3. **Output File:**

   After running the script, the output will be saved in a file named `stock_dividend_info.csv` in the same directory as the script.

   Example output:

   ```csv
   Name,Ticker,Last Close Price,Upcoming Dividend Amount,Upcoming Dividend Date
   Apple Inc.,AAPL,174.450,0.220,2023-12-07
   Microsoft Corporation,MSFT,312.560,0.620,2023-11-16
   Tesla, Inc.,TSLA,239.870,N/A,N/A
   ```

---

## Explanation

### Input:
- A CSV file containing the stock tickers (e.g., `stock_tickers.csv`).

### Process:
- The script uses `yfinance` to fetch stock information for each ticker.
- For each stock, the following data is fetched:
  - **Name**: From the stock’s `shortName`.
  - **Ticker**: The ticker symbol from the input file.
  - **Last Close Price**: Obtained from the most recent `Close` value in the stock’s daily history.
  - **Upcoming Dividend Amount**: Extracted from the `dividendRate` field in the stock’s metadata.
  - **Upcoming Dividend Date**: From the `Ex-Dividend Date` in the stock’s `calendar`.

### Output:
- A CSV file (`stock_dividend_info.csv`) containing the processed information for each stock.

---

## Error Handling
- If a stock ticker is invalid or data is missing, the respective fields will be marked as `Error` or `N/A` in the output file.
- The script prints detailed error messages in the console for debugging purposes.

---

## Example

### Input File (`stock_tickers.csv`):

```csv
Ticker
AAPL
MSFT
TSLA
```

### Running the Script:

```bash
python fetch_stock_data_with_upcoming_dividends.py stock_tickers.csv
```

### Output File (`stock_dividend_info.csv`):

```csv
Name,Ticker,Last Close Price,Upcoming Dividend Amount,Upcoming Dividend Date
Apple Inc.,AAPL,174.450,0.220,2023-12-07
Microsoft Corporation,MSFT,312.560,0.620,2023-11-16
Tesla, Inc.,TSLA,239.870,N/A,N/A
```

---

## Troubleshooting

- **Missing dependencies:** If the script fails due to missing libraries, ensure you have installed the required dependencies using `pip install yfinance pandas`.
- **Incorrect file path:** Ensure the input CSV file is in the same directory as the script or provide the correct relative/absolute path when running the script.
- **Network errors:** The script requires an active internet connection to fetch data from Yahoo Finance.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements

- [Yahoo Finance](https://finance.yahoo.com/) for providing stock data.
- The `yfinance` library for easy access to financial data.
``` 

This `README.md` provides clear guidance for installation, usage, and troubleshooting for your script. Let me know if you'd like to make further adjustments!