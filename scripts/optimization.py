# scripts/optimization.py
import numpy as np
from scipy.optimize import minimize

def portfolio_variance(weights, cov_matrix):
    """
    Calculate the portfolio variance given weights and covariance matrix.
    """
    return np.dot(weights.T, np.dot(cov_matrix, weights))

def optimize_portfolio(mean_returns, cov_matrix, target_return):
    """
    Optimize portfolio weights to minimize variance for a given target return.
    """
    num_assets = len(mean_returns)
    initial_weights = np.ones(num_assets) / num_assets
    bounds = [(0, 1) for _ in range(num_assets)]
    constraints = [
        {"type": "eq", "fun": lambda weights: np.sum(weights) - 1},  # Weights sum to 1
        {"type": "eq", "fun": lambda weights: np.dot(weights, mean_returns) - target_return},  # Target return
    ]
    result = minimize(
        portfolio_variance,
        initial_weights,
        args=(cov_matrix,),
        method="SLSQP",
        bounds=bounds,
        constraints=constraints
    )
    print("Mean Returns:\n", mean_returns)
    print("Covariance Matrix:\n", cov_matrix)
    print("Target Return:", target_return)
    return result.x
