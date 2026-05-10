from database.db import get_connection
import json
from semantic_service import get_embedding

def init():
    with get_connection(auto_create=True) as con:
        cur = con.cursor()
    
        cur.execute("""
            CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            embedding TEXT
        )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS categories(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            embedding TEXT
        )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS product_categories(
            product_id INTEGER,
            category_id INTEGER,
            PRIMARY KEY (product_id, category_id),
            FOREIGN KEY (product_id) REFERENCES products(id),
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
        """)

        # Seed categories if they don't exist
        seed_categories = ["Electronics", "Furniture", "Clothing", "Books", "Toys", "Food", "Office Supplies", "Home Decor"]
        for cat_name in seed_categories:
            cur.execute("SELECT id FROM categories WHERE name = ?", (cat_name,))
            if not cur.fetchone():
                embedding = json.dumps(get_embedding(cat_name))
                cur.execute("INSERT INTO categories (name, embedding) VALUES (?, ?)", (cat_name, embedding))

if __name__ == '__main__':
    init()