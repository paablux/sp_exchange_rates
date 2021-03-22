 
from time import sleep
from datetime import datetime, timedelta

from pymysql import connect
from pymysql.cursors import DictCursor
from pymysql.err import IntegrityError, InternalError, OperationalError

from utils.settings import read_settings


class BaseDB():
    def __init__(self):
        self.settings = read_settings()
        connection = connect(
            host=self.settings['mysql_host'],
            port=self.settings['mysql_port'],
            user=self.settings['mysql_user'],
            password=self.settings['mysql_password'],
            db=self.settings['mysql_database'],
            charset='utf8',
            cursorclass=DictCursor,
            autocommit=False
        )
        self.conn = connection


    def execute(self, query, args=None):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(query, args)
            except Exception as e:
                print(args)
                print(e)
                print('Error in insert')
                self.conn.rollback()
                self.close()
                raise e

    @staticmethod
    def generate_sql_insert(table, data):
        """ Insert template, requires a dictionary with the column names as keys and there corresponding values """
        def columns(d): return ', '.join(['{}'.format(k) for k in d])
        def values(d): return [v for v in d.values()]
        def placeholders(d): return ', '.join(['%s'] * len(d))
        sql_template = 'INSERT INTO {} ( {} ) VALUES ( {} );'
        return sql_template.format(table, columns(data), placeholders(data)), values(data)

    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if traceback is None:
            # No exception, so commit
            self.commit()
            self.close()
        else:
            # Exception occurred, so rollback.
            self.rollback()
            self.close()
    
    def load(self, data):
        base_sql = 'INSERT INTO `exchange_rates` (base_currency, to_exchange_currency, exchange_rate, date) VALUES (%s, %s, %s, %s);'
        for row in data:
            if row['exchange_rate']:
                params = [row['base_currency'], row['to_exchange_currency'], row['exchange_rate'], row['date']]
                self.execute(base_sql, params)