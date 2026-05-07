"""Regras de validação do cadastro de receita."""

CATEGORIAS = ["doce", "salgado", "bebida", "vegetariano"]
OBRIGATORIOS = ["titulo", "modo_preparo", "categoria", "ingredientes"]


def links_receita(receita_id):
    path = "/receitas/" + receita_id
    return {
        "self": path,
        "update": path,
        "delete": path,
        "collection": "/receitas",
    }


def validar(body):
    if body is None:
        body = {}

    faltam = [c for c in OBRIGATORIOS if c not in body or body[c] is None]
    if faltam:
        return False, {
            "erro": {
                "codigo": "campos_faltando",
                "mensagem": "Preencha todos os campos da receita.",
                "detalhes": {"faltam": faltam},
            }
        }, 400

    if type(body["titulo"]) is not str:
        return False, _erro_tipo("titulo"), 422
    if type(body["modo_preparo"]) is not str:
        return False, _erro_tipo("modo_preparo"), 422
    if type(body["categoria"]) is not str:
        return False, _erro_tipo("categoria"), 422

    if type(body["ingredientes"]) is not list:
        return False, _erro_tipo("ingredientes", "lista de textos"), 422
    for ing in body["ingredientes"]:
        if type(ing) is not str:
            return False, _erro_tipo("ingredientes", "lista de textos"), 422

    if body["categoria"] not in CATEGORIAS:
        return False, {
            "erro": {
                "codigo": "categoria_invalida",
                "mensagem": "Categoria fora da lista.",
                "detalhes": {"opcoes": CATEGORIAS},
            }
        }, 422

    return True, None, None


def _erro_tipo(nome_campo, esperado="texto"):
    return {
        "erro": {
            "codigo": "tipo_errado",
            "mensagem": "Tipo incorreto em " + nome_campo + ".",
            "detalhes": {"campo": nome_campo, "esperado": esperado},
        }
    }


def receita_json(doc, id_str):
    return {
        "_id": id_str,
        "titulo": doc["titulo"],
        "modo_preparo": doc["modo_preparo"],
        "categoria": doc["categoria"],
        "ingredientes": doc["ingredientes"],
        "links": links_receita(id_str),
    }
