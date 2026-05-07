# Mapa de aproveitamento (o que foi adaptado)

Este arquivo serve para você identificar rapidamente:

1. **qual parte do caderno de estudos foi usada**, e
2. **como ela foi adaptada** para um exercício real.

---

## Backend (API com Flask + Mongo)

### 1) Cadastro com validação (POST)

- **Fonte no caderno:** `exemplos/flask/app_receitas.py` + `exemplos/flask/validacao_receita.py`
- **Trechos-chave usados:**
  - `request.get_json(silent=True)`
  - `validar(body)` retornando `(ok, erro, status)`
  - `insert_one(doc)` e `str(inserted_id)`
- **Como adaptar no exercício:**
  - trocar nomes de campos (`titulo`, `modo_preparo`, etc.) pelos do enunciado;
  - trocar lista `CATEGORIAS`;
  - manter estrutura de retorno com `{"dados": ...}`.

### 2) Erros 400 e 422

- **Fonte no caderno:** `validacao_receita.py` (`validar`, `_erro_tipo`)
- **Trechos-chave usados:**
  - obrigatórios faltando -> 400;
  - tipo inválido com `type(...) is not ...` -> 422;
  - valor fora da lista permitida -> 422.
- **Como adaptar no exercício:**
  - ajustar apenas nomes dos campos e mensagens/códigos esperados.

### 3) Listagem (GET coleção)

- **Fonte no caderno:** `app_receitas.py`, função `listar()`
- **Trechos-chave usados:**
  - `for d in col_receitas.find():`
  - montagem de `saida` com todos os campos;
  - retorno `{"dados": saida}`.
- **Como adaptar no exercício:**
  - trocar `col_receitas` pela coleção do projeto;
  - manter `_id` convertido em string.

### 4) Consulta por id + 404

- **Fonte no caderno:** `app_receitas.py`, função `detalhe()`
- **Trechos-chave usados:**
  - `ObjectId(rid)` em `try/except InvalidId`;
  - `find_one({"_id": oid})`;
  - 404 quando inválido ou não encontrado.
- **Como adaptar no exercício:**
  - trocar nome da rota e das variáveis, manter a lógica.

### 5) HATEOAS (links no JSON)

- **Fonte no caderno:** `validacao_receita.py`, funções `links_receita()` e `receita_json()`
- **Trechos-chave usados:**
  - `self`, `update`, `delete`, `collection`.
- **Como adaptar no exercício:**
  - trocar o prefixo `/receitas` pelo recurso da API do exercício.

---

## Frontend (React)

### 1) Formulário controlado e envio POST

- **Fonte no caderno:** `exemplos/react/FormReceita.jsx`
- **Trechos-chave usados:**
  - `useState` por campo;
  - `e.preventDefault()`;
  - `fetch(..., { method: 'POST', headers, body: JSON.stringify(payload) })`;
  - limpar campos após `res.ok`.
- **Como adaptar no exercício:**
  - trocar nome dos estados e chaves do `payload`;
  - trocar endpoint `/receitas`.

### 2) Converter input único para lista

- **Fonte no caderno:** `FormReceita.jsx` (`listaIng`)
- **Trecho-chave usado:**
  - string de input vira lista com 0 ou 1 elemento.
- **Como adaptar no exercício:**
  - mesma técnica para tags/palavras/itens quando o backend espera array.

### 3) Buscar e renderizar lista

- **Fonte no caderno:** `exemplos/react/AppReceitas.jsx`
- **Trechos-chave usados:**
  - `useEffect(() => { atualizar() }, [])`;
  - `setReceitas(json.dados || [])`;
  - `.map()` com `key={_id}`.
- **Como adaptar no exercício:**
  - trocar endpoint, nome do state e componente de card.

### 4) Card e `<ul><li>`

- **Fonte no caderno:** `exemplos/react/CardReceita.jsx`
- **Trechos-chave usados:**
  - exibir campos principais;
  - renderizar lista com `<ul><li>`.
- **Como adaptar no exercício:**
  - trocar labels e nome da propriedade de lista.

---

## Ordem prática para montar um exercício parecido

1. `notas/validacao-api.md` (relembrar critérios 400/422)  
2. `exemplos/flask/validacao_receita.py` (copiar padrão da validação)  
3. `exemplos/flask/app_receitas.py` (ligar validação + rotas + Mongo)  
4. `exemplos/react/FormReceita.jsx` (POST)  
5. `exemplos/react/AppReceitas.jsx` + `CardReceita.jsx` (GET + render)  
6. `exemplos/testes/requisicoes.http` para validar os endpoints
