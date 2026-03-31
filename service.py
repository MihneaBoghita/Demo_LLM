from database.db import get_connection
from exceptions import DuplicateExeptions
import logging


def get_allknowledge():
    try:
        with get_connection() as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM products")

            rows = cur.fetchall()
            if not rows:
                return None
            
            content = []
            for row in rows:
                content.append({
                    "id": row[0],
                    "name": row[1],
                    "price": row[2]
                }) 
            return content

    except Exception:
        logging.exception("Eroare la citirea tuturor produselor")
        return None


def get_knowledge(id):
    try:
        with get_connection() as con:
            cur = con.cursor()

            cur.execute(
                "SELECT * FROM products WHERE id = ?",
                (id,)
            )
            row = cur.fetchone()

            if not row:
                return None

            return {
                "id": row[0],
                "name": row[1],
                "price": row[2]
            }

    except Exception:
        logging.exception(f"Eroare la get_knowledge pentru id={id}")
        return None


def add_knowledge(name, price):
    try:
        with get_connection() as con:
            cur = con.cursor()

            cur.execute(
                "SELECT 1 FROM products WHERE LOWER(name) = LOWER(?)",
                (name,)
            )

            if cur.fetchone():
                raise DuplicateExeptions()

            cur.execute(
                "INSERT INTO products (name, price) VALUES (?, ?)",
                (name, price)
            )

            new_id = cur.lastrowid

            cur.execute(
                "SELECT * FROM products WHERE id = ?",
                (new_id,)
            )

            row = cur.fetchone()

            return {
                "id": row[0],
                "name": row[1],
                "price": row[2]
            }

    except DuplicateExeptions:
        raise  # lasi route-ul sa trateze

    except Exception:
        logging.exception("Eroare la add_knowledge")
        return None