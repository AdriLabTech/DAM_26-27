# Compilación del informe con latexmk
#   make compilar   -> genera main.pdf
#   make abrir      -> compila y abre el PDF
#   make limpiar    -> borra los ficheros auxiliares

PDF     := main.pdf
SRC     := main.tex
LATEXMK := latexmk
BUILD   := $(LATEXMK) -pdf -interaction=nonstopmode -file-line-error $(SRC)

.PHONY: all compilar abrir limpiar

all: compilar

compilar:
	$(BUILD)

abrir: compilar
	@xdg-open $(PDF) >/dev/null 2>&1 &

limpiar:
	$(LATEXMK) -C $(SRC)