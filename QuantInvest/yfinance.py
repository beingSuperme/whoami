# get_data.py
import yfinance as yf
import pandas as pd

# 下载历史数据
data = yf.download('AAPL', start='2023-01-01', end='2024-01-01') # 日线
print(data.head())

# 保存到CSV (或SQLite数据库)
data.to_csv('AAPL_2023.csv')

# 获取最新实时价格 (简化)
ticker = yf.Ticker('AAPL')
current_price = ticker.history(period='1d')['Close'][0] # 获取最近一个交易日的收盘价
print(f"AAPL最新价格: ${current_price:.2f}")



