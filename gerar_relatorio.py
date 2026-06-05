# -*- coding: utf-8 -*-
"""
Gera relatorio ABNT em DOCX a partir de config.py e conteudo.py de um projeto.

Uso:
    python gerar_relatorio.py --projeto exemplos/grupo15-jogos
    python gerar_relatorio.py --projeto ../grupo15-jogos
"""

import argparse
import importlib.util
import os
import sys

from abnt_engine import gerar_documento


def carregar_modulo(caminho, nome):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    if spec is None or spec.loader is None:
        raise ImportError(f"Nao foi possivel carregar: {caminho}")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def resolver_caminhos(projeto_arg):
    base = os.path.dirname(os.path.abspath(__file__))

    if projeto_arg:
        projeto_dir = os.path.abspath(projeto_arg)
        if not os.path.isabs(projeto_arg):
            candidato = os.path.join(base, projeto_arg)
            if os.path.isdir(candidato):
                projeto_dir = candidato
    else:
        projeto_dir = os.getcwd()

    config_path = os.path.join(projeto_dir, "config.py")
    conteudo_path = os.path.join(projeto_dir, "conteudo.py")

    if not os.path.isfile(config_path):
        raise FileNotFoundError(
            f"config.py nao encontrado em {projeto_dir}. "
            "Copie exemplos/_template ou exemplos/grupo15-jogos."
        )
    if not os.path.isfile(conteudo_path):
        raise FileNotFoundError(
            f"conteudo.py nao encontrado em {projeto_dir}."
        )

    return projeto_dir, config_path, conteudo_path


def main():
    parser = argparse.ArgumentParser(
        description="Gera relatorio ABNT (.docx) a partir de config.py e conteudo.py"
    )
    parser.add_argument(
        "--projeto",
        default=".",
        help="Pasta do projeto com config.py e conteudo.py (padrao: pasta atual)",
    )
    parser.add_argument(
        "--saida",
        default=None,
        help="Caminho do .docx de saida (padrao: arquivo_saida do config.py)",
    )
    args = parser.parse_args()

    projeto_dir, config_path, conteudo_path = resolver_caminhos(args.projeto)

    config = carregar_modulo(config_path, "config")
    conteudo = carregar_modulo(conteudo_path, "conteudo")

    meta = config.METADADOS
    sumario = config.SUMARIO
    secoes = conteudo.SECOES
    consideracoes = conteudo.CONSIDERACOES
    referencias = conteudo.REFERENCIAS
    titulos_finais = getattr(config, "TITULOS_FINAIS", None)

    doc = gerar_documento(
        meta,
        sumario,
        secoes,
        consideracoes,
        referencias,
        projeto_dir=projeto_dir,
        titulos_finais=titulos_finais,
    )

    nome_saida = args.saida or meta.get("arquivo_saida", "Relatorio.docx")
    if not os.path.isabs(nome_saida):
        out_path = os.path.join(projeto_dir, nome_saida)
    else:
        out_path = nome_saida

    doc.save(out_path)
    print(f"Relatorio gerado: {out_path}")
    return out_path


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        sys.exit(1)
