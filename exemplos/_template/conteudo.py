# -*- coding: utf-8 -*-
"""Template de conteudo - edite SECOES, CONSIDERACOES e REFERENCIAS."""

FONTE_AUTORES = "Fonte: elaborado pelos autores (2026)."

SECOES = [
    {
        "titulo": "1 INTRODUCAO",
        "blocos": [
            {
                "tipo": "paragrafo",
                "texto": "Escreva aqui a introducao do trabalho em texto corrido.",
            },
        ],
    },
    {
        "titulo": "2 DESENVOLVIMENTO",
        "blocos": [
            {
                "tipo": "paragrafo",
                "texto": "Descreva o tema, metodo ou experimento.",
            },
            {
                "tipo": "quadro",
                "legenda": "Quadro 1 - Exemplo de tabela",
                "cabecalhos": ["Item", "Valor", "Unidade"],
                "linhas": [
                    ["Amostra A", "10,5", "mL"],
                    ["Amostra B", "12,0", "mL"],
                ],
                "fonte": FONTE_AUTORES,
            },
            {
                "tipo": "imagem",
                "paragrafo_antes": "Insira fotos, graficos ou diagramas:",
                "legenda": "Figura 1 - Exemplo de imagem",
                "arquivo": "imagens/exemplo.png",
                "largura_cm": 12,
                "fonte": FONTE_AUTORES,
            },
            {
                "tipo": "codigo",
                "paragrafo_antes": "Opcional: trecho de codigo (trabalhos de programacao):",
                "legenda": "Codigo 1 - Exemplo",
                "codigo": "print('Hello')",
                "fonte": "Fonte: codigo-fonte do projeto (2026).",
            },
            {
                "tipo": "figura",
                "paragrafo_antes": "Opcional: saida de terminal ou arquivo .txt:",
                "legenda": "Figura 2 - Saida do programa",
                "conteudo": "Programa executado com sucesso.",
                "fonte": "Fonte: captura de execucao (2026).",
            },
        ],
    },
]

CONSIDERACOES = [
    "Escreva aqui as consideracoes finais do trabalho.",
]

REFERENCIAS = [
    "ASSOCIACAO BRASILEIRA DE NORMAS TECNICAS. NBR 14724: informacao e documentacao - trabalhos academicos - apresentacao. Rio de Janeiro: ABNT, 2011.",
]
