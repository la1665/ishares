from sqlalchemy import create_engine
import sqlite3 as sql

from fetch_data import CreateDataFrame


class Database:
    def __init__(self):
        self.dataframe = CreateDataFrame()

    def create_table(self):
        df = self.dataframe.concat_dfs()
        engine = create_engine('postgresql://postgres:postgres@pgdb:5432/ishares')
        df.to_sql('holdings', engine)



if __name__ == '__main__':
    res = Database()
    res.create_table()

