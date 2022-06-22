from urls import ISHARES_HOLDINGS as ishares, JSON_QUERY as query


class IShareUrlList:
    def __init__(self):
        self.ishare_list = ishares
        self.urls_list = []
    
    def create_endpinots(self):
        """modify urls list and change it from csv format to json."""
        for ishare in self.ishare_list:
            url = (ishare[0].split('?')[0] + query)
            self.urls_list.append(url)
        return self.urls_list



