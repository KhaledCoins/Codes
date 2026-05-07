# React + API

## Estado do formulário

Um `useState` por input (`titulo`, `modoPreparo`, …).

## Ingrediente único → lista

```javascript
let listaIng = []
if (texto.trim() !== '') {
  listaIng = [texto.trim()]
}
```

## POST

```javascript
fetch('http://127.0.0.1:5000/receitas', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(payload),
})
```

## Carregar ao abrir

```javascript
useEffect(() => {
  fetch(...).then(r => r.json()).then(j => setReceitas(j.dados || []))
}, [])
```

Arquivos: `FormReceita.jsx`, `CardReceita.jsx`, `AppReceitas.jsx`.
