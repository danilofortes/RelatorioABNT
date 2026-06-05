# -*- coding: utf-8 -*-
"""Exemplo: relatorio de laboratorio de quimica (titulacao acido-base)."""

METADADOS = {
    "instituicao_linhas": [
        "UNIVERSIDADE SAO FRANCISCO",
        "QUIMICA GERAL EXPERIMENTAL",
    ],
    "autores": [
        "MARIA SILVA",
        "JOAO SANTOS",
    ],
    "grupo": "GRUPO 3",
    "titulo": "RELATORIO DE PRATICA DE LABORATORIO",
    "subtitulo": "Titulacao acido-base: determinacao da concentracao de HCl",
    "cidade": "Campinas",
    "ano": "2026",
    "nota_folha_rosto": (
        "Relatorio apresentado a disciplina de Quimica Geral Experimental "
        "como requisito parcial para avaliacao da pratica de laboratorio."
    ),
    "arquivo_saida": "Relatorio_Quimica.docx",
    "secoes_primarias_nova_pagina": True,
}

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
    ("2 MATERIAL E METODOS", "5"),
    ("2.1 Reagentes e equipamentos", "5", 2),
    ("2.2 Procedimento experimental", "6", 2),
    ("3 RESULTADOS", "7"),
    ("3.1 Dados da titulacao", "7", 2),
    ("3.2 Grafico e curva de titulacao", "8", 2),
    ("4 DISCUSSAO", "9"),
    ("5 CONSIDERACOES FINAIS", "10"),
    ("6 REFERENCIAS", "11"),
])
