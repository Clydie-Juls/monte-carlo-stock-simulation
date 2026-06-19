import sys
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
import yfinance as yf

ticker_symbol = sys.argv[1]
interval = sys.argv[2]

stock_folder = Path("stocks")
stock_folder.mkdir(parents=True, exist_ok=True)

endTime = datetime.now().date()
startTime = (datetime.now() - timedelta(days=365)).date()
aapl = yf.download(ticker_symbol, start=startTime, end=endTime, interval=interval)

if isinstance(aapl.columns, pd.MultiIndex):
    aapl.columns = aapl.columns.get_level_values(0)

aapl_new = aapl[["High", "Low", "Close", "Open"]]
aapl_new.to_json(f"stocks/{ticker_symbol}.json", orient="index")
