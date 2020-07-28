SOURCES=$(wildcard markdown/*.md)
NB=$(SOURCES:.md=.md.ipynb)

notebooks: $(NB)

%.md.ipynb: %.md
	notedown $< > $@
	
slide:
	jupyter nbconvert notebooks/*.ipynb --to slides --post serve
