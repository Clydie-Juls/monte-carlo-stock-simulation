from datetime import datetime, timedelta

import pandas as pd
import yfinance as yf

from generated import stock_pb2

def getHistoricalStockData(ticker_symbol, interval):
    endTime = datetime.now().date()
    startTime = (datetime.now() - timedelta(days=365)).date()
    stock = yf.download(ticker_symbol, start=startTime, end=endTime, interval=interval)

    if stock is None:
        return

    if isinstance(stock.columns, pd.MultiIndex):
        stock.columns = stock.columns.get_level_values(0)

    aapl_new = stock[["High", "Low", "Close", "Open"]]
    return aapl_new;
