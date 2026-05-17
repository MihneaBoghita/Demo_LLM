import json
from gemini_client import client


class QueryParser:

    @staticmethod
    def parse(user_query):

        prompt = f"""
Return ONLY valid JSON. No explanation. No markdown.

Schema:
{{
  "category": string|null,
  "color": string|null,
  "brand": string|null,
  "max_price": number|null,
  "sort": "price_asc"|"price_desc"|null,
  "limit": number|null
}}

Rules:
- "most expensive", "priciest", "highest price" -> sort: "price_desc"
- "least expensive", "cheapest", "lowest price" -> sort: "price_asc"
- "most expensive X" or "cheapest X" -> limit: 1
- "top 3 cheapest", "top 5 most expensive" -> limit: that number
- "under 100", "less than 50" -> max_price: that number

Examples:
"most expensive book" -> {{"category": "books", "sort": "price_desc", "limit": 1, "color": null, "brand": null, "max_price": null}}
"cheapest electronics" -> {{"category": "electronics", "sort": "price_asc", "limit": 1, "color": null, "brand": null, "max_price": null}}
"top 3 cheapest toys" -> {{"category": "toys", "sort": "price_asc", "limit": 3, "color": null, "brand": null, "max_price": null}}

Query: {user_query}
"""

        try:
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=prompt
            )

            content = response.text.strip()
            content = content.replace("```json", "").replace("```", "").strip()

            data = json.loads(content)

            if not isinstance(data, dict):
                return {}

            print(f"[QueryParser] filters: {data}")

            return data

        except Exception as e:
            print(f"[QueryParser ERROR] {e}")
            return {}