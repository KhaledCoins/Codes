# React — caderno de receitas

| Arquivo | Papel |
|---------|--------|
| `FormReceita.jsx` | Cadastro com `fetch` POST |
| `CardReceita.jsx` | Exibe uma receita + lista de ingredientes |
| `AppReceitas.jsx` | Página com form + GET na abertura |
| `estilo-receitas.css` | Estilos simples |

Importe no `App.jsx` de um projeto Vite para testar com a API em `app_receitas.py`.

## O que foi usado nos exercícios (frontend)

### Bloco 1: formulário controlado

- arquivo-base: `FormReceita.jsx`
- reaproveitamento comum:
  - `useState` por campo;
  - `onSubmit` com `preventDefault`;
  - montagem de `payload` com os campos da API;
  - limpeza do form após `res.ok`.

### Bloco 2: campo único virando lista

- arquivo-base: `FormReceita.jsx` (`listaIng`)
- reaproveitamento comum:
  - quando o backend espera lista, converter input string em array.

### Bloco 3: carregar dados na abertura

- arquivo-base: `AppReceitas.jsx`
- reaproveitamento comum:
  - `useEffect(..., [])` para GET inicial;
  - `setState(json.dados || [])`;
  - callback do form para atualizar lista.

### Bloco 4: renderização de lista e sublista

- arquivo-base: `CardReceita.jsx` + `AppReceitas.jsx`
- reaproveitamento comum:
  - `.map()` com `key={_id}`;
  - `<ul><li>` para ingredientes/tags/etc.

## Como adaptar rapidamente (receitas -> outro domínio)

1. troque endpoint `/receitas`;
2. troque nomes de states e chaves no `payload`;
3. troque labels no card;
4. mantenha o fluxo de submit -> limpar -> atualizar lista.
