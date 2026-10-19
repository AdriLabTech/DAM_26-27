#!/usr/bin/env bash
# Compila el informe y avisa de los errores que importan.
set -uo pipefail
cd "$(dirname "$0")"

log=$(mktemp)
if latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex >"$log" 2>&1; then
    echo "OK  -> $(pwd)/main.pdf"
    pdfinfo main.pdf | grep -E '^(Pages|Title|Author)'
else
    echo "FALLO la compilacion. Primeros errores:"
    grep -E '^\./main\.tex:[0-9]+:' "$log" | head -15
    echo "Log completo: /tmp/latex-entorno-movil.log"
    cp "$log" /tmp/latex-entorno-movil.log
    exit 1
fi