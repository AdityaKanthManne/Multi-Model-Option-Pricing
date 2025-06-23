# Multi-Model Option Pricing: Oil Price Volatility by Country

This project applies three classical option pricing models — **Black-Scholes**, **Binomial Tree**, and **Monte Carlo Simulation** — to real-world oil markets. In light of increasing geopolitical instability (e.g., Qatar airspace closures, Iran–US tensions), we examine how options on **oil ETFs and futures** reflect risk and volatility in oil prices by country.

## Real-World Motivation
From strikes on key oil-exporting countries to OPEC decisions, global oil pricing is increasingly volatile. Options are a key tool to quantify that uncertainty. Here, we test:
- How well standard models price oil options
- How implied volatility shifts during geopolitical events
- Country-level risk exposure through regional ETFs

## Models Implemented
### 1. **Black-Scholes Model**
- For pricing European oil options on ETFs like $USO (U.S.), $QAT (Qatar), $KSA (Saudi Arabia).

### 2. **Binomial Tree Model**
- Dynamic pricing with steps — useful for understanding the compounding effect of daily volatility (e.g., mid-crisis news cycles).

### 3. **Monte Carlo Simulation**
- Simulate paths of oil price futures under war, production cut, or embargo scenarios.


## Project Structure

multi-model-option-pricing/
├── data/
│   └── uso_options_data.csv         # USO: United States Oil Fund (proxy for U.S. crude)
│   └── qat_etf_data.csv             # QAT: Qatar ETF (risk exposure proxy)
│   └── ksa_etf_data.csv             # KSA: Saudi Arabia ETF
├── notebooks/
│   └── Oil_Option_Pricing_Comparison.ipynb
├── src/
│   ├── black_scholes.py
│   ├── binomial_tree.py
│   └── monte_carlo.py
├── plots/                           # Vol surface, error plots
├── README.md
└── requirements.txt




## Key Analysis
- Theoretical option prices vs. market prices
- Volatility surface for oil ETFs
- Sensitivity to strike price, time to maturity, and volatility
- Region-wise volatility behaviour (Middle East vs. U.S. vs. global)



## Skills Demonstrated
- Quantitative finance + energy market integration
- Modelling volatility shocks due to political/military events
- Geopolitical risk analysis using pricing models
- Real data acquisition and backtesting


## Coming Next
- Black-Scholes notebook on USO ETF options
- Monte Carlo simulation on oil price crashes/spikes
- Implied vs realised volatility plots by country




Aditya Kanth Manne
