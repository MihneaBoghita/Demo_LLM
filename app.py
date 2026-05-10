from flask import Flask, jsonify, request, Response
from service import get_knowledge,get_allknowledge, add_knowledge
from exceptions import DuplicateExeptions
import logging

logging.basicConfig(
    level=logging.INFO,  # vezi INFO, WARNING, ERROR
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = Flask(__name__, template_folder="templates")


@app.route('/produse', methods=['GET']) 
def get_produse():
    try:
        content = get_allknowledge()

        if not content:
            return jsonify({"Eroare": "Nu exista produse"}), 404
        return jsonify(content), 200

    except Exception:
        logging.exception("Eroare")
    return jsonify({"Status": "Error"}), 500
    
    

@app.route('/produs/<int:produs_id>', methods=['GET'])
def get_produs(produs_id):
    try:
        content = get_knowledge(produs_id)
        if not content:
            return jsonify({"eroare": "Produsul nu a fost gasit"}),404
        return jsonify(content),200
    except Exception as e:
        # return jsonify({"Status": "Error", "Message": str(e)}), 500     ->   risc de securitate, str(e) arata direct eroarea 
        logging.exception("Eroare la get_produs")
    return jsonify({"Status": "Error", "Message": "Internal server error"}), 500
    

@app.route('/add_produs/', methods=['POST'])
def add_produs():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    if not name or not price:
        return jsonify({"eroare": "Lipsesc date (nume sau pret)"}), 400
    try: #Exception handling, blocul de cod "asculta" exceptii(erori) si returneaza in functie de eroare
        item = add_knowledge(name, price)
        return jsonify({
            "message": "Produsul a fost adăugat",
            "data": item
        }), 201
    except DuplicateExeptions as e:
        logging.warning("Produs duplicat incercat: %s", name)
        return jsonify({"eroare": "Produsul exista deja"}), 409

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)