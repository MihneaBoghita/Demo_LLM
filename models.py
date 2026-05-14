from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    brand: str
    color: str
    description: str
    tags: str
    category: str
    price: float
    embedding: str