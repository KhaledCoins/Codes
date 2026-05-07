# REST (anotação)

- `GET /receitas` — lista o caderno inteiro
- `GET /receitas/<id>` — uma receita
- `POST /receitas` — cadastra

Resposta costuma vir em:

```json
{ "dados": { ... } }
```

## Links no JSON

Coloco `links` com URLs da própria API para praticar HATEOAS (nível 2 de Richardson): `self`, `update`, `delete`, `collection`.

## CORS

React em porta 5173 e Flask em 5000 → `flask_cors.CORS(app)`.
