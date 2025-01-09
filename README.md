# Portfolio Optimization Model

## Project Description
This project showcases the implementation of a Portfolio Optimization Model in Python, built around the principles of Modern Portfolio Theory. The model computes optimal portfolio weights for a two-asset portfolio, aiming to minimize risk for a given target return. Additionally, the project includes an optional feature to visualize the Efficient Frontier, which illustrates the trade-off between portfolio risk and return.

### Key Features
1. **Optimal Portfolio Weights Calculation**: Determines the weights for a two-asset portfolio that minimize portfolio variance under specific constraints.
2. **Efficient Frontier Visualization**: Demonstrates the trade-off between risk and return for different portfolio combinations.
   
### Future Plans
To enhance and expand this project, the following improvements are planned:

1. **Multi-Asset Portfolios**
   - Extend the model to handle portfolios with more than two assets.
   - Actionable Step: Update the covariance matrix and optimization logic to accommodate additional assets.

2. **Dynamic Data Updates**
   - Add real-time data fetching to make the model adaptive to current market conditions.
   - Actionable Step: Integrate APIs that provide live financial data.

3. **Sharpe Ratio Optimization**
   - Incorporate risk-adjusted performance metrics, such as the Sharpe ratio, into the optimization process.
   - Actionable Step: Modify the objective function to maximize the Sharpe ratio instead of minimizing variance.

4. **Interactive Visualizations**
   - Use libraries like Plotly or Dash to create interactive plots for the Efficient Frontier.
   - Actionable Step: Develop a web-based or notebook-integrated visualization module.

### How It Works
1. **Data Collection**: Fetches historical price data for two assets, calculates daily/weekly returns, and computes the covariance matrix.
2. **Mathematical Modeling**: Defines the optimization problem to minimize variance for a given target return with constraints.
3. **Optimization**: Uses `scipy.optimize` to solve for optimal portfolio weights.
4. **Visualization**: plots the Efficient Frontier to showcase portfolio risk-return trade-offs.

### Requirements
To run this project, you will need:
- Python 3.8+
- Libraries: `yfinance`, `numpy`, `pandas`, `scipy`, `matplotlib`

### Visualization

The Efficient Frontier represents the optimal portfolios that offer the highest expected return for a given level of risk.

#### Example: Two-Asset Portfolio (No Short Selling)
Below is the Efficient Frontier for a two-asset portfolio containing Coca-Cola and NVIDIA stocks:

![Efficient Frontier](path-to-image/efficient_frontier.png)

- **Blue Curve**: Shows the tradeoff between risk (volatility) and return for different portfolios.
- **Red Point**: Represents the optimal portfolio for Coca-Cola.
- **Green Point**: Represents the optimal portfolio for NVIDIA.



### Usage
1. Edit the asset tickers and date range in the script to specify your portfolio.
2. Run the script to calculate optimal weights and optionally visualize the Efficient Frontier.
3. Outputs include:
   - Optimal portfolio weights.
   - Portfolio variance and return values.
   - Efficient Frontier plot (if enabled).


### Acknowledgments
- Modern Portfolio Theory concepts by Harry Markowitz.
- Python libraries `yfinance`, `numpy`, `scipy`, and `matplotlib` for enabling seamless financial analysis.
