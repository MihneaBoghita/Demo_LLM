from database.db import Database

db = Database()


def add_knowledge(product_data):
    with db.get_connection() as con:
        cursor = con.cursor()

        cursor.execute("""
            INSERT INTO products (name, price, embedding)
            VALUES (?, ?, ?)
        """, (
            product_data["name"],
            product_data["price"],
            product_data.get("embedding")
        ))


def get_allKnowledge():
    return db.get_all_products()


def get_knowledge(prod_id):
    with db.get_connection() as con:
        cursor = con.cursor()

        cursor.execute("SELECT * FROM products WHERE id = ?", (prod_id,))
        row = cursor.fetchone()

        return dict(row) if row else None
    
def update_product_price(prod_id, new_price):
    with db.get_connection() as con:
        cursor = con.cursor()

        cursor.execute("""
            UPDATE products
            SET price = ?
            WHERE id = ?
        """, (new_price, prod_id))