#!/usr/bin/bash

(cd markdown;

for f in *.md; do
	notedown $f > ../notebooks/$f.ipynb
done
)

rsync -var python/* notebooks/
