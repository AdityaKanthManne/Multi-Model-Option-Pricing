import numpy as np

def monte_carlo(S, K, T, r, sigma, option_type="call", simulations=10000):
    """
    Monte Carlo simulation for European option pricing.

    Parameters:
    S : float
        Current stock (underlying) price
    K : float
        Option strike price
    T : float
        Time to expiration in years
    r : float
        Annualized risk-free interest rate
    sigma : float
        Volatility of the underlying
    option_type : str
        'call' or 'put'
    simulations : int
        Number of simulated price paths

    Returns:
    float
        Estimated option price
    """
    Z = np.random.standard_normal(simulations)
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

    if option_type == "call":
        payoff = np.maximum(ST - K, 0)
    elif option_type == "put":
        payoff = np.maximum(K - ST, 0)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return np.exp(-r * T) * np.mean(payoff)
