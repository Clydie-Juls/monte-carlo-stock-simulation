from concurrent import futures
from datetime import datetime, timedelta

import pandas as pd
import yfinance as yf

import grpc
from src.python.grpc import stock_history_pb2
from src.python.grpc import stock_history_pb2_grpc

BATCH_SIZE = 256

class HistoricalStockDataGRPCServer(stock_history_pb2_grpc.StockHistoryServiceServicer):
    def RequestStockHistoryData(self, request, context):
        ticker = request.ticker
        interval = request.interval

        stock_df = getHistoricalStockData(ticker, interval);
        if stock_df is None:
            return

        batch = []
        for timestamp, rows in stock_df.iterrows():
            close = rows["Close"]
            if hasattr(rows, "item"):
                close = float(close.item())

            batch.append(stock_history_pb2.StockHistory(
                timestamp=str(timestamp),
                stock_info= stock_history_pb2.StockInfo(
                    close= close if isinstance(close, float) else 0
                )
            ))

            if len(batch) == BATCH_SIZE:
                yield stock_history_pb2.StockHistoryResponse(
                    batch
                )
                batch = []

        if batch:
            yield stock_history_pb2.StockHistoryResponse(
                batch
            )

def getHistoricalStockData(ticker_symbol, interval):
    endTime = datetime.now().date()
    startTime = (datetime.now() - timedelta(days=365)).date()
    stock = yf.download(ticker_symbol, start=startTime, end=endTime, interval=interval)

    if stock is None:
        return

    if isinstance(stock.columns, pd.MultiIndex):
        stock.columns = stock.columns.get_level_values(0)

    aapl_new = stock[["Close"]]
    return aapl_new;

def runGRPCSever(): 
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stock_history_pb2_grpc.add_StockHistoryServiceServicer_to_server(
        HistoricalStockDataGRPCServer,
        server
    )
    server.add_insecure_port("[::]:8082")
    server.start()
    print("GRPC server starting at 8082")
    server.wait_for_termination()



def main():
    runGRPCSever()

if __name__ == "__main__":
    main()

