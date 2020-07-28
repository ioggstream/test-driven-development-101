# Test Driven Development API 101

This is a test driven development API course.


## Methodology

The course will teach TDD using a set of SaaS tools like github, circleci, github-actions, ...

## What will I learn

To design and implement a simple HTTP API, testing the interface and the implementation with online tools.

The course is based on the python programming language.


## Prerequisites

A set of SaaS account:

- github
- circleci
- ..

## Tools

- spectral (node/javascript)
- connexion (python)
- ...

# Running the course

## Notebooks

Jupyter notebooks are produced from [markdown](markdown) files.
The following script builds all into the `notebooks` folder.

```
bash -x build.sh 
```

Code is in [python](python) and will be loaded into slides via `%loadpy` jupyter macro.

## Markdown

To play the course, start the reveal-md server and point the browser to the given location.

```
sudo npm install -g reveal-md
reveal-md markdown &
firefox http://localhost:1948/ 

```

