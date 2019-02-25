# PythonInFourSteps
Quick Start Guide To Introduce Python

Step 1

Download and install Python (https://www.python.org/downloads/) NOTE: If you are using a Mac, chances are Python is installed and you can skip to step#2

Step 2

Run Python IDLE and install matplotlib, pandas and yahoo finance fix

pip install matplotlib
pip install pandas
pip install fix_yahoo_finance

Step 3 (Optional)

Download and install Microsoft Visual Studio Code (https://code.visualstudio.com/download). I really enjoy using this IDE. It seem to have massive potential and if you like it too, let me know.

Step 4

Copy and paste or type the code below on the right into your editor, save and run it.

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
