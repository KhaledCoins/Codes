/*
  Formulario.jsx — formulário de cadastro de novo item.

  Props:
    depoisCadastrar: função chamada após cadastro bem-sucedido
                     (geralmente recarrega a lista no componente pai)

  Conceitos demonstrados:
    - Inputs controlados com useState (controlled components)
    - onSubmit com e.preventDefault() para evitar reload
    - fetch POST com JSON body e header Content-Type
    - Limpar formulário após sucesso
    - Passar lista com um único elemento quando o campo aceita array
*/

import { useState } from 'react'

const API = 'http://127.0.0.1:5000'

export default function Formulario({ depoisCadastrar }) {
  // ── Estado de cada campo ───────────────────────────────────────────────────
  const [nome,       setNome]       = useState('')
  const [descricao,  setDescricao]  = useState('')
  const [tipo,       setTipo]       = useState('web')   // valor padrão do select
  const [tecnologia, setTecnologia] = useState('')      // campo aceita apenas 1 item

  // ── Handler do formulário ──────────────────────────────────────────────────
  function cadastrar(e) {
    e.preventDefault()   // impede o reload padrão do form

    // Campo de lista com um único elemento
    // trim() remove espaços; se vazio, envia lista vazia
    let tecnologiasLista = []
    if (tecnologia.trim() !== '') {
      tecnologiasLista = [tecnologia.trim()]
    }

    const corpo = {
      nome:        nome,
      descricao:   descricao,
      tipo:        tipo,
      tecnologias: tecnologiasLista,   // sempre enviado como array
    }

    fetch(API + '/projetos', {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify(corpo),
    }).then(function (resposta) {
      if (resposta.ok) {
        console.log('Projeto cadastrado com sucesso')

        // Limpa todos os campos após cadastro bem-sucedido
        setNome('')
        setDescricao('')
        setTipo('web')
        setTecnologia('')

        // Avisa o pai para recarregar a lista
        if (typeof depoisCadastrar === 'function') {
          depoisCadastrar()
        }
      }
    })
  }

  // ── Renderização ──────────────────────────────────────────────────────────
  return (
    <form className="formulario" onSubmit={cadastrar}>
      <h2>Novo projeto</h2>

      {/* Campo texto simples */}
      <div className="campo">
        <label>Nome</label>
        <input
          value={nome}
          onChange={function (e) { setNome(e.target.value) }}
        />
      </div>

      {/* Textarea para textos longos */}
      <div className="campo">
        <label>Descrição</label>
        <textarea
          rows={4}
          value={descricao}
          onChange={function (e) { setDescricao(e.target.value) }}
        />
      </div>

      {/*
        Select com valores fixos (equivalente ao campo categoria/tipo).
        O value do select é controlado pelo estado; onChange atualiza o estado.
      */}
      <div className="campo">
        <label>Tipo</label>
        <select
          value={tipo}
          onChange={function (e) { setTipo(e.target.value) }}
        >
          <option value="web">web</option>
          <option value="mobile">mobile</option>
          <option value="dados">dados</option>
          <option value="automacao">automacao</option>
        </select>
      </div>

      {/*
        Campo de lista com apenas 1 item:
        o usuário digita uma string, mas o body envia um array de 1 elemento.
      */}
      <div className="campo">
        <label>Tecnologia principal</label>
        <input
          value={tecnologia}
          onChange={function (e) { setTecnologia(e.target.value) }}
          placeholder="ex: python"
        />
      </div>

      <button type="submit">Cadastrar</button>
    </form>
  )
}
