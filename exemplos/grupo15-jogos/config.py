# -*- coding: utf-8 -*-
"""Configuracao do relatorio - edite este arquivo para cada projeto."""

METADADOS = {
    "instituicao_linhas": [
        "UNIVERSIDADE SÃO FRANCISCO",
        "ENGENHARIA DA COMPUTAÇÃO",
    ],
    "autores": [
        "GABRIELA BENEDUZI",
        "DANILO AUGUSTO DO NASCIMENTO FORTES",
    ],
    "grupo": "GRUPO 15",
    "titulo": "RELATÓRIO DE TRABALHO PRÁTICO EM LINGUAGEM C",
    "subtitulo": "Gerador e Separador de Dados: Tema Jogos",
    "cidade": "Campinas",
    "ano": "2026",
    "nota_folha_rosto": (
        "Relatório apresentado à disciplina de Programação "
        "Estruturada do curso de Engenharia da Computação da "
        "Universidade São Francisco como requisito parcial "
        "para avaliação da atividade prática final."
    ),
    "arquivo_saida": "Grupo15_Relatorio.docx",
    "secoes_primarias_nova_pagina": True,
}

TITULOS_FINAIS = {
    "consideracoes": "6 CONSIDERAÇÕES FINAIS",
    "referencias": "7 REFERÊNCIAS",
}

# Paginas sao estimativas; ajuste se o documento mudar de tamanho.
SUMARIO = [
    ("1 INTRODUÇÃO", "4"),
    ("2 TEMA E CAMPOS UTILIZADOS", "5"),
    ("3 ESTRUTURAS DE DADOS UTILIZADAS", "6"),
    ("3.1 Struct Jogo", "6", 2),
    ("3.2 Vetores", "7", 2),
    ("3.3 Variáveis simples e ponteiros", "8", 2),
    ("4 PROGRAMA 1: GERADOR DE DADOS", "9"),
    ("4.1 Descrição", "9", 2),
    ("4.2 Funções", "9", 2),
    ("4.3 Trechos do código", "10", 2),
    ("4.4 Tela de execução e arquivo gerado", "12", 2),
    ("5 PROGRAMA 2: LEITOR E SEPARADOR DE DADOS", "13"),
    ("5.1 Descrição", "13", 2),
    ("5.2 Critérios de separação", "13", 2),
    ("5.3 Funções", "14", 2),
    ("5.4 Trechos do código", "15", 2),
    ("5.5 Tela de execução e arquivos gerados", "17", 2),
    ("6 CONSIDERAÇÕES FINAIS", "19"),
    ("7 REFERÊNCIAS", "20"),
]

# Normaliza sumario: aceita tuplas de 2 ou 3 elementos
def normalizar_sumario(itens):
    resultado = []
    for item in itens:
        if len(item) == 2:
            resultado.append({"titulo": item[0], "pagina": item[1], "nivel": 1})
        else:
            resultado.append({"titulo": item[0], "pagina": item[1], "nivel": item[2]})
    return resultado

SUMARIO = normalizar_sumario(SUMARIO)
