from flask import Blueprint, jsonify
from service import get_allKnowledge, get_knowledge

view_bp = Blueprint('view_produse', __name__)

@view_bp.route('/produse', methods=['GET'])
def get_produse():
    try:
        content = get_allKnowledge()
        return jsonify(content)
    except Exception as e:
        return jsonify({"eroare": str(e)}), 500


@view_bp.route('/produs/<int:produs_id>', methods=['GET'])
def get_produs(produs_id):
    try:
        content = get_knowledge(produs_id)

        if not content:
            return jsonify({"eroare": "Produsul nu a fost gasit"}), 404

        return jsonify(content)

    except Exception as e:
        return jsonify({"eroare": str(e)}), 500