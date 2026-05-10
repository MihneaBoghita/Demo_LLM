from database.db import get_connection
from semantic_service import get_embedding, get_top_category_ids
import json

def get_allKnowledge():
    with get_connection() as con: #with deschide conexiunea catre database, si o comiteaza automat 
        cur = con.cursor() #cursor = pointer care tine cont unde ne aflam in lista(in cazul nostru de produse)
        #De asemenea executa operatii in baza de date
        cur.execute("SELECT id, name, price FROM products") # * - all. Se selecteaza toate obiectele si se introduc in cursor
        rows = cur.fetchall() # Toate obiectele sunt transmise din cursor in variabila rows
        if not rows:
            return [] # Nu exista obiecte
        
        content = []
        for row in rows:
            content.append({
                "id": row[0],
                "name":row[1],
                "price":row[2]
            }) # Se adauga cate un obiect de tip produs

        return content
        
        
def get_knowledge(id):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(
        "SELECT id, name, price FROM products WHERE id = ?", (id,)) #se selecteaza fiecare produs din products unde id-ul este cel transmit prin parametru
         #Metoda accepta ca parametru doar tuple, "," transforma parametrul in unul
        row = cur.fetchone() # Se transmite un singur obiect din cursor catre variabila row(un singur produs)
        if not row:
            return None

        data = {
            "id":row[0],
            "name":row[1],
            "price":row[2],
            "categories": []
        }

        # Get categories
        cur.execute("""
            SELECT c.name FROM categories c
            JOIN product_categories pc ON c.id = pc.category_id
            WHERE pc.product_id = ?
        """, (id,))
        cat_rows = cur.fetchall()
        data["categories"] = [r[0] for r in cat_rows]

        return data

def add_knowledge(name, price):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(
        "SELECT 1 FROM products WHERE LOWER(name) = LOWER(?)",
        (name,)
        ) #Selectam orice element(indiferent de care ar fi acesta) din baza de date, unde numele este acelasi
        # Ca cel transmis prin parametru. Duplicate checking
        if cur.fetchone():
            raise Exception("Product already exists") #Se ridica o exceptie, efectiv se returneaza si se instantiaza un obiect
        
        embedding = get_embedding(name)
        embedding_json = json.dumps(embedding)

        cur.execute("INSERT INTO products (name, price, embedding) VALUES (?, ?, ?) RETURNING id, name, price", (name, price, embedding_json))
        row = cur.fetchone()
        product_id = row[0]
        
        item = {
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "categories": []
        }

        cur.execute("SELECT id, name, embedding FROM categories")
        categories_rows = cur.fetchall()
        categories = [{"id": r[0], "name": r[1], "embedding": r[2]} for r in categories_rows]

        if categories:
            top_category_ids = get_top_category_ids(name, categories, top_k=3)
            
            for cat_id in top_category_ids:
                cur.execute("INSERT INTO product_categories (product_id, category_id) VALUES (?, ?)", (product_id, cat_id))
            
            cur.execute("""
                SELECT c.name FROM categories c
                JOIN product_categories pc ON c.id = pc.category_id
                WHERE pc.product_id = ?
            """, (product_id,))
            cat_rows = cur.fetchall()
            item["categories"] = [r[0] for r in cat_rows]

        return item #Se returneaza obiectul adaugat, pentru confirmare, integritate a datelor, pentru ca clientul sa primeasca id-ul, etc


def update_product_price(produs_id, new_price):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute("SELECT id, name, price FROM products WHERE id = ?", (produs_id,))
        product = cur.fetchone()
        
        if not product:
            return None
            
        current_price = product[2]
        
        if float(new_price) == float(current_price):
            raise Exception(f"Noul pret ({new_price}) este identic cu pretul actual.")
        
        cur.execute("UPDATE products SET price = ? WHERE id = ? RETURNING id, name, price", (new_price, produs_id))
        row = cur.fetchone()
        return {
            "id": row[0],
            "name": row[1],
            "price": row[2]
        }

