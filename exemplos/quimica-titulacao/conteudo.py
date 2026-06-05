# -*- coding: utf-8 -*-
"""Conteudo do relatorio de quimica - titulacao acido-base."""

FONTE_AUTORES = "Fonte: elaborado pelos autores (2026)."
FONTE_LAB = "Fonte: registro do laboratorio (2026)."

SECOES = [
    {
        "titulo": "1 INTRODUCAO",
        "blocos": [
            {
                "tipo": "paragrafo",
                "texto": (
                    "A titulacao acido-base e um metodo quantitativo usado para "
                    "determinar a concentracao de uma solucao desconhecida a partir "
                    "da reacao com uma solucao padrao de concentracao conhecida. "
                    "Neste experimento, titulou-se uma solucao de acido cloridrico (HCl) "
                    "com hidroxido de sodio (NaOH) 0,1 mol/L, usando fenolftaleina como "
                    "indicador visual do ponto de equivalencia."
                ),
            },
            {
                "tipo": "paragrafo",
                "texto": (
                    "O objetivo foi calcular a molaridade do HCl a partir do volume "
                    "de NaOH consumido e discutir possiveis fontes de erro experimental."
                ),
            },
        ],
    },
    {
        "titulo": "2 MATERIAL E METODOS",
        "blocos": [
            {
                "tipo": "subsecao",
                "titulo": "2.1 Reagentes e equipamentos",
                "nivel": 2,
                "blocos": [
                    {
                        "tipo": "paragrafo",
                        "texto": (
                            "Utilizaram-se bureta de 50 mL, pipeta volumetrica de 25 mL, "
                            "Erlenmeyer de 250 mL, funil, agitador magnetico, solucao de "
                            "NaOH 0,1 mol/L, solucao de HCl de concentracao desconhecida "
                            "e fenolftaleina 1%."
                        ),
                    },
                    {
                        "tipo": "imagem",
                        "paragrafo_antes": "Montagem basica do sistema de titulacao:",
                        "legenda": "Figura 1 - Montagem da bureta e Erlenmeyer",
                        "arquivo": "imagens/montagem_bureta.png",
                        "largura_cm": 12,
                        "fonte": FONTE_LAB,
                    },
                    {
                        "tipo": "quadro",
                        "legenda": "Quadro 1 - Reagentes utilizados",
                        "cabecalhos": ["Reagente", "Concentracao", "Funcao"],
                        "linhas": [
                            ["HCl", "Desconhecida", "Analito"],
                            ["NaOH", "0,1 mol/L", "Titulante"],
                            ["Fenolftaleina", "1%", "Indicador"],
                        ],
                        "fonte": FONTE_AUTORES,
                    },
                ],
            },
            {
                "tipo": "subsecao",
                "titulo": "2.2 Procedimento experimental",
                "nivel": 2,
                "blocos": [
                    {
                        "tipo": "paragrafo",
                        "texto": (
                            "Transferiu-se 25,0 mL de HCl para o Erlenmeyer com pipeta "
                            "volumetrica. Adicionaram-se duas gotas de fenolftaleina. "
                            "O NaOH foi adicionado lentamente da bureta, com agitacao "
                            "constante, ate a persistencia da coloracao rosa por 30 segundos."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "titulo": "3 RESULTADOS",
        "blocos": [
            {
                "tipo": "subsecao",
                "titulo": "3.1 Dados da titulacao",
                "nivel": 2,
                "blocos": [
                    {
                        "tipo": "quadro",
                        "legenda": "Quadro 2 - Volumes de NaOH consumidos",
                        "cabecalhos": ["Leitura", "Volume NaOH (mL)"],
                        "linhas": [
                            ["1", "23,40"],
                            ["2", "23,55"],
                            ["3", "23,48"],
                        ],
                        "fonte": FONTE_LAB,
                    },
                    {
                        "tipo": "paragrafo",
                        "texto": (
                            "O volume medio de NaOH foi 23,48 mL. Pela estequiometria "
                            "1:1 entre HCl e NaOH, a concentracao calculada do acido foi "
                            "0,094 mol/L."
                        ),
                    },
                ],
            },
            {
                "tipo": "subsecao",
                "titulo": "3.2 Grafico e curva de titulacao",
                "nivel": 2,
                "blocos": [
                    {
                        "tipo": "paragrafo",
                        "texto": (
                            "A curva de titulacao relaciona o pH ao volume de titulante "
                            "adicionado. O salto brusco de pH proximo ao ponto de "
                            "equivalencia confirma a reacao completa do acido com a base."
                        ),
                    },
                    {
                        "tipo": "imagem",
                        "legenda": "Figura 2 - Curva de titulacao acido-base",
                        "arquivo": "imagens/curva_titulacao.png",
                        "largura_cm": 14,
                        "fonte": FONTE_AUTORES,
                    },
                ],
            },
        ],
    },
    {
        "titulo": "4 DISCUSSAO",
        "blocos": [
            {
                "tipo": "paragrafo",
                "texto": (
                    "Os tres ensaios apresentaram variacao maxima de 0,15 mL entre "
                    "leituras, indicando boa reprodutibilidade. Pequenas diferencas "
                    "podem ser atribuidas a leitura parcial da gota na ponta da bureta "
                    "e a variacao na percepcao da cor do indicador."
                ),
            },
            {
                "tipo": "paragrafo",
                "texto": (
                    "A concentracao obtida (0,094 mol/L) esta coerente com a solucao "
                    "preparada pelo laboratorio (aproximadamente 0,10 mol/L), dentro "
                    "da margem esperada para o nivel da pratica."
                ),
            },
        ],
    },
]

CONSIDERACOES = [
    (
        "A titulacao permitiu estimar a concentracao do HCl de forma pratica e "
        "com resultado consistente entre repeticoes. O uso de indicador adequado "
        "e a leitura cuidadosa da bureta foram essenciais para a precisao."
    ),
    (
        "Como melhoria, poderia ser utilizado pH-metro para localizar o ponto "
        "de equivalencia com maior exatidao, reduzindo a subjetividade da cor "
        "da fenolftaleina."
    ),
]

REFERENCIAS = [
    (
        "ATKINS, Peter; JONES, Loretta. Principios de quimica: questionando a "
        "vida moderna e a ciencia ambiental. 5. ed. Porto Alegre: Bookman, 2013."
    ),
    (
        "ASSOCIACAO BRASILEIRA DE NORMAS TECNICAS. NBR 14724: informacao e "
        "documentacao - trabalhos academicos - apresentacao. Rio de Janeiro: ABNT, 2011."
    ),
]
