# Data Source: Yahoo Finance API (https://finance.yahoo.com)
# Retrieved on: March 20, 2025

import yfinance as yf
import pandas as pd
import os

# path to csv-data folder
csv_folder = "/Users/irajakbar/Desktop/ENSF444/stock-market-index/csv-data"

# sector etfs
sector_etfs = {
    "Information Technology": "XLK",
    "Health Care": "XLV",
    "Financials": "XLF",
    "Consumer Discretionary": "XLY",
    "Communication Services": "XLC",
    "Industrials": "XLI",
    "Consumer Staples": "XLP",
    "Energy": "XLE",
    "Materials": "XLB",
    "Real Estate": "XLRE",
    "Utilities": "XLU"
}

# date range
start_date = "2015-01-01"
end_date = "2025-01-01"

# to download and save data for each sector ETF
for sector, ticker in sector_etfs.items():
    print(f"Downloading data for {sector} ({ticker})...")
    
    # historical data
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # create path for csv file
    filename = os.path.join(csv_folder, f"{ticker}_historical_data.csv")
    
    # save as csv
    data.to_csv(filename)
    
    print(f"Saved: {filename}")

print("All sector data downloaded successfully!") 