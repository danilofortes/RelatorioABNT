# -*- coding: utf-8 -*-
"""
Conteudo do relatorio - Grupo 15, tema Jogos.

Edite os textos e blocos abaixo. Cada secao usa uma lista de blocos
(paragrafo, quadro, codigo, figura, subsecao).
"""

FONTE_AUTORES = "Fonte: elaborado pelos autores (2026)."
FONTE_CODIGO = "Fonte: código-fonte do projeto (2026)."
FONTE_EXEC = "Fonte: captura de execução (2026)."
FONTE_ARQ = "Fonte: arquivo gerado pelo programa (2026)."

SECOES = [
    {
        "titulo": "1 INTRODUÇÃO",
        "blocos": [
            {"tipo": "paragrafo", "texto": (
                "Este relatório descreve dois programas em linguagem C desenvolvidos "
                "pelo Grupo 15 como projeto final da disciplina de Programação "
                "Estruturada. O tema do trabalho é Jogos, e cada registro representa "
                "um jogo com cinco campos: código, nome do jogo, categoria, nota e "
                "plataforma."
            )},
            {"tipo": "paragrafo", "texto": (
                "O primeiro programa, Grupo15_gerador.c, gera o arquivo jogos.txt com "
                "100 registros aleatórios. O segundo, Grupo15_separador.c, lê esse "
                "arquivo, exibe um resumo na tela e grava quatro arquivos de saída: "
                "notas_altas.txt, notas_baixas.txt, por_categoria.txt e "
                "resultado_numerico.txt."
            )},
            {"tipo": "paragrafo", "texto": (
                "Os programas usam struct, vetores, laços for, if/else, funções e "
                "comandos de arquivo (fopen, fprintf, fscanf, fgets, fclose). "
                "Ponteiros aparecem apenas para passar struct para função, como "
                "aprendido em aula."
            )},
            {"tipo": "paragrafo", "texto": (
                "O gerador monta nomes fictícios combinando prefixos e sufixos "
                "sorteados em vetores. O separador classifica os jogos por nota "
                "(corte em 7,0), agrupa por categoria e calcula médias gerais, "
                "por categoria e por plataforma no arquivo numérico."
            )},
        ],
    },
    {
        "titulo": "2 TEMA E CAMPOS UTILIZADOS",
        "blocos": [
            {"tipo": "paragrafo", "texto": (
                "O tema escolhido foi Jogos. Cada registro contém cinco campos, "
                "conforme o Quadro 1."
            )},
            {"tipo": "quadro", "legenda": "Quadro 1 - Campos do registro de jogo",
             "cabecalhos": ["Campo", "Tipo em C", "Descrição", "Exemplo"],
             "linhas": [
                 ["codigo", "int", "Identificador sequencial único", "1"],
                 ["jogo", "char[60]", "Nome do jogo (prefixo + sufixo)", "Dragon Rising"],
                 ["categoria", "char[30]", "Gênero do jogo", "Corrida"],
                 ["nota", "float", "Avaliação de 1.0 a 10.0", "6.9"],
                 ["plataforma", "char[20]", "Plataforma de lançamento", "PC"],
             ], "fonte": FONTE_AUTORES},
            {"tipo": "paragrafo", "texto": (
                "O arquivo jogos.txt usa ponto e vírgula como separador e começa "
                "com uma linha de cabeçalho. Trecho inicial de uma execução:"
            )},
            {"tipo": "codigo", "legenda": "Exemplo de registros em jogos.txt",
             "codigo": (
                 "codigo;jogo;categoria;nota;plataforma\n"
                 "1;Dragon Rising;Corrida;6.9;PC\n"
                 "2;Final Legacy;RPG;8.6;Xbox\n"
                 "3;Cyber Empire;FPS;5.2;Xbox\n"
                 "4;Dragon Empire;Aventura;7.7;Xbox\n"
                 "5;Dragon Strike;Aventura;2.9;Switch"
             ), "fonte": FONTE_ARQ},
            {"tipo": "paragrafo", "texto": (
                "O código é sequencial de 1 a 100. O nome do jogo combina um "
                "prefixo e um sufixo sorteados. A nota varia de 1,0 a 10,0 com "
                "uma casa decimal. As categorias possíveis são RPG, FPS, Aventura, "
                "Esportes, Corrida e Puzzle. As plataformas são PC, PS5, Xbox, "
                "Switch e Mobile."
            )},
        ],
    },
    {
        "titulo": "3 ESTRUTURAS DE DADOS UTILIZADAS",
        "blocos": [
            {"tipo": "paragrafo", "texto": (
                "As estruturas usadas nos dois programas estão descritas abaixo, "
                "com trechos reais do código."
            )},
            {"tipo": "subsecao", "titulo": "3.1 Struct Jogo", "nivel": 2, "blocos": [
                {"tipo": "paragrafo", "texto": (
                    "A struct Jogo reúne os cinco campos de cada registro. Os dois "
                    "programas usam a mesma declaração, sem typedef."
                )},
                {"tipo": "codigo", "legenda": "Código 1 - Declaração da struct Jogo",
                 "codigo": (
                     "struct Jogo {\n"
                     "    int codigo;\n"
                     "    char jogo[60];\n"
                     "    char categoria[30];\n"
                     "    float nota;\n"
                     "    char plataforma[20];\n"
                     "};"
                 ), "fonte": FONTE_CODIGO},
            ]},
            {"tipo": "subsecao", "titulo": "3.2 Vetores", "nivel": 2, "blocos": [
                {"tipo": "paragrafo", "texto": (
                    "O gerador guarda prefixos, sufixos, categorias e plataformas em "
                    "vetores de char. O sorteio com rand() escolhe índices e monta "
                    "cada registro sem entrada manual."
                )},
                {"tipo": "codigo", "legenda": "Código 2 - Vetores de strings (Grupo15_gerador.c)",
                 "codigo": (
                     "char prefixos[10][15] = {\n"
                     "    \"Shadow\", \"Dragon\", \"Star\", \"Dark\", \"Final\",\n"
                     "    \"Cyber\", \"Neon\", \"Storm\", \"Lost\", \"Thunder\"\n"
                     "};\n"
                     "\n"
                     "char categorias[6][15] = {\n"
                     "    \"RPG\", \"FPS\", \"Aventura\", \"Esportes\", \"Corrida\", \"Puzzle\"\n"
                     "};"
                 ), "fonte": FONTE_CODIGO},
                {"tipo": "paragrafo", "texto": (
                    "O separador lê até 200 registros em um vetor de struct Jogo. "
                    "Esse vetor fica em memória enquanto as funções de separação "
                    "percorrem os dados."
                )},
                {"tipo": "codigo", "legenda": "Código 3 - Vetor de structs (Grupo15_separador.c)",
                 "codigo": (
                     "struct Jogo registros[200];\n"
                     "int total = lerArquivo(registros);"
                 ), "fonte": FONTE_CODIGO},
            ]},
            {"tipo": "subsecao", "titulo": "3.3 Variáveis simples e ponteiros", "nivel": 2, "blocos": [
                {"tipo": "paragrafo", "texto": (
                    "Variáveis int e float servem como contadores, somadores e índices. "
                    "O ponteiro struct Jogo *j aparece em gerarJogo para preencher a "
                    "struct passada pelo main. FILE *fp aponta para o arquivo aberto "
                    "com fopen."
                )},
            ]},
        ],
    },
    {
        "titulo": "4 PROGRAMA 1: GERADOR DE DADOS",
        "blocos": [
            {"tipo": "subsecao", "titulo": "4.1 Descrição", "nivel": 2, "blocos": [
                {"tipo": "paragrafo", "texto": (
                    "Grupo15_gerador.c grava jogos.txt com 100 linhas de dados mais "
                    "o cabeçalho. Os valores de cada campo são sorteados com rand() "
                    "a partir dos vetores de prefixos, sufixos, categorias e plataformas."
                )},
                {"tipo": "paragrafo", "texto": (
                    "O main abre o arquivo, escreve o cabeçalho, executa um for de 1 "
                    "a 100 chamando gerarJogo e escreverRegistro, e fecha o arquivo "
                    "com fclose."
                )},
            ]},
            {"tipo": "subsecao", "titulo": "4.2 Funções", "nivel": 2, "blocos": [
                {"tipo": "quadro", "legenda": "Quadro 2 - Funções do Grupo15_gerador.c",
                 "cabecalhos": ["Função", "Retorno", "Descrição"],
                 "linhas": [
                     ["main", "int", "Abre jogos.txt e executa o laço de geração."],
                     ["gerarJogo", "void", "Preenche a struct com código, nome, categoria, plataforma e nota."],
                     ["escreverRegistro", "void", "Grava um registro no formato CSV com ponto e vírgula."],
                 ], "fonte": FONTE_AUTORES},
            ]},
            {"tipo": "subsecao", "titulo": "4.3 Trechos do código", "nivel": 2, "blocos": [
                {"tipo": "subsecao", "titulo": "4.3.1 Geração da nota", "nivel": 3, "blocos": [
                    {"tipo": "paragrafo", "texto": (
                        "A nota usa ((rand() % 91) + 10) / 10.0, produzindo valores "
                        "entre 1,0 e 10,0 com uma casa decimal."
                    )},
                    {"tipo": "codigo", "legenda": "Código 4 - Cálculo da nota",
                     "codigo": "j->nota = ((rand() % 91) + 10) / 10.0;", "fonte": FONTE_CODIGO},
                ]},
                {"tipo": "subsecao", "titulo": "4.3.2 Geração de um jogo completo", "nivel": 3, "blocos": [
                    {"tipo": "paragrafo", "texto": (
                        "gerarJogo sorteia prefixo e sufixo, monta o nome com sprintf, "
                        "copia categoria e plataforma com strcpy e calcula a nota."
                    )},
                    {"tipo": "codigo", "legenda": "Código 5 - Função gerarJogo",
                     "codigo": (
                         "void gerarJogo(struct Jogo *j, int codigo) {\n"
                         "    j->codigo = codigo;\n"
                         "    p = rand() % 10;\n"
                         "    s = rand() % 10;\n"
                         "    sprintf(j->jogo, \"%s %s\", prefixos[p], sufixos[s]);\n"
                         "    strcpy(j->categoria, categorias[rand() % 6]);\n"
                         "    strcpy(j->plataforma, plataformas[rand() % 5]);\n"
                         "    j->nota = ((rand() % 91) + 10) / 10.0;\n"
                         "}"
                     ), "fonte": FONTE_CODIGO},
                ]},
                {"tipo": "subsecao", "titulo": "4.3.3 Laço principal e escrita no arquivo", "nivel": 3, "blocos": [
                    {"tipo": "paragrafo", "texto": (
                        "O laço for no main gera os 100 registros. A cada iteração, "
                        "gerarJogo recebe o endereço da struct com &j."
                    )},
                    {"tipo": "codigo", "legenda": "Código 6 - Laço de geração no main",
                     "codigo": (
                         "for (i = 1; i <= 100; i++) {\n"
                         "    gerarJogo(&j, i);\n"
                         "    escreverRegistro(fp, j);\n"
                         "}"
                     ), "fonte": FONTE_CODIGO},
                    {"tipo": "paragrafo", "texto": (
                        "escreverRegistro usa fprintf com %.1f na nota e ponto e vírgula "
                        "entre os campos."
                    )},
                    {"tipo": "codigo", "legenda": "Código 7 - Função escreverRegistro",
                     "codigo": (
                         "void escreverRegistro(FILE *fp, struct Jogo j) {\n"
                         "    fprintf(fp, \"%d;%s;%s;%.1f;%s\\n\",\n"
                         "            j.codigo, j.jogo, j.categoria, j.nota, j.plataforma);\n"
                         "}"
                     ), "fonte": FONTE_CODIGO},
                ]},
            ]},
            {"tipo": "subsecao", "titulo": "4.4 Tela de execução e arquivo gerado", "nivel": 2, "blocos": [
                {"tipo": "figura", "paragrafo_antes": "Saída do terminal após executar Grupo15_gerador.exe:",
                 "legenda": "Figura 1 - Saída do Grupo15_gerador.c no terminal",
                 "conteudo": (
                     "Arquivo 'jogos.txt' gerado com sucesso!\n"
                     "Total de registros: 100"
                 ), "fonte": FONTE_EXEC},
                {"tipo": "figura", "paragrafo_antes": "Primeiras linhas do jogos.txt gerado:",
                 "legenda": "Figura 2 - Primeiros registros do arquivo jogos.txt",
                 "conteudo": (
                     "codigo;jogo;categoria;nota;plataforma\n"
                     "1;Dragon Rising;Corrida;6.9;PC\n"
                     "2;Final Legacy;RPG;8.6;Xbox\n"
                     "3;Cyber Empire;FPS;5.2;Xbox\n"
                     "4;Dragon Empire;Aventura;7.7;Xbox\n"
                     "5;Dragon Strike;Aventura;2.9;Switch\n"
                     "6;Star Wars;Aventura;6.7;Switch\n"
                     "7;Storm Arena;Puzzle;5.9;Switch\n"
                     "8;Star Rising;FPS;7.6;PC"
                 ), "fonte": FONTE_ARQ},
            ]},
        ],
    },
    {
        "titulo": "5 PROGRAMA 2: LEITOR E SEPARADOR DE DADOS",
        "blocos": [
            {"tipo": "subsecao", "titulo": "5.1 Descrição", "nivel": 2, "blocos": [
                {"tipo": "paragrafo", "texto": (
                    "Grupo15_separador.c lê jogos.txt, guarda os registros em memória, "
                    "mostra estatísticas na tela e grava quatro arquivos conforme "
                    "critérios definidos no enunciado."
                )},
            ]},
            {"tipo": "subsecao", "titulo": "5.2 Critérios de separação", "nivel": 2, "blocos": [
                {"tipo": "paragrafo", "texto": (
                    "O Quadro 3 resume os quatro arquivos gerados e o critério de "
                    "cada um. O corte de nota 7,0 separa jogos bem e mal avaliados."
                )},
                {"tipo": "quadro", "legenda": "Quadro 3 - Arquivos de saída do Grupo15_separador.c",
                 "cabecalhos": ["Arquivo", "Critério de separação", "Conteúdo"],
                 "linhas": [
                     ["notas_altas.txt", "nota >= 7,0", "Jogos considerados bem avaliados"],
                     ["notas_baixas.txt", "nota < 7,0", "Jogos considerados mal avaliados"],
                     ["por_categoria.txt", "agrupamento por categoria", "Todos os jogos listados por gênero"],
                     ["resultado_numerico.txt", "cálculo estatístico", "Médias, maior/menor nota e percentuais"],
                 ], "fonte": FONTE_AUTORES},
                {"tipo": "paragrafo", "texto": (
                    "O arquivo resultado_numerico.txt concentra os cálculos numéricos "
                    "exigidos no enunciado: média geral, maior e menor nota, percentual "
                    "de jogos acima e abaixo de 7,0, média por categoria e média por "
                    "plataforma."
                )},
            ]},
            {"tipo": "subsecao", "titulo": "5.3 Funções", "nivel": 2, "blocos": [
                {"tipo": "quadro", "legenda": "Quadro 4 - Funções do Grupo15_separador.c",
                 "cabecalhos": ["Função", "Retorno", "Descrição"],
                 "linhas": [
                     ["main", "int", "Lê o arquivo e chama as funções de separação."],
                     ["lerArquivo", "int", "Abre jogos.txt, descarta cabeçalho e lê com fscanf."],
                     ["exibirResumo", "void", "Imprime total, média, maior, menor nota e contagem por faixa."],
                     ["separarPorNota", "void", "Grava notas_altas.txt e notas_baixas.txt."],
                     ["agruparPorCategoria", "void", "Lista jogos agrupados por categoria."],
                     ["gerarEstatisticas", "void", "Grava resultado_numerico.txt com médias e percentuais."],
                 ], "fonte": FONTE_AUTORES},
            ]},
            {"tipo": "subsecao", "titulo": "5.4 Trechos do código", "nivel": 2, "blocos": [
                {"tipo": "subsecao", "titulo": "5.4.1 Leitura com fscanf", "nivel": 3, "blocos": [
                    {"tipo": "paragrafo", "texto": (
                        "lerArquivo descarta a primeira linha com fgets e lê os campos com "
                        "fscanf. O laço while continua enquanto fscanf retornar 5."
                    )},
                    {"tipo": "codigo", "legenda": "Código 8 - Leitura com fscanf",
                     "codigo": (
                         "fgets(cabecalho, 200, fp);\n"
                         "n = 0;\n"
                         "while (fscanf(fp, \"%d;%59[^;];%29[^;];%f;%19[^\\n]\\n\",\n"
                         "              &r[n].codigo, r[n].jogo, r[n].categoria,\n"
                         "              &r[n].nota, r[n].plataforma) == 5) {\n"
                         "    n++;\n"
                         "}"
                     ), "fonte": FONTE_CODIGO},
                ]},
                {"tipo": "subsecao", "titulo": "5.4.2 Separação por nota", "nivel": 3, "blocos": [
                    {"tipo": "paragrafo", "texto": (
                        "separarPorNota percorre o vetor e usa if/else: nota >= 7,0 vai "
                        "para notas_altas.txt; caso contrário, vai para notas_baixas.txt."
                    )},
                    {"tipo": "codigo", "legenda": "Código 9 - Separação com if/else",
                     "codigo": (
                         "if (r[i].nota >= 7.0) {\n"
                         "    fprintf(fa, \"%d;%s;%s;%.1f;%s\\n\", ...);\n"
                         "    qtdAltas = qtdAltas + 1;\n"
                         "} else {\n"
                         "    fprintf(fb, \"%d;%s;%s;%.1f;%s\\n\", ...);\n"
                         "    qtdBaixas = qtdBaixas + 1;\n"
                         "}"
                     ), "fonte": FONTE_CODIGO},
                ]},
                {"tipo": "subsecao", "titulo": "5.4.3 Agrupamento por categoria", "nivel": 3, "blocos": [
                    {"tipo": "paragrafo", "texto": (
                        "agruparPorCategoria percorre as seis categorias fixas do vetor "
                        "categorias e imprime um bloco para cada uma, usando strcmp."
                    )},
                    {"tipo": "codigo", "legenda": "Código 10 - Função agruparPorCategoria",
                     "codigo": (
                         "for (c = 0; c < 6; c++) {\n"
                         "    fprintf(fp, \"--- %s ---\\n\", categorias[c]);\n"
                         "    for (i = 0; i < n; i++) {\n"
                         "        if (strcmp(r[i].categoria, categorias[c]) == 0) {\n"
                         "            fprintf(fp, \"%d;%s;%.1f;%s\\n\", ...);\n"
                         "        }\n"
                         "    }\n"
                         "}"
                     ), "fonte": FONTE_CODIGO},
                ]},
                {"tipo": "subsecao", "titulo": "5.4.4 Cálculo estatístico", "nivel": 3, "blocos": [
                    {"tipo": "paragrafo", "texto": (
                        "gerarEstatisticas soma as notas, calcula média geral, maior, "
                        "menor, percentuais de altas e baixas, e repete o cálculo de "
                        "média para cada categoria e cada plataforma."
                    )},
                    {"tipo": "codigo", "legenda": "Código 11 - Função gerarEstatisticas",
                     "codigo": (
                         "fprintf(fp, \"Media geral das notas     : %.2f\\n\", mediaGeral);\n"
                         "fprintf(fp, \"Jogos bem avaliados (>=7.0): %d (%.1f%%)\\n\",\n"
                         "        altas, (altas * 100.0) / n);\n"
                         "...\n"
                         "fprintf(fp, \"%-12s -> %d jogos | Media: %.2f\\n\",\n"
                         "        categorias[c], qtd, somaCat / qtd);"
                     ), "fonte": FONTE_CODIGO},
                ]},
            ]},
            {"tipo": "subsecao", "titulo": "5.5 Tela de execução e arquivos gerados", "nivel": 2, "blocos": [
                {"tipo": "figura", "paragrafo_antes": "Saída do terminal após executar Grupo15_separador.exe:",
                 "legenda": "Figura 3 - Saída do Grupo15_separador.c no terminal",
                 "conteudo": (
                     "=== GRUPO 15 - SEPARADOR DE JOGOS ===\n"
                     "Total de jogos   : 100\n"
                     "Media geral      : 5.32\n"
                     "Maior nota       : 10.0\n"
                     "Menor nota       : 1.0\n"
                     "Notas altas >=7.0 : 33\n"
                     "Notas baixas <7.0: 67\n"
                     "=====================================\n"
                     "Arquivo 'notas_altas.txt' gerado com 33 jogos.\n"
                     "Arquivo 'notas_baixas.txt' gerado com 67 jogos.\n"
                     "Arquivo 'por_categoria.txt' gerado.\n"
                     "Arquivo 'resultado_numerico.txt' gerado."
                 ), "fonte": FONTE_EXEC},
                {"tipo": "figura", "paragrafo_antes": "Trecho de notas_altas.txt:",
                 "legenda": "Figura 4 - Conteúdo de notas_altas.txt",
                 "conteudo": (
                     "=== JOGOS BEM AVALIADOS (nota >= 7.0) ===\n"
                     "2;Final Legacy;RPG;8.6;Xbox\n"
                     "4;Dragon Empire;Aventura;7.7;Xbox\n"
                     "8;Star Rising;FPS;7.6;PC\n"
                     "...\n"
                     "Total: 33 jogos"
                 ), "fonte": FONTE_ARQ},
                {"tipo": "figura", "paragrafo_antes": "Trecho de por_categoria.txt (categoria RPG):",
                 "legenda": "Figura 5 - Conteúdo de por_categoria.txt",
                 "conteudo": (
                     "=== JOGOS AGRUPADOS POR CATEGORIA ===\n"
                     "\n"
                     "--- RPG ---\n"
                     "2;Final Legacy;8.6;Xbox\n"
                     "...\n"
                     "Subtotal: 15 jogo(s)"
                 ), "fonte": FONTE_ARQ},
                {"tipo": "figura", "paragrafo_antes": "Conteúdo de resultado_numerico.txt:",
                 "legenda": "Figura 6 - Conteúdo de resultado_numerico.txt",
                 "conteudo": (
                     "=== RESULTADO NUMERICO - ANALISE DE JOGOS ===\n"
                     "\n"
                     "--- ESTATISTICAS GERAIS ---\n"
                     "Total de jogos analisados : 100\n"
                     "Media geral das notas     : 5.32\n"
                     "Jogos bem avaliados (>=7.0): 33 (33.0%)\n"
                     "Jogos mal avaliados (<7.0) : 67 (67.0%)\n"
                     "\n"
                     "--- MEDIA DE NOTAS POR CATEGORIA ---\n"
                     "RPG          -> 15 jogos | Media: 4.97\n"
                     "FPS          -> 12 jogos | Media: 5.98"
                 ), "fonte": FONTE_ARQ},
            ]},
        ],
    },
]

