from sentence_transformers import SentenceTransformer
import json


model = SentenceTransformer('all-MiniLM-L6-v2')


class EmbeddingService:

    @staticmethod
    def generate_product_embedding(product):

        searchable_text = f"""
        {product['name']}
        {product['brand']}
        {product['description']}
        {product['tags']}
        {product['color']}
        {product['category']}
        """

        embedding = model.encode(searchable_text)

        return json.dumps(embedding.tolist())


    @staticmethod
    def generate_query_embedding(query):

        return model.encode(
            query,
            convert_to_tensor=True
        )