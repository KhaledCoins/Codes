# Como usar este repositório

## Ideia

É um **mini-projeto tema receitas** para fixar conceitos da disciplina:

- Backend grava documentos no Mongo
- Front lista e cadastra via `fetch`
- Validação de tipos com `type()` em Python

Se você fizer outro tema (lista de filmes, inventário, etc.), copie a **estrutura** e troque nomes de rota e campos.

## Leitura orientada para identificar adaptação

Se você quer enxergar claramente "o que eu peguei daqui e adaptei no exercício", use esta ordem:

1. `guias/MAPA-APROVEITAMENTO.md` (visão geral por tarefa);
2. `exemplos/flask/validacao_receita.py` (validação e erros);
3. `exemplos/flask/app_receitas.py` (rotas e Mongo);
4. `exemplos/react/FormReceita.jsx` (envio do formulário);
5. `exemplos/react/AppReceitas.jsx` + `CardReceita.jsx` (listagem na tela).

## Ordem para estudar

1. `notas/rest-http.md` e `notas/mongodb-pymongo.md`
2. `exemplos/mongo/crud_basico.py` (sem Flask)
3. `exemplos/flask/app_sem_banco.py` (só memória RAM)
4. `exemplos/flask/app_receitas.py` (completo)
5. `exemplos/react/AppReceitas.jsx`
6. `exemplos/testes/requisicoes.http`

## Estender

- Novo campo na receita → alterar `validacao_receita.py`, insert e respostas GET
- Nova categoria → lista `CATEGORIAS` no mesmo arquivo
- CSS → `estilo-receitas.css`

## Checklist rápido antes de adaptar

- backend: `guias/CHECKLIST-BACKEND.md`
- frontend: `guias/CHECKLIST-FRONTEND.md`
- conceitos: `notas/README.md`

## Git

Commits são do desenvolvimento real deste caderno. Não misturar com pastas de entrega da faculdade.
