#!/usr/bin/bash
set -x

(cd markdown;

for f in *.md; do
	notedown $f > ../notebooks/$f.ipynb
done
)

rsync -var python/* notebooks/

find notebooks/ -type f -name \*.py --maxdepth=2 -exec python strip_solutions.py --replace {}

(cd notebooks;
make
)
