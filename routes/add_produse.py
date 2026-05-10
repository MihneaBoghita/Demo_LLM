from flask import Blueprint, jsonify, request
from service import add_knowledge
from validators import validate_name, validate_price

add_bp = Blueprint('add_produse', __name__)

@add_bp.route('/add_produs', methods=['POST'])
def add_produs():
    try:
        data = request.get_json() or {}

        name = data.get('name')
        price = data.get('price')

        err, status = validate_name(data.get('name'))
        if err:
            return jsonify(err), status
            
        err, status = validate_price(data.get('price'))
        if err:
            return jsonify(err), status

        name = name.strip()
        item = add_knowledge(name, price)
        return jsonify({
            "mesaj": "Produsul a fost adaugat",
            "date": item
        }), 201    
    except Exception as e: #Nu se mai returneaza obiectul, ci doar eroarea
        return jsonify({"eroare": str(e), "status": 409}), 409 #str "intreaba" obiectul daca are o metoda de string. foarte interesant
    #clasa Exception, pe care o mosteneste, contine astfel de metoda
