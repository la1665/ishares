import requests
import pandas as pd
import json

from fetch_data import IShareUrlList



class IShareData():
    def __init__(self):
        self.urls = []
        self.cols = []

    def fetch_data(self):
        self.ishares = IShareUrlList()
        self.urls = self.ishares.create_urls()

        return self.urls

    def col_names(self, url):
        """as in json file only contains data and not its relative column name this function get them from page source."""
        cols = self.ishares.create_columns(url)
        return cols

    def save_data(self):
        """send a request to esch endpoint and save each relative response data in different csv files."""

        self.fetch_data()
        for url in range(len(self.urls)):
            result = []
            req = requests.get(self.urls[url])
            responses = json.loads(req.content).get('aaData')
            for res in responses:
                result.append([r.get('raw') if isinstance(r, dict) else r for r in res])
        
            print(url)
            df = pd.DataFrame(result, columns=self.col_names(self.urls[url]))
            df.to_csv('result_{}.csv'.format(url), encoding='utf-8', index=False)


if __name__ == '__main__':
    result_csv = IShareData()
    result_csv.save_data()


