# Flask

| Arquivo | Descrição |
|---------|-----------|
| `app_sem_banco.py` | GET/POST sem Mongo |
| `app_receitas.py` | API completa com validação |
| `validacao_receita.py` | Regras e montagem do JSON de resposta |
| `checar_lista.py` | Helper opcional para listas |

## O que foi usado nos exercícios (backend)

### Bloco 1: validação e erros

- arquivo-base: `validacao_receita.py`
- função principal: `validar(body)`
- reaproveitamento comum:
  - campos obrigatórios;
  - `type()` para tipo inválido;
  - lista de valores permitidos (`CATEGORIAS`).

### Bloco 2: criação no banco

- arquivo-base: `app_receitas.py`, função `cadastrar()`
- reaproveitamento comum:
  - `request.get_json(silent=True)`;
  - chamada da validação;
  - `insert_one` + `str(inserted_id)`;
  - retorno `201` com `{"dados": ...}`.

### Bloco 3: listagem e consulta por id

- arquivo-base: `app_receitas.py`, funções `listar()` e `detalhe()`
- reaproveitamento comum:
  - `find()` para coleção;
  - `ObjectId` com `try/except` para validar id;
  - 404 para id inválido ou não encontrado.

### Bloco 4: links HATEOAS

- arquivo-base: `validacao_receita.py`, funções `links_receita()` e `receita_json()`
- reaproveitamento comum:
  - padronizar links `self/update/delete/collection` por item.

## Como adaptar rapidamente (receitas -> outro domínio)

1. troque rota `/receitas` pelo recurso do seu projeto;
2. troque `OBRIGATORIOS` e `CATEGORIAS`;
3. troque nomes de campos no `doc` e no `receita_json`;
4. mantenha a estrutura de validação e de retorno.

```bash
pip install -r requirements.txt
python app_sem_banco.py
python app_receitas.py
```
