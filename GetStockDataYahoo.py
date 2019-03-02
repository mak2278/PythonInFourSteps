import pandas as pd 
import pandas_datareader as dr 
import matplotlib.pyplot as plt

df= dr.data.get_data_yahoo('aapl', start='2018-01-01', end='2019-01-25')
df.loc['2017-01-01':'2019-01-25',['Open', 'Close']].plot(figsize=(16,9))
#df['Close'].pct_change().plot(figsize=(16,9))

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('AAPL Open & Close \n Data Source:Yahoo Finance')
plt.legend()

plt.grid(True)
plt.show()