CONSIDERACOES = [
    (
        "Grupo15_gerador.c e Grupo15_separador.c atendem ao enunciado: "
        "100 registros gerados, leitura do arquivo, resumo na tela, "
        "quatro arquivos de saída e cálculos numéricos em "
        "resultado_numerico.txt."
    ),
    (
        "O código segue o que foi visto em aula: struct sem typedef, "
        "vetores fixos, funções separadas, if/else, for, strcmp, strcpy, "
        "sprintf, fopen, fprintf, fscanf e fgets."
    ),
    (
        "O corte em 7,0 para notas altas e baixas facilita a leitura dos "
        "dados. O arquivo por_categoria.txt mostra a distribuição dos jogos "
        "entre os seis gêneros sorteados pelo gerador."
    ),
    (
        "Uma limitação do projeto é a duplicação das listas de categorias "
        "e plataformas nos dois programas. Se novos gêneros forem "
        "adicionados, será preciso alterar os dois arquivos .c."
    ),
    (
        "O vetor registros[200] comporta até 200 jogos, mais que os 100 "
        "exigidos. Para arquivos maiores, seria necessário aumentar esse "
        "limite ou usar alocação dinâmica, tema ainda não visto em aula."
    ),
]

REFERENCIAS = [
    (
        "ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. NBR 14724: informação "
        "e documentação - trabalhos acadêmicos - apresentação. Rio de "
        "Janeiro: ABNT, 2011."
    ),
    (
        "UNIVERSIDADE SÃO FRANCISCO. Projeto final: gerador e organizador "
        "de dados em C. Disciplina Programação Estruturada, Engenharia da "
        "Computação, 2026. Material didático (arquivo programacao "
        "estruturada proj26.pdf)."
    ),
]
