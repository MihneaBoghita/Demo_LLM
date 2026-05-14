import sqlite3
import json
from config import DB_PATH
from semantic_service import get_embedding


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # PRODUCTS
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            brand TEXT,
            color TEXT,
            description TEXT,
            tags TEXT,
            category TEXT,
            price REAL,
            embedding TEXT
        )
    """)

    # CATEGORIES
    cur.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            embedding TEXT
        )
    """)

    # PRODUCT - CATEGORY RELATION
    cur.execute("""
        CREATE TABLE IF NOT EXISTS product_categories (
            product_id INTEGER,
            category_id INTEGER,
            PRIMARY KEY (product_id, category_id),
            FOREIGN KEY (product_id) REFERENCES products(id),
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    """)

    conn.commit()

    # SEED CATEGORIES
    seed_categories = [
        "Electronics",
        "Furniture",
        "Clothing",
        "Books",
        "Toys",
        "Food",
        "Office Supplies",
        "Home Decor"
    ]

    for cat in seed_categories:
        cur.execute("SELECT id FROM categories WHERE name = ?", (cat,))
        if not cur.fetchone():
            embedding = json.dumps(get_embedding(cat))
            cur.execute(
                "INSERT INTO categories (name, embedding) VALUES (?, ?)",
                (cat, embedding)
            )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")