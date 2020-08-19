# Test Driven Development 101



---


## Goal

  - Understand the rationale of TDD

---

# Test Driven Development

1- define and clarify one user requirement

2- write down some examples with the inputs and the expected outputs

3- write the code testing for the expected behavior

4- implement the code

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

`tox` is a python tool that can invoke pytest, a common framework for running
 python tests.
You can find a minimal test file in the python directory

```bash
cd python/
tox -e py37
cd ..
```

Exercise:

- see the example test case `python/tests/test_one.py`
- brief discussion on tox and pytest

----

## Running tests with java

`maven` provides a goal for running tests and invoke junit.
Let's try this nice junit5 tutorial repo!

```bash
git clone https://github.com/junit-team/junit5-workshop
cd junit5-workshop
mvn -e test
cd ..
```

Exercises:
 - check the relevant parts in pom.xml
 - have a look at the [slides](https://codefx-org.github.io/talk-junit-5/#/_basics)
 
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
Moreover you can use those tools to identify the uncovered parts, so that you can add more test cases or discover "dead" code parts.


----

## Code coverage in practice

Let's see [coverage in action](/notebooks/notebooks/01-ttd.md.ipynb#Code-coverage-in-practice).

```ipython

!PYTHONPATH=$PWD pytest --cov=tdd_course tests/

```

Mumble: there are uncovered parts...

----

## Practice

Show the function to test

```ipython
%loadpy tdd_course/utils.py
```

And the test case

```ipython
%loadpy tests/test_one.py
```

Exercise: what can we do to gain 100% text coverage?


---

# Code quality

Product quality is based on automatized processes and synchronized practices.
Once upon a time all that work was done in synchronous meetings, with a long
trail of discussions and blaming in case of issues.

Automation reduces the space for discussions and just applies a set of
 validation rules to human (and non/human) production.
This has many  positive effects as it allows to apply continuous and
 gradual changes, and avoids discussions. 
Newcomers will eventually learn faster all development standards. 

----

## Linting

To increase readability and reduce code variability, an important component
in the development pipeline is linting and reformatting.

Reformatting code reduces diff size, eases contribution and make easier to
 contribute even for sporadic community members.

----
 
## Linting

Linter rules should be defined in a specific file and should be useful to
 achieve coding goals.
 
Newer languages like Golang come with a linter with a predefined format
, and other languages like python are following using "opinionated" linter
 which reformats code with a very little possibility of customizations.
 
Linting instruction should be in the pipeline and pull requests should fail
 unless the linter/formatter says it's ok.

----
 
## Linting with python

Let's see `black` configuration in [pyproject.toml](pyproject.toml)

```python
!cat pyproject.toml

```

Further formatting can be done, eg:

- remove unused dependencies
- sort dependencies
- ...

----

## Linting metadata files

While linting code is quite useful, we can do something more: lint software
 configuration and metadata file.
 
Linting metadata files allow us to check if all the compliance rules for
 the project are set up, eg. we can check if `pyproject.toml` is correctly
  configured or if the linter is called by the pipeline.
  
----

## Linting metadata files

A python tool for implementing a CI  is `tox` which is
 configured via `tox.ini`. 

Tox is simpler than maven, as packaging information are outside (in
 pyproject.toml or in requirements.txt).
 
```python
!cat tox.ini
```

Meta-linting can be very useful to ensure uniformity on catalogs, even
 software catalogs.

Specifications, pipeline and linting languages are thus very important.

---

## Linting with java

A linting and autoformatting tool for java is
[google-java-format](https://github.com/google/google-java-format)


```bash
java -jar /path/to/google-java-format-1.8-all-deps.jar --set-exit-if-changed 
```

Exercise:
1- git clone https://github.com/caldav4j/caldav4j
2- play with google-java-format on its files

## Linting with java

The typical java workflow is to add a linting step (goal) in the project
 descriptor `pom.xml` [see this PR](https://github.com/caldav4j/caldav4j/pull/127/files)
 
```xml
... in <plugins>
      <plugin>
        <groupId>com.diffplug.spotless</groupId>
        <artifactId>spotless-maven-plugin</artifactId>
        <version>2.0.2</version>
        <configuration>
          <java>
            <!-- apply a specific flavor of google-java-format -->
            <googleJavaFormat>
              <version>1.8</version>
              <style>AOSP</style>
            </googleJavaFormat>
          </java>
        </configuration>
      </plugin>
...
```