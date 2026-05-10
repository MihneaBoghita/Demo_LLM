def validate_name(name):
    if not name or not isinstance(name, str) or not name.strip():
        return {"eroare": "Campul 'name' este obligatoriu si nu poate fi gol", "status": 400}, 400
    return None, 200

def validate_price(price):
    if price is None:
        return {"eroare": "Campul 'price' este obligatoriu", "status": 400}, 400
    if not isinstance(price, (int, float)) or isinstance(price, bool):
        return {"eroare": "Campul 'price' trebuie sa fie un numar", "status": 400}, 400
    if price <= 0:
        return {"eroare": "Campul 'price' trebuie sa fie un numar pozitiv", "status": 400}, 400
    return None, 200