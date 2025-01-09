import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

def plot_two_asset_frontier(mean_returns, cov_matrix, asset_names=None, target_return = None):
    """
    Plot the efficient frontier for two assets using a simple parametric approach:
    w in [0,1] for Asset 1, (1-w) for Asset 2.
    
    mean_returns: length-2 array-like of mean returns [mu1, mu2]
    cov_matrix:   2x2 covariance matrix
    asset_names:  optional list/tuple of the names of these two assets
    """
    mu1 = mean_returns.iloc[0]
    mu2 = mean_returns.iloc[1]
    
    var1  = cov_matrix.iloc[0, 0]
    var2  = cov_matrix.iloc[1, 1]
    cov12 = cov_matrix.iloc[0, 1]

    # Create a grid of w from 0 to 1
    weights = np.linspace(0, 1, 100)
    
    portfolio_returns = []
    portfolio_risks = []
    
    for w in weights:
        # Parametric formulas for return & variance
        ret = w*mu1 + (1-w)*mu2
        var = (w**2 * var1) + ((1-w)**2 * var2) + (2*w*(1-w)*cov12)
        sd  = np.sqrt(var)
        
        portfolio_returns.append(ret)
        portfolio_risks.append(sd)

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(portfolio_risks, portfolio_returns, label="2-Asset Frontier", color="blue")

   
    plt.scatter(np.sqrt(var1), mu1, color="red", 
                label=asset_names[0] if asset_names else "Asset 1")
    plt.scatter(np.sqrt(var2), mu2, color="green", 
                label=asset_names[1] if asset_names else "Asset 2")

    plt.xlabel("Volatility (Risk)")
    plt.ylabel("Expected Return")
    plt.title("Two-Asset Efficient Frontier (No Short Selling)")
    plt.grid(True)
    plt.legend()
    plt.show()