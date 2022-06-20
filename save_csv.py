import requests
import pandas as pd
import json
import concurrent.futures

from fetch_data import IShareUrlList



class IShareData():
    def __init__(self):
        self.urls = []
        self.dfs = []

    def fetch_data(self):
        self.ishares = IShareUrlList()
        self.urls = self.ishares.create_urls()
        return self.urls
    
    def col_names(self, url):
        """as in json file only contains data and not its relative column name this function get them from page source."""
        cols = self.ishares.create_columns(url)
        cols = ['Ticker' if cols[i]=='Issuer Ticker' else cols[i] for i in range(len(cols))]
        cols = ['Currency' if cols[i]=='Market Currency' else cols[i] for i in range(len(cols))]
        return cols

    def save_data(self):
        """send a request to esch endpoint and save each relative response data in different csv files."""
        self.fetch_data()
        for url in range(len(self.urls)):
            results = []
            req = requests.get(self.urls[url])
            response = json.loads(req.content).get('aaData')

            for res in response:
                results.append([r.get('raw') if isinstance(r, dict) else r for r in res])
            print(url)
            df = pd.DataFrame(results, columns=self.col_names(self.urls[url]))
            self.dfs.append(df)
        return self.dfs
        
    
    def save_csv(self):
        self.save_data()
        df = pd.concat(self.dfs)
        df.to_csv('results.csv', encoding='utf-8', index=False)

if __name__ == '__main__':
    result_csv = IShareData()
    result_csv.save_csv()


