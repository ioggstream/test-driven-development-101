SOURCES=$(wildcard *.md)
NB=$(addsuffix .ipynb, $(SOURCES))
NB1=$(addprefix ../notebooks/, $(NB))
SLIDES=$(addsuffix .slides.html, $(SOURCES))

../notebooks/%.md.ipynb: %.md
	notedown $<  > $@

%.md.ipynb: %.md
	notedown $(basename $<).md > $@


%.slides.html: %.ipynb
	jupyter nbconvert $< --to slides


nb: $(NB)
	echo $(NB) $(SLIDES)


clean:
	rm -f $(NB) $(SLIDES)

slides: $(SLIDES)
	echo $(SLIDES)


all: slides

nb1: $(NB1)
	echo $(NB1)