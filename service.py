from database.db import get_connection
from exeptions import DuplicateExeptions

def get_allknowledge():
    with get_connection() as con:#with deschide conexiunea catre database, si o inchide automat cand se iese din blocul indentat
        cur = con.cursor()
        #De asemenea executa operatii in baza de date
        cur.execute("SELECT * FROM")


def get_knowledge(id):
    con = get_connection()
    cur = con.cursor()
    cur.execute(
    "SELECT * FROM products WHERE id = ?",
    (id,)
    )
    row = cur.fetchone()
    if not row:
        return None
    con.close()
    data = {
        "id":row[0],
        "name":row[1],
        "price":row[2]
    }
    return data

def add_knowledge(name, price):
    con = get_connection()
    cur = con.cursor()

    cur.execute(
    "SELECT 1 FROM products WHERE LOWER(name) = LOWER(?)",
    (name,)
    )
    if cur.fetchone():
        return {"Status": "Duplicate"}
    cur.execute(
    "INSERT INTO products (name, price) VALUES (?, ?)",
    (name, price)
    )
    con.commit()
    con.close()
    return {"Status": "Success"}

