from database.db import Database
from embedding_service import EmbeddingService


db = Database()


products = [
    {
        "name": "ASUS ROG Strix G16",
        "brand": "ASUS",
        "color": "red",
        "description": "Gaming laptop with RTX graphics",
        "tags": "gaming,rgb,powerful",
        "category": "laptop",
        "price": 4200
    },
    {
        "name": "Lenovo IdeaPad Slim",
        "brand": "Lenovo",
        "color": "silver",
        "description": "Lightweight laptop for school",
        "tags": "student,battery,thin",
        "category": "laptop",
        "price": 2600
    }
]


for product in products:

    embedding = EmbeddingService.generate_product_embedding(product)

    db.add_product(
        product['name'],
        product['brand'],
        product['color'],
        product['description'],
        product['tags'],
        product['category'],
        product['price'],
        embedding
    )


print("Products inserted")