SOURCES=$(wildcard *.md)
NB=$(addprefix ../notebooks/, $(addsuffix .ipynb, $(SOURCES)))
SLIDES=$(addprefix ../slides/, $(addsuffix .slides.html, $(SOURCES)))

../notebooks/%.md.ipynb: %.md
	../mermaid_magic.py $< | notedown > $@


../slides/%.slides.html: ../notebooks/%.ipynb
	jupyter nbconvert  $<  --to slides --output $@


nb: $(NB)
	echo $(NB) $(SLIDES)


clean:
	rm -f $(NB) $(SLIDES)

slides: $(SLIDES)
	echo $(SLIDES)


all: nb slides

