import numpy as np
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type="call"):
    """
    Black-Scholes option pricing formula for European options.

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
        Volatility of underlying (standard deviation)
    option_type : str
        'call' or 'put'

    Returns:
    float
        Theoretical price of the option
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")
