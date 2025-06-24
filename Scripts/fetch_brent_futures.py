import yfinance as yf
import pandas as pd
import os

def fetch_brent_futures(save_path="C:/Users/adity/OneDrive/Documents/GitHub/Multi-Model-Option-Pricing/data/brent_options_data.csv", num_expirations=2):
    ticker_symbol = "CL=F"  # Brent Crude Futures

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    print(f"Fetching Brent futures data from Yahoo Finance for symbol: {ticker_symbol}")
    brent = yf.Ticker(ticker_symbol)

    try:
        expirations = brent.options[:num_expirations]
    except Exception as e:
        print("Error fetching expirations:", e)
        return

    if not expirations:
        print("No expirations available. Check the symbol or internet connection.")
        return

    print("Available expirations:", expirations)

    all_calls = []

    for expiry in expirations:
        try:
            opt = brent.option_chain(expiry)
            calls = opt.calls
            calls['expirationDate'] = expiry
            all_calls.append(calls)
            print(f"Fetched {len(calls)} rows for expiry {expiry}")
        except Exception as e:
            print(f"Failed to fetch data for {expiry}: {e}")

    if not all_calls:
        print("No option chain data fetched. Exiting.")
        return

    # Combine and save
    combined_df = pd.concat(all_calls, ignore_index=True)
    combined_df.to_csv(save_path, index=False)
    print(f"Saved {len(combined_df)} rows to {save_path}")

if __name__ == "__main__":
    fetch_brent_futures()
