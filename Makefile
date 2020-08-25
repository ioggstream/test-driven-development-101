
MARKDOWNDIR = markdown
SHELL := bash

dep:
	npm install -g reveal-md
	pip3 install notedown click astor

build: 
	mkdir -p notebooks
	@for f in $(shell ls ${MARKDOWNDIR}/*.md) ; do \
		notedown $$f > notebooks/$${f/markdown\//}.ipynb ; \
	done
	rsync -var python/* notebooks/
	$(shell find notebooks/ -type f -name \*.py --maxdepth=2 -exec python strip_solutions.py --replace {})


docker:
	docker-compose up -d
	

markdown-dep:
	npm install -g reveal-md

markdown-reveal:
	reveal-md markdown -w &

markdown: markdown-dep markdown-reveal