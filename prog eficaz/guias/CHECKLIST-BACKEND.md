# Checklist — API Flask + Mongo (receitas)

- [ ] `CORS(app)` se o React usar outra porta
- [ ] `get_json(silent=True)` no POST
- [ ] Campos obrigatórios da receita presentes
- [ ] `ingredientes` é `list` e cada item é `str`
- [ ] `categoria` está em `CATEGORIAS`
- [ ] `insert_one` + `str(inserted_id)` na resposta 201
- [ ] GET lista retorna `{"dados": [...]}` ou `[]`
- [ ] GET por id com `ObjectId` e 404
- [ ] Objeto `links` em cada receita (URLs sob `/receitas`)
