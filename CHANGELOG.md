# Changelog

## [1.2.0] - 2026-06-05

### Changed

- Espaçamento alinhado à NBR 14724: **18 pt** (1,5 linhas) antes/depois de subseções e após títulos primários
- Seções primárias (1, 2, 3…) iniciam em **página nova** por padrão
- Considerações finais e referências sempre em página nova
- Opção `secoes_primarias_nova_pagina: False` em `METADADOS` para relatórios curtos

## [1.1.0] - 2026-06-05

### Added

- Bloco `imagem` para inserir PNG, JPG e outros formatos no relatório
- Campo `arquivo` também aceito em blocos `figura`
- Parâmetros `largura_cm` e `altura_cm` para redimensionar imagens
- `TITULOS_FINAIS` configurável em `config.py`
- Exemplo `exemplos/quimica-titulacao` (laboratório de química com imagens)

### Changed

- Template e README mais genéricos (qualquer disciplina)
- Seções finais deixam de ter numeração fixa no motor

## [1.0.0] - 2026-06-05

### Added

- Motor ABNT genérico (`abnt_engine.py`)
- CLI para gerar DOCX e converter para PDF
- Template `_template` e exemplo `grupo15-jogos`
- Blocos declarativos: parágrafo, quadro, código, figura, subseção
