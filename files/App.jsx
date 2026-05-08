/*
  App.jsx — componente raiz
  Responsabilidades:
    1. Buscar a lista de itens da API ao montar (useEffect)
    2. Passar callback para o Formulario atualizar a lista após cadastro
    3. Renderizar Formulario + lista de Itens
*/

import { useEffect, useState } from 'react'
import './App.css'
import Formulario from './Formulario.jsx'
import Item from './Item.jsx'

// URL base da API — ajuste conforme seu ambiente
const API = 'http://127.0.0.1:5000'

export default function App() {
  // Estado que guarda a lista de itens vindos da API
  const [itens, setItens] = useState([])

  // Função reutilizável para (re)carregar a lista
  function carregarItens() {
    fetch(API + '/projetos')
      .then(function (resposta) {
        return resposta.json()
      })
      .then(function (data) {
        // A API devolve { dados: [...] }
        if (data.dados) {
          setItens(data.dados)
        } else {
          setItens([])
        }
      })
  }

  // Busca os itens assim que o componente é montado
  // Dependência [] → executa apenas uma vez (equivalente ao componentDidMount)
  useEffect(function () {
    carregarItens()
  }, [])

  return (
    <div className="pagina">
      <h1>ProjectHub</h1>

      {/*
        Passa carregarItens como prop para que o Formulario
        possa atualizar a lista após um cadastro bem-sucedido.
      */}
      <Formulario depoisCadastrar={carregarItens} />

      <h2 className="subtitulo">Projetos cadastrados</h2>

      <div className="lista-itens">
        {itens.map(function (item) {
          // key deve ser único — usamos o _id gerado pelo MongoDB
          return <Item key={item._id} projeto={item} />
        })}
      </div>
    </div>
  )
}
