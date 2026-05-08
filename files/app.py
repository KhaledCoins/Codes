"""
Referência: API RESTful com Flask + MongoDB
Domínio: Cadastro de Projetos (ProjectHub)

Conceitos cobertos:
  - Rotas REST (POST / GET coleção / GET recurso) → Nível 2 de Richardson
  - Validação de campos obrigatórios → 400
  - Validação de tipos com type()  → 422
  - Validação de valores permitidos → 422
  - Links HATEOAS em todas as respostas
  - Busca por ID usando ObjectId
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId

# import certifi                          # descomente se tiver problema de SSL
# ca = certifi.where()

app = Flask(__name__)
CORS(app)

# ── Conexão com MongoDB Atlas ──────────────────────────────────────────────────
connection = (
    "mongodb+srv://<usuario>:<senha>@cluster.xxxxx.mongodb.net/"
    "ProjectHub?retryWrites=true&w=majority"
)
client = MongoClient(connection)
# client = MongoClient(connection, tlsCAFile=ca)   # versão com certifi

db = client["ProjectHub"]
projetos = db["projetos"]


# ── Helper: links HATEOAS ─────────────────────────────────────────────────────
def hateoas(id_str: str) -> dict:
    """
    Retorna os links HATEOAS padrão para um recurso.
    Padrão: self, update, delete apontam para o recurso;
            collection aponta para a coleção.
    """
    base = "/projetos/" + id_str
    return {
        "self":       base,
        "update":     base,
        "delete":     base,
        "collection": "/projetos",
    }


# ── POST /projetos ─────────────────────────────────────────────────────────────
@app.route("/projetos", methods=["POST"])
def criar_projeto():
    """
    Cadastra um novo projeto.

    Payload esperado:
    {
        "nome":        "Meu projeto",
        "descricao":   "O que ele faz",
        "tipo":        "web | mobile | dados | automacao",
        "tecnologias": ["python", "flask"]
    }

    Fluxo de validação:
      1. Campos obrigatórios → 400 se algum faltar
      2. Tipos de cada campo → 422 se algum estiver errado
      3. Valor permitido de 'tipo' → 422 se não estiver na lista
      4. Inserção → 201 com dados + links HATEOAS
    """
    dados = request.get_json(silent=True)
    if dados is None:
        dados = {}

    # ── 1. Campos obrigatórios ────────────────────────────────────────────────
    obrigatorios = ["nome", "descricao", "tipo", "tecnologias"]
    missing = []
    for campo in obrigatorios:
        if campo not in dados or dados[campo] is None:
            missing.append(campo)

    if len(missing) > 0:
        return jsonify({
            "erro": {
                "codigo":   "campo_obrigatorio",
                "mensagem": "Campos obrigatórios ausentes.",
                "detalhes": {"missing": missing},
            }
        }), 400

    # ── 2. Validação de tipos ─────────────────────────────────────────────────
    # Usa type() (e não isinstance()) conforme padrão adotado no curso.
    # Retorna apenas o PRIMEIRO campo com problema.

    if type(dados["nome"]) is not str:
        return jsonify({
            "erro": {
                "codigo":   "tipo_invalido",
                "mensagem": "Um ou mais campos possuem tipo inválido.",
                "detalhes": {"campo": "nome", "expected": "string"},
            }
        }), 422

    if type(dados["descricao"]) is not str:
        return jsonify({
            "erro": {
                "codigo":   "tipo_invalido",
                "mensagem": "Um ou mais campos possuem tipo inválido.",
                "detalhes": {"campo": "descricao", "expected": "string"},
            }
        }), 422

    if type(dados["tipo"]) is not str:
        return jsonify({
            "erro": {
                "codigo":   "tipo_invalido",
                "mensagem": "Um ou mais campos possuem tipo inválido.",
                "detalhes": {"campo": "tipo", "expected": "string"},
            }
        }), 422

    if type(dados["tecnologias"]) is not list:
        return jsonify({
            "erro": {
                "codigo":   "tipo_invalido",
                "mensagem": "Um ou mais campos possuem tipo inválido.",
                "detalhes": {"campo": "tecnologias", "expected": "list of strings"},
            }
        }), 422

    # Valida cada item da lista
    for item in dados["tecnologias"]:
        if type(item) is not str:
            return jsonify({
                "erro": {
                    "codigo":   "tipo_invalido",
                    "mensagem": "Um ou mais campos possuem tipo inválido.",
                    "detalhes": {"campo": "tecnologias", "expected": "list of strings"},
                }
            }), 422

    # ── 3. Valores permitidos ─────────────────────────────────────────────────
    tipos_permitidos = ["web", "mobile", "dados", "automacao"]

    if dados["tipo"] not in tipos_permitidos:
        return jsonify({
            "erro": {
                "codigo":   "valor_invalido",
                "mensagem": "Valor não permitido para o campo tipo.",
                "detalhes": {
                    "campo":          "tipo",
                    "allowed_values": tipos_permitidos,
                },
            }
        }), 422

    # ── 4. Inserção ───────────────────────────────────────────────────────────
    doc = {
        "nome":        dados["nome"],
        "descricao":   dados["descricao"],
        "tipo":        dados["tipo"],
        "tecnologias": dados["tecnologias"],
    }
    retorno = projetos.insert_one(doc)
    _id_str = str(retorno.inserted_id)   # ObjectId → string

    return jsonify({
        "dados": {
            "_id":         _id_str,
            "nome":        doc["nome"],
            "descricao":   doc["descricao"],
            "tipo":        doc["tipo"],
            "tecnologias": doc["tecnologias"],
            "links":       hateoas(_id_str),
        }
    }), 201


# ── GET /projetos ──────────────────────────────────────────────────────────────
@app.route("/projetos", methods=["GET"])
def listar_projetos():
    """
    Retorna todos os projetos cadastrados.
    Lista vazia → { "dados": [] }
    """
    lista = []
    for doc in projetos.find():
        sid = str(doc["_id"])
        lista.append({
            "_id":         sid,
            "nome":        doc["nome"],
            "descricao":   doc["descricao"],
            "tipo":        doc["tipo"],
            "tecnologias": doc["tecnologias"],
            "links":       hateoas(sid),
        })
    return jsonify({"dados": lista})


# ── GET /projetos/<id> ─────────────────────────────────────────────────────────
@app.route("/projetos/<pid>", methods=["GET"])
def obter_projeto(pid):
    """
    Retorna um projeto específico pelo ID.

    - ObjectId(pid) converte a string para o formato aceito pelo MongoDB.
    - InvalidId é lançado se a string não for um ObjectId válido → 404.
    - find_one retorna None se não encontrar → 404.
    """
    try:
        oid = ObjectId(pid)
    except InvalidId:
        return "", 404

    doc = projetos.find_one({"_id": oid})
    if doc is None:
        return "", 404

    sid = str(doc["_id"])
    return jsonify({
        "dados": {
            "_id":         sid,
            "nome":        doc["nome"],
            "descricao":   doc["descricao"],
            "tipo":        doc["tipo"],
            "tecnologias": doc["tecnologias"],
            "links":       hateoas(sid),
        }
    })


if __name__ == "__main__":
    app.run(debug=True)
