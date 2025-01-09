# scripts/data_collection.py

import yfinance as yf
import pandas as pd
import os

def fetch_and_process_data():
    # Asset tickers and date range
    assets = ["KO", "COST"]
    start_date = "2020-01-01"
    end_date = "2023-01-01"

    # Fetch historical data
    data = yf.download(assets, start=start_date, end=end_date)
    #couldnt access [ADJ close]
    #because 
    data.columns = ['_'.join(col).strip() for col in data.columns.values]
    print(data.head())
    
    close_prices = data.filter(like='Close_')

    # Calculate daily returns
    daily_returns = close_prices.pct_change().dropna()

    # Calculate mean returns and covariance matrix
    mean_returns = daily_returns.mean()
    cov_matrix = daily_returns.cov()
    if not os.path.exists("data"):
     os.makedirs("data")
    
    close_prices.to_csv("data/close_prices.csv")
    daily_returns.to_csv("data/daily_returns.csv")

    return close_prices, daily_returns, mean_returns, cov_matrix
