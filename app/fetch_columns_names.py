import requests
from bs4 import BeautifulSoup

from endpoints import IShareUrlList


class ColumnsNames:
    def __init__(self):
        self.urls_list = IShareUrlList()
        self.columns = []
    
    def create_columns(self, url):
        """as in json file only contains data and not its relative column name this function get them from page source."""
        columns = []
        url = url.split('.ajax')[0]
        r = requests.get(url)
        html_contents = r.text
        html_soup = BeautifulSoup(html_contents, 'html.parser')
        script = html_soup.find(id="tabsAll")
        table = script.find('table')
        for col in table.find('tr').find_all('th'):
            columns.append(col.text.strip())
        
        return columns



