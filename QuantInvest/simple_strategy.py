# simple_strategy.py (回测版)
import pandas as pd
import matplotlib.pyplot as plt

# 从文件加载数据
data = pd.read_csv('AAPL_2023.csv', index_col='Date', parse_dates=True)
data = data.sort_index() # 确保按时间排序

# 计算指标 - 短期(5天)和长期(60天)移动均线
data['SMA5'] = data['Close'].rolling(window=5).mean()
data['SMA60'] = data['Close'].rolling(window=60).mean()

# 生成信号：短期均线上穿长期均线 -> 买入信号(1)；下穿 -> 卖出信号(-1)；其余为0(持有/空仓)
data['Signal'] = 0
data['Signal'][data['SMA5'] > data['SMA60']] = 1 # 金叉
data['Signal'][data['SMA5'] < data['SMA60']] = -1 # 死叉

# 简单计算策略收益 (次日开盘买入/卖出)
data['Position'] = data['Signal'].shift(1) # 信号滞后一期，避免使用未来数据
data['Daily_Return'] = data['Close'].pct_change()
data['Strategy_Return'] = data['Position'] * data['Daily_Return']

# 计算累计收益
data['Cumulative_Market'] = (1 + data['Daily_Return']).cumprod()
data['Cumulative_Strategy'] = (1 + data['Strategy_Return']).cumprod()

# 可视化结果
data[['Cumulative_Market', 'Cumulative_Strategy']].plot(figsize=(10, 6), title='策略 vs 市场表现')
plt.xlabel('日期')
plt.ylabel('累计收益')
plt.savefig('backtest_result.png') # 保存图表
plt.show()



