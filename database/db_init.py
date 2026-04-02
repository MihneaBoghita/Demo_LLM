from database.db import get_connection

def init():
    with get_connection(auto_create = True) as con:
        cur = con.cursor()
    
        cur.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER
            )
        """)

if __name__ == '__main__':
    init()