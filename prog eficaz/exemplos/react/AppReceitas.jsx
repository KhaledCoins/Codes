import { useEffect, useState } from 'react'
import FormReceita from './FormReceita.jsx'
import CardReceita from './CardReceita.jsx'
import './estilo-receitas.css'

const API = 'http://127.0.0.1:5000'

export default function AppReceitas() {
  const [receitas, setReceitas] = useState([])

  function atualizar() {
    fetch(API + '/receitas')
      .then((r) => r.json())
      .then((json) => {
        setReceitas(json.dados || [])
      })
  }

  useEffect(() => {
    atualizar()
  }, [])

  return (
    <div className="pagina-receitas">
      <h1>Caderno de receitas</h1>
      <FormReceita quandoSalvar={atualizar} />
      <h2 className="sub">Receitas salvas</h2>
      <div className="grade">
        {receitas.map((r) => (
          <CardReceita key={r._id} receita={r} />
        ))}
      </div>
    </div>
  )
}
