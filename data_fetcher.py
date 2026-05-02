import akshare as ak
import pandas as pd

def fetch_historical_data(stock_code, start_date, end_date):
    # Fetch historical stock data using Akshare
    stock_data = ak.stock_zh_a_daily(symbol=stock_code, adjust="qfq")
    stock_data = stock_data[(stock_data.index >= start_date) & (stock_data.index <= end_date)]
    return stock_data

if __name__ == "__main__":
    start_date = "2003-01-01"
    end_date = "2026-12-31"
    
    # Fetching data for Kweichow Moutai
    moutai_data = fetch_historical_data("600519", start_date, end_date)
    print("Kweichow Moutai Historical Data:")
    print(moutai_data)
    
    # Fetching data for Wuliangye
    wuliangye_data = fetch_historical_data("000858", start_date, end_date)
    print("Wuliangye Historical Data:")
    print(wuliangye_data)