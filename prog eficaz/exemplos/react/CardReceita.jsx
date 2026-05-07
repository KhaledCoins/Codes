export default function CardReceita({ receita }) {
  const ings = receita.ingredientes !== undefined ? receita.ingredientes : []

  return (
    <article className="card-receita">
      <p>
        <b>Título:</b> {receita.titulo}
      </p>
      <p>
        <b>Preparo:</b> {receita.modo_preparo}
      </p>
      <p>
        <b>Categoria:</b> {receita.categoria}
      </p>
      <p>
        <b>Id:</b> {receita._id}
      </p>
      <p>
        <b>Ingredientes:</b>
      </p>
      <ul>
        {ings.map(function (nome, i) {
          return <li key={i}>{nome}</li>
        })}
      </ul>
    </article>
  )
}
