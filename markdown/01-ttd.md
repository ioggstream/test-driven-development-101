# Test Driven Development 101



---


## Goal

  - Understand the rationale of TDD

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
%load ex-01/test_minimal.py
```

Use the [terminal](/terminals/1) to run the following command:

```bash
# run pytest with verbose
pytest -v ex-01/test_minimal.py

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
cat ex-01/tox.ini
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

## Static analysis

To increase readability and reduce code variability, an important component
in the development pipeline is static code analysis.

It includes syntax checks, linting and reformatting, identification of
 dangerous patterns like cleartext passwords or clumsy code.

Reformatting code reduces diff size, eases contribution and make easier to
 contribute even for sporadic community members.

----
 
## Linting

Linter rules should be defined in a specific file and should be useful to
 achieve coding goals.
 
Newer languages like Golang come with a linter with a predefined format
, and other languages like python are following using "opinionated" linter
 which reformats code with a very little possibility of customizations.
 
Linting requirements should be part of the project description and be
 checked before the build phase.

----
 
A CI pipeline and the associated pull requests should fail unless
the linter/formatter says it's ok.

We can lint xml and yaml files using proper tools like `xmllint` and `yamllint`.

Exercise: 

- reformat the following code with xmllint

```xml
<a><b foo="bar"
buz="lar"
>ciao</b></a>
``` 

```bash
xmllint --format # complete the command
```

----

## Linting with python

`black` is a linter and formatter for python.
Let's see its configuration in [pyproject.toml](pyproject.toml)

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
  
Example: you can use the `yamllint` tool to 

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

----

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