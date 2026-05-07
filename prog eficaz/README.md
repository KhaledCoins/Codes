# Caderno de receitas — estudos de Programação Eficaz

API e front de **exemplo pessoal**: cadastro de receitas (titulo, modo de preparo, categoria, ingredientes).

Objetivo deste repositório: guardar os **padrões reutilizáveis** que normalmente aparecem nos exercícios da disciplina:

- API REST com Flask e JSON;
- persistência em MongoDB Atlas;
- validação com `type()` e erros 400/422;
- frontend React com `useState`, `useEffect` e `fetch`.

## O que foi reaproveitado nos exercícios

### Parte backend (equivalente ao que você aplicou no Ex. 1)

- Estrutura de rotas `POST` + `GET lista` + `GET por id`.
- Fluxo de validação em função separada.
- Conversão de `_id` para string no retorno.
- Tratamento de id inválido com `ObjectId` e 404.
- Links HATEOAS no JSON (`self`, `update`, `delete`, `collection`).

### Parte frontend (equivalente ao que você aplicou no Ex. 2)

- Formulário controlado (`useState` por campo).
- Envio via `fetch` POST com `Content-Type: application/json`.
- Limpar campos após sucesso.
- Buscar lista ao abrir a página (`useEffect`).
- Renderizar cards com `.map()` e lista `<ul><li>`.

> Mapa detalhado de "peguei daqui e adaptei assim":
> `guias/MAPA-APROVEITAMENTO.md`.

## Estrutura

| Pasta | Conteúdo |
|-------|----------|
| `notas/` | Resumos de REST, Mongo, validação e React |
| `guias/` | Como estudar, checklist e mapa de aproveitamento |
| `exemplos/flask/` | API `/receitas` completa + versão sem banco |
| `exemplos/mongo/` | Conexão Atlas e CRUD básico |
| `exemplos/react/` | Form, card, página e CSS |
| `exemplos/testes/` | Arquivo `.http` para testar endpoints |

## Rodar backend

```bash
cd exemplos/flask
pip install -r requirements.txt
# edite exemplos/mongo/conexao.py com sua URI
python app_receitas.py
```

## Rodar frontend (modo estudo)

Este repositório guarda snippets React. Para executar, copie os arquivos de `exemplos/react/` para um projeto Vite e importe `AppReceitas.jsx`.

## Banco usado no exemplo

- Database: `CadernoReceitas`
- Coleção: `receitas`
- Categorias de exemplo: `doce`, `salgado`, `bebida`, `vegetariano`
