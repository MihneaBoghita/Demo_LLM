from flask import Flask
from routes.add_produse import add_bp
from routes.view_produse import view_bp
from routes.update_produse import update_bp
from routes.frontend import frontend_bp

app = Flask(__name__, template_folder="templates")
app.register_blueprint(frontend_bp)
app.register_blueprint(add_bp)
app.register_blueprint(view_bp)
app.register_blueprint(update_bp)

if __name__ == "__main__": #Toate fisierele python, cand sunt rulate, devin obiecte, care contin variabile(ex: __name__)
    app.run(debug=True, host="0.0.0.0", port=5000)
