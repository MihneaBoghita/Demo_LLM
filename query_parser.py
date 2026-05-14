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
  "sort": "price_asc"|"price_desc"|null
}}

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

            return data

        except Exception:
            return {}