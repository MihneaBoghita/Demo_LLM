from flask import Blueprint, request, jsonify
from search_service import SearchService

search_bp = Blueprint("search", __name__)
search_service = SearchService()

@search_bp.route("/api/search", methods=["GET"])
def search():
    query = request.args.get("q")

    if not query:
        return jsonify({"error": "Missing query"}), 400

    results = search_service.search(query)

    clean_results = [
        {k: v for k, v in product.items() if k != "embedding"}
        for product in results
    ]

    return jsonify(clean_results)