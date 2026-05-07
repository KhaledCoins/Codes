# Validação na API

Ordem que uso no POST de receita:

1. JSON com `get_json(silent=True)`
2. Campos obrigatórios → HTTP 400
3. `type(campo) is not str` → 422
4. `ingredientes` tem que ser `list` de `str`
5. `categoria` dentro de `CATEGORIAS`

Códigos de erro neste repo: `campos_faltando`, `tipo_errado`, `categoria_invalida` — no seu outro projeto pode usar outros nomes.

Implementação: `exemplos/flask/validacao_receita.py`.
