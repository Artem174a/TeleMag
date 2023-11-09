import os

import psycopg2
from conf import config
from database.SQL import SQL_FOLDER


class DB:
    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=config['database']['dbname'],
                user=config['database']['user'],
                password=config['database']['password'],
                host=config['database']['host'],
                port=config['database']['port']
            )
        except Exception as error:
            print(f"Error while connecting to PostgreSQL: {error}")

    def execute_query(self, sql_query, is_commit: bool, fetch_all: bool = None, is_sql_file: bool = False):
        if is_sql_file is True:
            file_path = os.path.join(SQL_FOLDER, sql_query)
            with open(file_path+'.sql', 'r') as file:
                query = file.read()
        else:
            query = sql_query
        if not self.conn:
            self.connect()

        cursor = self.conn.cursor()
        cursor.execute(query)
        if is_commit is True:
            self.conn.commit()
            return True
        if fetch_all is True:
            return cursor.fetchall()
        else:
            return cursor.fetchone()[0]

    def close(self):
        self.conn.close()

    def run(self, sql_query, is_commit: bool, fetch_all: bool = None, is_sql_file: bool = False):
        try:
            self.connect()
            self.execute_query(sql_query, is_commit, fetch_all, is_sql_file)
        except Exception as error:
            print(f'Database has error - {error}')
        finally:
            self.close()
