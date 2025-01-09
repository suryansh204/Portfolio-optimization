# portfolio_optimization.py

import numpy as np
from scripts.data_collection import fetch_and_process_data
from scripts.optimization import optimize_portfolio
from scripts.visualization import plot_two_asset_frontier

if __name__ == "__main__":
    
    target_return = 0.0051 
    data, daily_returns, mean_returns, cov_matrix = fetch_and_process_data()

    #  Model
    optimal_weights = optimize_portfolio(mean_returns, cov_matrix, target_return)

    # Visualization 
    plot_two_asset_frontier(mean_returns, cov_matrix,
                        asset_names=["Coca-Cola", "NVIDIA"],
                        target_return=0.0002)

    print(f"Optimal Weights: {optimal_weights}")

#  mean_returns = np.array([0.0012, 0.0010])  # Apple and Microsoft average returns
#  cov_matrix = np.array([
#         [0.0004, 0.0002],  # Variance and covariance for Apple
#         [0.0002, 0.0003]   # Variance and covariance for Microsoft
#     ])
#  target_return = 0.00109  # Target portfolio return

#     # Run Optimization
#  optimal_weights = optimize_portfolio(mean_returns, cov_matrix, target_return)
#  print(f"Optimal Portfolio Weights: {optimal_weights}")