import yfinance as yf
import pandas as pd
import os

def fetch_uso_options(save_path="data/uso_options_data.csv", num_expirations=2):
    """
    Fetches option chain data for the USO ETF (U.S. Oil Fund) and saves it as a CSV.

    Parameters:
    save_path : str
        File path to save the CSV
    num_expirations : int
        Number of upcoming expiration dates to fetch
    """
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    ticker = yf.Ticker("USO")
    expirations = ticker.options[:num_expirations]

    all_calls = []
    for expiry in expirations:
        calls = ticker.option_chain(expiry).calls
        calls["expirationDate"] = expiry
        all_calls.append(calls)

    combined_df = pd.concat(all_calls, ignore_index=True)
    combined_df.to_csv(save_path, index=False)
    print(f"USO options data saved to {save_path}")

if __name__ == "__main__":
    fetch_uso_options()
