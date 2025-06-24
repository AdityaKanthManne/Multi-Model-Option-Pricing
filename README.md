
# Multi-Model Option Pricing: Oil Price Volatility by Country

This project applies three classical option pricing models — Black-Scholes, Binomial Tree, and Monte Carlo Simulation — to real-world oil markets. In light of increasing geopolitical instability (for example, Qatar airspace closures and Iran–US tensions), we examine how options on oil ETFs and futures reflect risk and volatility in oil prices by country.

## Real-World Motivation
From strikes on key oil-exporting countries to OPEC decisions, global oil pricing is increasingly volatile. Options are a key tool to quantify that uncertainty. This project explores:
- How well standard models price oil options
- How implied volatility shifts during geopolitical events
- Country-level risk exposure through regional ETFs

## Models Implemented
1. Black-Scholes Model
Used for pricing European oil options on ETFs like USO (U.S.), QAT (Qatar), and KSA (Saudi Arabia)

2. Binomial Tree Model
Dynamic pricing using discrete time steps, useful for visualizing compounding volatility during events

3. Monte Carlo Simulation
Simulates future oil price paths under various scenarios such as war, production cuts, and embargoes

## Project Structure
```
multi-model-option-pricing/
├── data/
│   └── uso_options_data.csv         # USO: United States Oil Fund (U.S. crude proxy)
│   └── qat_etf_data.csv             # QAT: Qatar ETF
│   └── ksa_etf_data.csv             # KSA: Saudi Arabia ETF
├── notebooks/
│   └── Oil_Option_Pricing_Comparison.ipynb
├── src/
│   ├── black_scholes.py
│   ├── binomial_tree.py
│   └── monte_carlo.py
├── scripts/
│   ├── fetch_uso_options.py
│   └── fetch_etf_options_qat_ksa.py
├── plots/                           # Volatility surfaces and pricing error plots
├── README.md
└── requirements.txt
```

## Key Analysis
- Comparison of theoretical option prices with actual market prices
- Volatility surface construction for oil ETFs
- Sensitivity of model prices to strike, maturity, and volatility inputs
- Cross-regional volatility behavior (Middle East, U.S., Global)

## Requirements
```
yfinance
pandas
numpy
scipy
matplotlib
```

## Scripts
- `fetch_uso_options.py`: Downloads the latest USO options data from Yahoo Finance
- `fetch_etf_options_qat_ksa.py`: Fetches options data for QAT and KSA ETFs

## Notebooks
- `Oil_Option_Pricing_Comparison.ipynb`: Runs Black-Scholes model on USO options and visualizes:
  - Market vs. Model price differences
  - Sensitivity to volatility and time to expiry
  - Error analysis by strike and maturity

## Skills Demonstrated
- Quantitative finance with energy market context
- Modeling volatility shocks from geopolitical events
- Application of pricing models for risk analysis
- Real-world data collection and backtesting

## Coming Next
- Binomial Tree and Monte Carlo implementations
- Regional option volatility comparison: QAT vs. USO vs. KSA
- Interactive Streamlit dashboard for pricing inputs

## Author
Aditya Kanth Manne
