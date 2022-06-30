import requests
import pandas as pd
import json
import random
import yfinance as yf

from endpoints import IShareUrlList
from serializer import Serializer


class CreateDataFrame:
    def __init__(self):
        self.urls = IShareUrlList()
        self.cols = Serializer()
        self.df = pd.DataFrame()
        self.dfs = []
        self.tickers_ohlc = []
    
    def save_data(self):
        """send a request to esch endpoint and save each relative response data dataframe."""
        urls = self.urls.create_endpinots()
        for url in urls:
            results = []
            cols = self.cols.columns_serializer(url)
            req = requests.get(url)
            response = json.loads(req.content).get('aaData')

            for res in response:
                results.append([r.get('raw') if isinstance(r, dict) else r for r in res])
            
            print(urls.index(url))
            df = pd.DataFrame(results, columns=cols)
            df = df[df['ticker'].map(lambda x: str(x)!="-")]
            self.dfs.append(df)
        return self.dfs

    def concat_dfs(self):
        """Concat all dataframes"""
        self.save_data()
        self.df = pd.concat(self.dfs, ignore_index=True)
        return self.df

    def ticker_ohlc(self, num: int=500):
        df = self.df
        data_list = []

        for ticker in range(len(df)):
            data_list.append(df['ticker'][ticker])

        random_ticker_list = random.sample(data_list, num)

        for ticker in random_ticker_list:
            data =  yf.download(ticker, period='1mo')
            if not data.empty:
                data = pd.DataFrame(data)
                self.tickers_ohlc.append(data)
            else: 
                print('no data')
        
        return self.tickers_ohlc, random_ticker_list


