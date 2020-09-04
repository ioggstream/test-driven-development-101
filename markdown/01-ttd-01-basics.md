# Test Driven Development 101


```python
cd ex-01
```
---


## Goal

  - Understand the rationale of TDD
  - Static analysis & linting

---

# Test Driven Development

  - define and clarify one user requirement
  - write down some examples with the inputs and the expected outputs
  - write the code testing for the expected behavior
  - implement the code

----

## TDD in practice

You need to implement a function that finds the maximum number in a list.

The first step is to *gather examples*.

```python

my_input = [1, 5, 3, 0, 9]
expected_output = 9
```

---- 

Then I write my function, which just throws an exception

```python
def maximum(l: list):
    raise NotImplementedError("Write me") 
```

----

Finally I write the test

```python
def test_maximum(my_input, expected_output):
    assert maximum(my_input) == expected_output
```
and run it

```python
test_maximum(my_input, expected_output)
```

Now I just have to start coding until the test works.

```python
# Implement the `maximum` function here and re-run the test


```

----

## Advantages

- your code will be covered by tests in time
- newcomers can develop without fear of breaking things
- refactors will be safer
- code usability and reusability
- less time spent in debugging
- bugs are isolated easily

=> Faster development

----

## Advantages

Writing tests helps the developer to *think* about **how using the function**
and being in the shoes of the function user.

This improves design significantly!

---

# Running tests

----

## Running tests with python

Let's install on the course machine some python testing packages
 via the `pip3` package manager.

Use the [terminal](/terminals/1) to see the output in real time.

```bash
# Note the --user flag to avoid system-wide installation.
pip3 install pytest black isort yamllint --user
```


## Running tests with python

Here is a minimal python file with a test

```python
%load test_minimal.py
```

Use the [terminal](/terminals/1) to run the following command:

```bash
# run pytest with verbose
pytest -v test_minimal.py

```
----

Exercise: 

 - fix the first test 
 - add one more failing tests

```python
def test_fail():
    assert 1 == 0  # This is supposed to fail
```

----

To run tests in an isolated environment you can use `tox`, which:
- declares the python version
- installs dependencies
- runs pytest

```bash
cat tox.ini
```

We can configure tox to do further stuff, like we do with maven.

Exercise: 

  - run tox in [terminal](/terminals/1)

```bash
tox -v
```

  - brief discussion on tox and pytest

----

## Running tests with java

`maven` provides a goal for running tests and invoke junit.
Let's try with this nice junit5 tutorial repo in a [terminal](/terminals/1)

```bash
git clone https://github.com/junit-team/junit5-workshop
cd junit5-workshop
mvn -e test
```

Exercises:
 - check the relevant parts in pom.xml
 - have a look at the [slides](https://codefx-org.github.io/talk-junit-5/#/_basics)
 
----

## Test Practice

Implement a simple parser in python:

- the program parses [access.log](ex-01/access.log)
- returns the number of occurrencies of an HTTP method (eg. POST, GET, ..)
- use [test_what.py](ex-01/test_what.py) as a stub