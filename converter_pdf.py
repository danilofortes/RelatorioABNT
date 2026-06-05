# -*- coding: utf-8 -*-
"""Converte DOCX em PDF usando Microsoft Word (docx2pdf)."""

import argparse
import os
import sys

from docx2pdf import convert


def main():
    parser = argparse.ArgumentParser(description="Converte relatorio .docx para .pdf")
    parser.add_argument(
        "docx",
        nargs="?",
        default=None,
        help="Arquivo .docx de entrada",
    )
    parser.add_argument(
        "--pdf",
        default=None,
        help="Arquivo .pdf de saida (padrao: mesmo nome do docx)",
    )
    args = parser.parse_args()

    if args.docx is None:
        print("Informe o arquivo .docx ou use apos gerar_relatorio.py", file=sys.stderr)
        sys.exit(1)

    docx_path = os.path.abspath(args.docx)
    if not os.path.isfile(docx_path):
        print(f"Arquivo nao encontrado: {docx_path}", file=sys.stderr)
        sys.exit(1)

    if args.pdf:
        pdf_path = os.path.abspath(args.pdf)
    else:
        pdf_path = os.path.splitext(docx_path)[0] + ".pdf"

    print(f"Convertendo: {docx_path}")
    convert(docx_path, pdf_path)
    print(f"PDF gerado: {pdf_path}")


if __name__ == "__main__":
    main()
