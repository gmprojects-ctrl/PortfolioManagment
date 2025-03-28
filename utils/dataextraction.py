# Imports
import pandas as pd
import numpy as np
import yfinance as yf




def yf_data_scraper_function(ticker: str,interval_:str = "1d", start:str = None, end:str = None, auto_adjust_=True):
    '''
    Title: yf_data_scraper_function
    Description: Function to scrape yfinance data
    Input:
        ticker: str 
        interval_: str
        start: str
        end: str
        auto_adjust_: bool
    Output:
        data: pd.DataFrame
    '''
    
    # Check if start date exists    
    if start is not None:
        start_date = start
    else:
        start_date = (pd.to_datetime("today") - pd.DateOffset(years=1)).strftime("%Y-%m-%d")
    
    # Check if end date exists
    if end is not None:
        end_date = end
    else:
        end_date = pd.to_datetime("today").strftime("%Y-%m-%d")
        
    # Get the ticker
    data = yf.download(ticker,start=start_date,end=end_date,auto_adjust=auto_adjust_,interval=interval_)
    
    # Return the data
    return data   