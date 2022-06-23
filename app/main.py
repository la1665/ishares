from sqlalchemy import create_engine
import numpy as np
from fetch_data import CreateDataFrame


class Database:
    def __init__(self):
        self.dataframe = CreateDataFrame()

    def create_table(self):
        df = self.dataframe.concat_dfs()
        df = df.replace(r'^-', np.nan, regex=True)
        engine = create_engine('postgresql://postgres:postgres@pgdb:5432/ishares')
        df.to_sql('holdings', engine, if_exists='append')



if __name__ == '__main__':
    res = Database()
    res.create_table()

