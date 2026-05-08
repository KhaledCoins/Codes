/*
  Item.jsx — componente de exibição de UM item da coleção.

  Props:
    projeto: objeto com { _id, nome, descricao, tipo, tecnologias, links }

  Pontos de atenção:
    - Sempre proteja campos que podem ser undefined (ex: tecnologias)
    - Lista de tags/tecnologias → usar <ul> + <li> com .map()
    - key no .map() → use o índice ou um valor único do item
*/

export default function Item(props) {
  const p = props.projeto

  // Garante array mesmo se o campo vier ausente
  const tecnologias = p.tecnologias !== undefined ? p.tecnologias : []

  return (
    <div className="item-card">
      <p><b>Nome:</b> {p.nome}</p>
      <p><b>Descrição:</b> {p.descricao}</p>
      <p><b>Tipo:</b> {p.tipo}</p>
      <p><b>ID:</b> {p._id}</p>

      {/* Lista de tecnologias com <ul> e <li> */}
      <p><b>Tecnologias:</b></p>
      <ul>
        {tecnologias.map(function (tec, i) {
          return <li key={i}>{tec}</li>
        })}
      </ul>
    </div>
  )
}
