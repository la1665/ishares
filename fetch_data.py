
import requests
from bs4 import BeautifulSoup

from urls import ISHARES_HOLDINGS as ishares, JSON_QUERY as query


class IShareUrlList():
    """read data from urls.py and create each endpoint to request to."""
    def __init__(self):
        self.ishare_list = ishares
        self.urls_list = []
    
    def create_urls(self):
        """modify urls list and change it from csv format to json."""
        for ishare in self.ishare_list:
            url = (ishare[0].split('?')[0] + query)
            self.urls_list.append(url)
        return self.urls_list

    def create_columns(self, url):
        """as in json file only contains data and not its relative column name this function get them from page source."""
        columns = []
        url = url.split('.ajax')[0]
        r = requests.get(url)
        html_contents = r.text
        html_soup = BeautifulSoup(html_contents, 'html.parser')
        script = html_soup.find(id="tabsAll")
        table = script.find('table')
        for text in table.find('tr').find_all('th'):
            columns.append(text.text.strip())
        
        return columns

