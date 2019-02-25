import fix_yahoo_finance as fyf

import pandas as pd

import pandas_datareader as pdr

import matplotlib.pyplot as plt

fyf.pdr.override()

df= pdr.data.get_data_yahoo('aapl', start='2018-01-01', end='2019-01-25')

df.loc['2017-01-01':'2019-01-25',['Open', 'Close']].plot(figsize=(16,9))

plt.xlabel('Date')

plt.ylabel('Price')

plt.title('AAPL\n Source:Yahoo Finance')

plt.legend()

plt.grid(True)

plt.show()
