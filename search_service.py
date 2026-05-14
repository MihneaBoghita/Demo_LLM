import json
import torch
from sentence_transformers import util

from embedding_service import EmbeddingService
from query_parser import QueryParser
from database.db import Database


class SearchService:

    def __init__(self):
        self.db = Database()

    def rerank_products(self, user_query, products):

        if not products:
            return []

        query_embedding = EmbeddingService.generate_query_embedding(user_query)

        product_embeddings = []

        for p in products:
            embedding = p["embedding"]

            if isinstance(embedding, str):
                embedding = json.loads(embedding)

            product_embeddings.append(embedding)

        query_embedding = torch.tensor(query_embedding, dtype=torch.float32)
        product_embeddings = torch.tensor(product_embeddings, dtype=torch.float32)

        hits = util.semantic_search(
            query_embedding,
            product_embeddings,
            top_k=min(10, len(products))
        )

        ranked = []

        for hit in hits[0]:
            product = products[hit["corpus_id"]]
            product["score"] = float(hit["score"])
            ranked.append(product)

        return ranked

    def search(self, user_query):

        try:
            filters = QueryParser.parse(user_query)

            if filters:
                products = self.db.filter_products(filters)
            else:
                products = self.db.get_all_products()

            if not products:
                return []

            ranked = self.rerank_products(user_query, products)

            sort = filters.get("sort") if filters else None
            if sort == "price_asc":
                ranked.sort(key=lambda p: p["price"])
            elif sort == "price_desc":
                ranked.sort(key=lambda p: p["price"], reverse=True)

            limit = filters.get("limit") if filters else None
            if limit:
                ranked = ranked[:int(limit)]

            return ranked

        except Exception as e:
            return [{"error": str(e)}]