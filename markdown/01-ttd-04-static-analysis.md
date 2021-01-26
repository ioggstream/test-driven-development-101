# Test Driven Development 101


```python
cd ex-01
```
---


## Goal

  - Static analysis & linting

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
- use xmllint to format the file in-place

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

1. git clone https://github.com/caldav4j/caldav4j
2. play with google-java-format on its files

----

## Linting with java

The typical java workflow is to add a linting step (goal) in the project
 descriptor `pom.xml` [see this PR](https://github.com/caldav4j/caldav4j/pull/127/files)
 
```xml

<!-- ... in <plugins> -->
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
```

