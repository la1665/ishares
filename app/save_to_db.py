import sqlite3 as sql

from fetch_data import CreateDataFrame


class Database:
    def __init__(self):
        self.dataframe = CreateDataFrame()

    def create_table(self):
        df = self.dataframe.concat_dfs()
        conn = sql.connect('./ishares.db')
        df.to_sql('ishares', conn)



if __name__ == '__main__':
    res = Database()
    res.create_table()

