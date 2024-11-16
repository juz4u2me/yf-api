import yfinance as yf
import pandas as pd
import sys
import os

# Check for CSV file argument
if len(sys.argv) < 2:
    print("Usage: python script.py <csv_file>")
    sys.exit(1)

input_file = sys.argv[1]

# Check if file exists in the same directory as the script
if not os.path.isfile(input_file):
    print(f"File '{input_file}' not found in the current directory.")
    sys.exit(1)

# Load the CSV file
tickers_df = pd.read_csv(input_file)

# Ensure there is a 'Ticker' column
if 'Ticker' not in tickers_df.columns:
    raise ValueError("The CSV file must have a 'Ticker' column")

# Define a function to fetch stock data
def fetch_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        
        # Fetch relevant details
        info = stock.info
        name = info.get('shortName', 'N/A')
        
        # Last close price
        history = stock.history(period="1d")
        last_close_price = round(history['Close'][-1], 3) if not history.empty else 'N/A'
        
        # Upcoming dividends from 'calendar'
        calendar = stock.calendar
        if calendar and 'Ex-Dividend Date' in calendar:
            upcoming_dividend_date = calendar['Ex-Dividend Date']
            upcoming_dividend = info.get('dividendRate', 'N/A')  # Extract dividend amount if available
        else:
            upcoming_dividend = 'N/A'
            upcoming_dividend_date = 'N/A'
        
        return {
            'Name': name,
            'Ticker': ticker,
            'Last Close Price': last_close_price,
            'Upcoming Dividend Amount': round(upcoming_dividend, 3) if isinstance(upcoming_dividend, (int, float)) else upcoming_dividend,
            'Upcoming Dividend Date': upcoming_dividend_date
        }
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return {
            'Name': 'Error',
            'Ticker': ticker,
            'Last Close Price': 'Error',
            'Upcoming Dividend Amount': 'Error',
            'Upcoming Dividend Date': 'Error'
        }

# Fetch data for all tickers
results = [fetch_stock_data(ticker) for ticker in tickers_df['Ticker']]

# Create a DataFrame and save to CSV
output_df = pd.DataFrame(results)
output_file = 'stock_dividend_info.csv'
output_df.to_csv(output_file, index=False)

print(f"Data saved to '{output_file}'")
