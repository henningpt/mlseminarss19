ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
endif

all: build/analyse.pdf

# hier Python-Skripte:
build/plot_name.pdf: preprocessing.py header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python analize_ds.py

# hier weitere Abhängigkeiten für build/analyse.pdf deklarieren:
build/analyse.pdf: build/plot_name.pdf

build/analyse.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	analyse.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
