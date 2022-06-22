import requests
import pandas as pd
import json

from endpoints import IShareUrlList
from serializer import Serializer


class CreateDataFrame:
    def __init__(self):
        self.urls = IShareUrlList()
        self.cols = Serializer()
        self.dfs = []
    
    def save_data(self):
        """send a request to esch endpoint and save each relative response data dataframe."""
        urls = self.urls.create_endpinots()
        for url in range(len(urls[:2])):
            results = []
            cols = self.cols.columns_serializer(urls[url])
            req = requests.get(urls[url])
            response = json.loads(req.content).get('aaData')

            for res in response:
                results.append([r.get('raw') if isinstance(r, dict) else r for r in res])
            
            print(url)
            df = pd.DataFrame(results, columns=cols)
            self.dfs.append(df)
        return self.dfs

    def concat_dfs(self):
        """Concat all dataframes"""
        self.save_data()
        df = pd.concat(self.dfs)
        return df


