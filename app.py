from flask import Flask, jsonify, request, Response
from service import get_knowledge,get_allknowledge, add_knowledge
from exeptions import DuplicateExeptions

app = Flask(__name__, template_folder="templates")


@app.route('/produse', methods=['GET']) 
def get_produse():
    content = get_allknowledge() #Extragem continutul din baza de date
    if not content :
        return jsonify({"Eroare" : "Nu exista produse"})
    return jsonify(content)
    
    

@app.route('/produs/<int:produs_id>', methods=['GET'])
def get_produs(produs_id):
    content = get_knowledge(produs_id)
    if not content:
        return jsonify({"eroare": "Produsul nu a fost gasit"})
    return jsonify(content)
    

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
    except DuplicateException as e: #Nu se mai returneaza obiectul, ci doar eroarea
        return jsonify({"eroare": str(e)}), 409

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

