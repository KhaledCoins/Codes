import { useState } from 'react'

const API = 'http://127.0.0.1:5000'

export default function FormReceita({ quandoSalvar }) {
  const [titulo, setTitulo] = useState('')
  const [modoPreparo, setModoPreparo] = useState('')
  const [categoria, setCategoria] = useState('salgado')
  const [ingrediente, setIngrediente] = useState('')

  function salvar(e) {
    e.preventDefault()
    let listaIng = []
    if (ingrediente.trim() !== '') {
      listaIng = [ingrediente.trim()]
    }

    const payload = {
      titulo: titulo,
      modo_preparo: modoPreparo,
      categoria: categoria,
      ingredientes: listaIng,
    }

    fetch(API + '/receitas', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    }).then(function (res) {
      if (res.ok) {
        console.log('Receita gravada')
        setTitulo('')
        setModoPreparo('')
        setCategoria('salgado')
        setIngrediente('')
        if (typeof quandoSalvar === 'function') {
          quandoSalvar()
        }
      }
    })
  }

  return (
    <form className="form-receita" onSubmit={salvar}>
      <h2>Nova receita</h2>
      <div className="campo">
        <label>Título</label>
        <input value={titulo} onChange={(e) => setTitulo(e.target.value)} />
      </div>
      <div className="campo">
        <label>Modo de preparo</label>
        <textarea
          rows={4}
          value={modoPreparo}
          onChange={(e) => setModoPreparo(e.target.value)}
        />
      </div>
      <div className="campo">
        <label>Categoria</label>
        <select value={categoria} onChange={(e) => setCategoria(e.target.value)}>
          <option value="doce">doce</option>
          <option value="salgado">salgado</option>
          <option value="bebida">bebida</option>
          <option value="vegetariano">vegetariano</option>
        </select>
      </div>
      <div className="campo">
        <label>Ingrediente principal (um por vez)</label>
        <input
          value={ingrediente}
          onChange={(e) => setIngrediente(e.target.value)}
        />
      </div>
      <button type="submit">Salvar receita</button>
    </form>
  )
}
