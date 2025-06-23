# Multi-Model Option Pricing: Oil Price Volatility by Country

This project applies three classical option pricing models — Black-Scholes, Binomial Tree, and Monte Carlo Simulation — to real-world oil markets. In light of increasing geopolitical instability (for example, Qatar airspace closures and Iran–US tensions), we examine how options on oil ETFs and futures reflect risk and volatility in oil prices by country.

## Real-World Motivation
Global oil pricing is increasingly volatile, from strikes on key oil-exporting countries to OPEC decisions. Options are a key tool to quantify that uncertainty. This project explores:
- How well standard models price oil options
- How implied volatility shifts during geopolitical events
- Country-level risk exposure through regional ETFs

## Models Implemented
1. Black-Scholes Model
- Used for pricing European oil options on ETFs like USO (U.S.), QAT (Qatar), and KSA (Saudi Arabia)

2. Binomial Tree Model
- Dynamic pricing using discrete time steps, useful for visualizing compounding volatility during events

3. Monte Carlo Simulation
- Simulates future oil price paths under various scenarios such as war, production cuts, and embargoes

## Project Structure
```
multi-model-option-pricing/
├── data/
│   └── uso_options_data.csv         
  USO: United States Oil Fund (U.S. crude proxy)
│   └── qat_etf_data.csv             
  QAT: Qatar ETF
│   └── ksa_etf_data.csv             
  KSA: Saudi Arabia ETF
├── notebooks/
│   └── Oil_Option_Pricing_Comparison.ipynb
├── src/
│   ├── black_scholes.py
│   ├── binomial_tree.py
│   └── monte_carlo.py
├── plots/                           
  Volatility surfaces and pricing error plots
├── README.md
└── requirements.txt
```

## Key Analysis
- Comparison of theoretical option prices with actual market prices
- Volatility surface construction for oil ETFs
- Sensitivity of model prices to strike, maturity, and volatility inputs
- Cross-regional volatility behaviour (Middle East, U.S., Global)

## Skills Demonstrated
- Quantitative finance with energy market context
- Modelling volatility shocks from geopolitical events
- Application of pricing models for risk analysis
- Real-world data collection and backtesting

## Coming Next
- Black-Scholes pricing applied to USO ETF
- Monte Carlo simulations for crisis-driven volatility
- Comparison of implied versus realised volatility by country


Aditya Kanth Manne
