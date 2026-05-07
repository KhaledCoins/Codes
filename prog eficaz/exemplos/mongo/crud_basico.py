"""Testa insert/find sem Flask."""
from bson.objectid import ObjectId
from conexao import col_receitas


def inserir_exemplo():
    doc = {
        "titulo": "Ovos mexidos",
        "modo_preparo": "Bater ovos, refogar na manteiga.",
        "categoria": "salgado",
        "ingredientes": ["ovos", "manteiga", "sal"],
    }
    r = col_receitas.insert_one(doc)
    print("id:", r.inserted_id)


def listar():
    for d in col_receitas.find():
        print(str(d["_id"]), d.get("titulo"))


if __name__ == "__main__":
    inserir_exemplo()
    listar()
