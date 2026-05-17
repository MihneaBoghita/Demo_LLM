from database.db import Database
from semantic_service import get_embedding, get_top_category_ids
import json

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

        cursor.execute("SELECT id, name, price FROM products WHERE id = ?", (prod_id,))
        row = cursor.fetchone()

        if not row:
            return None

        data = {
            "id": row["id"],
            "name": row["name"],
            "price": row["price"],
            "categories": []
        }

        cursor.execute("""
            SELECT c.name FROM categories c
            JOIN product_categories pc ON c.id = pc.category_id
            WHERE pc.product_id = ?
        """, (prod_id,))
        cat_rows = cursor.fetchall()
        data["categories"] = [r["name"] for r in cat_rows]

        return data


def update_product_price(prod_id, new_price):
    with db.get_connection() as con:
        cursor = con.cursor()

        cursor.execute("SELECT id, name, price FROM products WHERE id = ?", (prod_id,))
        product = cursor.fetchone()

        if not product:
            return None

        if float(new_price) == float(product["price"]):
            raise Exception(f"Noul pret ({new_price}) este identic cu pretul actual.")

        cursor.execute("""
            UPDATE products SET price = ? WHERE id = ? RETURNING id, name, price
        """, (new_price, prod_id))
        row = cursor.fetchone()
        return {
            "id": row["id"],
            "name": row["name"],
            "price": row["price"]
        }