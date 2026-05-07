"""
Função auxiliar: garantir que um campo do JSON é lista de strings.
Reaproveito em outros projetos com outro nome de campo.
"""


def lista_de_textos(payload, nome):
    if nome not in payload:
        return None
    valor = payload[nome]
    if type(valor) is not list:
        return "o campo " + nome + " precisa ser uma lista"
    for x in valor:
        if type(x) is not str:
            return "cada item de " + nome + " precisa ser texto"
    return None
