import sqlite3
from config import DB_PATH
from contextlib import contextmanager


class Database:
    def __init__(self):
        pass

    @contextmanager
    def get_connection(self):
        con = sqlite3.connect(DB_PATH)
        con.row_factory = sqlite3.Row

        try:
            yield con
            con.commit()
        except Exception as e:
            con.rollback()
            raise e
        finally:
            con.close()

    def filter_products(self, filters):
        products = []

        with self.get_connection() as con:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM products")
            rows = cursor.fetchall()

            products = [dict(row) for row in rows]

        return products

    def get_all_products(self):
        products = []

        with self.get_connection() as con:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM products")
            rows = cursor.fetchall()

            products = [dict(row) for row in rows]

        return products