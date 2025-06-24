import numpy as np

def binomial_tree(S, K, T, r, sigma, option_type="call", steps=100):
    """
    Binomial Tree model for European option pricing.

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
    steps : int
        Number of steps in the binomial tree

    Returns:
    float
        Theoretical option price
    """
    dt = T / steps
    u = np.exp(sigma * np.sqrt(dt))       # Up factor
    d = 1 / u                              # Down factor
    p = (np.exp(r * dt) - d) / (u - d)     # Risk-neutral probability

    # Initialize asset prices at maturity
    ST = np.array([S * (u ** j) * (d ** (steps - j)) for j in range(steps + 1)])

    # Initialize option values at maturity
    if option_type == "call":
        option_values = np.maximum(0, ST - K)
    else:
        option_values = np.maximum(0, K - ST)

    # Step backwards through the tree
    for i in range(steps - 1, -1, -1):
        option_values = np.exp(-r * dt) * (p * option_values[1:] + (1 - p) * option_values[:-1])

    return option_values[0]
