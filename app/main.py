from sqlalchemy import create_engine
import numpy as np
from fetch_data import CreateDataFrame


class Database:
    def __init__(self):
        self.dataframe = CreateDataFrame()

    def create_table(self):
        engine = create_engine('postgresql://postgres:postgres@pgdb:5432/ishares')
        df = self.dataframe.concat_dfs()
        df = df.replace(r'^-', np.nan, regex=True)
        df.to_sql('holdings', engine, if_exists='replace')
        data_list, ticker = self.dataframe.ticker_ohlc()
        for data in range(len(data_list)):
            data_list[data].to_sql('{}_ohlc'.format(str(ticker[data]).lower()), engine, if_exists='replace')



if __name__ == '__main__':
    res = Database()
    res.create_table()
    # res.create_ohlc_table()

