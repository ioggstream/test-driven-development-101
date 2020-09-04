# Test Driven Development 101


```python
cd ex-01
```
---


## Goal

  - Identify test scope
  - Code coverage

---

# What to test

So the question: should I write unit test for every function/method?

While you should write unit test for relevant functionalities (eg. public methods, ...)
you should focus on *code coverage* instead.

Code coverage is a measure in percentage used to describe the degree to which
 the source code of a program is executed when a particular test suite runs; 

----

## Code coverage

A code coverage of 75% means that your testsuite executes 75% of the project's code.
An acceptable code coverage starts at 88-90%

Using a code-coverage tool you can ensure that even if you don't wrote
 unittest for all functions, that code is still stressed.
Moreover you can use those tools to identify the uncovered parts,
so that you can add more test cases or discover "dead" code parts.


----

## Code coverage in practice

Let's see [coverage in action](https://pytest-cov.readthedocs.io/en/latest/reporting.html)
on [test_minimal.py](/edit/notebooks/ex-01/test_minimal.py).

```bash
pytest --cov-report term-missing test_minimal.py
```

Mumble: Are there uncovered parts?

----

## Practice

Show the function to test (`maximum`) and its test...

```ipython
%loadpy test_minimal.py
```

Exercise: what can we do to gain 100% text coverage?

