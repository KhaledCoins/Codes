"""API do caderno de receitas — Flask + Mongo."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from flask import Flask, request, jsonify
from flask_cors import CORS
from bson.objectid import ObjectId
from bson.errors import InvalidId

from mongo.conexao import col_receitas
from validacao_receita import validar, receita_json

app = Flask(__name__)
CORS(app)


@app.route("/receitas", methods=["POST"])
def cadastrar():
    body = request.get_json(silent=True)
    ok, erro, status = validar(body)
    if not ok:
        return jsonify(erro), status

    doc = {
        "titulo": body["titulo"],
        "modo_preparo": body["modo_preparo"],
        "categoria": body["categoria"],
        "ingredientes": body["ingredientes"],
    }
    ins = col_receitas.insert_one(doc)
    rid = str(ins.inserted_id)
    return jsonify({"dados": receita_json(doc, rid)}), 201


@app.route("/receitas", methods=["GET"])
def listar():
    saida = []
    for d in col_receitas.find():
        rid = str(d["_id"])
        saida.append(
            receita_json(
                {
                    "titulo": d["titulo"],
                    "modo_preparo": d["modo_preparo"],
                    "categoria": d["categoria"],
                    "ingredientes": d.get("ingredientes", []),
                },
                rid,
            )
        )
    return jsonify({"dados": saida})


@app.route("/receitas/<rid>", methods=["GET"])
def detalhe(rid):
    try:
        oid = ObjectId(rid)
    except InvalidId:
        return "", 404
    d = col_receitas.find_one({"_id": oid})
    if d is None:
        return "", 404
    doc = {
        "titulo": d["titulo"],
        "modo_preparo": d["modo_preparo"],
        "categoria": d["categoria"],
        "ingredientes": d.get("ingredientes", []),
    }
    return jsonify({"dados": receita_json(doc, str(d["_id"]))})


if __name__ == "__main__":
    app.run(debug=True)
