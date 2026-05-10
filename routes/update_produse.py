from flask import Blueprint, jsonify, request
from service import update_product_price
from validators import validate_price

update_bp = Blueprint('update_produse', __name__)

@update_bp.route('/produs/<int:produs_id>/pret', methods=['PATCH'])
def update_pret(produs_id):
    try:
        data = request.get_json() or {}
        
        new_price = data.get('price')
        
        # Validare pret
        err, status = validate_price(new_price)
        if err:
            return jsonify(err), status
            
        updated_produs = update_product_price(produs_id, new_price)
        if not updated_produs:
            return jsonify({"eroare": "Produsul nu a fost gasit", "status": 404}), 404
            
        return jsonify({
            "mesaj": "Produsul a fost adaugat",
            "date": updated_produs}), 201
    
    except Exception as e:
        return jsonify({"eroare": str(e), "status": 500}), 500
