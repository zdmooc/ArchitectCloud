import pandas as pd
import numpy
import matplotlib.pyplot as plt
import cufflinks as cf
import yfinance as yf

start = "2010-01-01"
end = "2020-12-31"

symbol = "MSFT"

df = yf.download(tickers = symbol, start = start, end = end)
df
df.info()

symbol = ["MSFT", "GE", "AAPL"]

df = yf.download(tickers = symbol, start = start, end = end)
df


df = pd.read_csv("stocks.csv", header = [0, 1], index_col = 0, parse_dates = [0])
df

df.info()

df.Close.GE

df.Close.GE.plot(figsize = (12, 8))
plt.show()