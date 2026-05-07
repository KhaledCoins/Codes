"""Flask só para testar rotas — receitas ficam em lista na RAM."""
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

_memoria = []


@app.route("/receitas", methods=["GET"])
def get_lista():
    return jsonify({"dados": _memoria})


@app.route("/receitas", methods=["POST"])
def post_receita():
    body = request.get_json(silent=True) or {}
    if not body.get("titulo"):
        return jsonify({"erro": "falta titulo"}), 400
    item = {
        "titulo": body["titulo"],
        "modo_preparo": body.get("modo_preparo", ""),
        "categoria": body.get("categoria", "salgado"),
        "ingredientes": body.get("ingredientes", []),
    }
    _memoria.append(item)
    return jsonify({"dados": item}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
