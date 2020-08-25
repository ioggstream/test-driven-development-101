#!/usr/bin/bash
set -x

# Make notebook + slides
(cd markdown; make -j4 all)

rsync -var python/* notebooks/

find notebooks/ -name \*.py -a ! -path '*/.tox/*' -type f  -exec python strip_solutions.py --replace {} \;

