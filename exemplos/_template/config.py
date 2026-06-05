# -*- coding: utf-8 -*-
"""Template de configuracao - copie esta pasta para iniciar um novo relatorio."""

METADADOS = {
    "instituicao_linhas": [
        "UNIVERSIDADE ...",
        "NOME DO CURSO OU DISCIPLINA",
    ],
    "autores": [
        "NOME DO ALUNO 1",
        "NOME DO ALUNO 2",
    ],
    "grupo": "",  # opcional; deixe "" se nao usar
    "titulo": "RELATORIO DE TRABALHO",
    "subtitulo": "Titulo ou tema do trabalho",
    "cidade": "Campinas",
    "ano": "2026",
    "nota_folha_rosto": (
        "Relatorio apresentado a disciplina de ... como requisito parcial "
        "para avaliacao."
    ),
    "arquivo_saida": "Relatorio.docx",
    "secoes_primarias_nova_pagina": True,
}

# Titulos das secoes finais (ajuste numeracao conforme seu sumario)
TITULOS_FINAIS = {
    "consideracoes": "5 CONSIDERACOES FINAIS",
    "referencias": "6 REFERENCIAS",
}


def normalizar_sumario(itens):
    resultado = []
    for item in itens:
        if len(item) == 2:
            resultado.append({"titulo": item[0], "pagina": item[1], "nivel": 1})
        else:
            resultado.append({"titulo": item[0], "pagina": item[1], "nivel": item[2]})
    return resultado


SUMARIO = normalizar_sumario([
    ("1 INTRODUCAO", "4"),
    ("2 DESENVOLVIMENTO", "5"),
    ("5 CONSIDERACOES FINAIS", "10"),
    ("6 REFERENCIAS", "11"),
])
