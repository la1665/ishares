from fetch_columns_names import ColumnsNames


class Serializer:
    def __init__(self):
        self.cols = ColumnsNames()

    def columns_serializer(self, url):
        cols = self.cols.create_columns(url)
        cols = ['Ticker' if cols[i]=='Issuer Ticker' else cols[i] for i in range(len(cols))]
        cols = ['Currency' if cols[i]=='Market Currency' else cols[i] for i in range(len(cols))]
        cols = [str.lower(i) for i in cols ]
        return cols



# if __name__ == '__main__':
# 	a = Serializer()
#     print(a.columns_serializer())

