import numpy as np
from portfolio_optimization import optimize_portfolio  # Adjust the import path if needed
from colorama import Fore, Style

def test_optimize_portfolio():
    # Define mean returns for assets
    mean_returns = np.array([0.0012, 0.0010])  

    # Define covariance matrix
    cov_matrix = np.array([
        [0.0004, 0.0002],  
        [0.0002, 0.0003]  
    ])


    target_return = 0.00109  # Target portfolio return


    expected_weights = np.array([0.45, 0.55])  

    try:
      
        optimal_weights = optimize_portfolio(mean_returns, cov_matrix, target_return)

       
        if np.allclose(optimal_weights, expected_weights, atol=1e-2):
            print(f"{Fore.GREEN}Test Passed: Optimal Portfolio Weights: {optimal_weights}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Test Failed: Optimal Portfolio Weights: {optimal_weights}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Test Failed: Optimization raised an error: {e}{Style.RESET_ALL}")

# Run the test
if __name__ == "__main__":
    test_optimize_portfolio()
