# OpenAPI & Modeling

---

## [OpenAPI](https://www.openapis.org/) is a specification language

OpenAPI is a specification language for REST APIs that allows to communicate:

- technical specifications 

- metadata

- docs & references

----

## OpenAPI is driven by a [Foundation](https://www.openapis.org/)

The OpenAPI Foundation is an initiative under the Linux Foundation, 
participated by government & companies  (gov.uk, Microsoft, Google, Oracle, IBM, ..):

- Driver for API adoption

- Evolution of Swagger 2.0

- Lightweight format: [YAML](https://learnxinyminutes.com/docs/yaml/)

- Generates docs & code via tools ([swagger-editor](https://editor.swagger.io),
  [apicur.io](https://www.apicur.io/))

- Allows reusable components via hyperlink (eg. $ref)

---

## OpenAPI is WSDL for REST APIs

----

## OpenAPI Editor

Every OAS3 document begins with

```
openapi: 3.0.0
```

[Swagger Editor](https://editor.swagger.io/?url=https://raw.githubusercontent.com/teamdigitale/api-starter-kit/master/openapi/simple.yaml.src)
is a simple webapp for editing OpenAPI 3 language specs.

Discuss OAS spec

----

## OAS files compliance

Writing the spec before the code, forces us to think about:

- API usage
- security and data protection
- use cases and examples

----

## OAS files compliance

Lint spec example: the Italian API 
[Online linter](https://teamdigitale.github.io/api-oas-checker?url=https://raw.githubusercontent.com/teamdigitale/api-starter-kit/master/openapi/simple.yaml.src)

Rationale of the use of [Spectral]():

- can be run via command line or via server
- can be web-packed as an in-browser validator
- rules are distributed via a single yaml file

----

## Oas file compliance

We can integrate the linter via SaaS and add it to the Development Pipeline
showing comments.

[See example](https://github.com/teamdigitale/api-starter-kit-python/pull/5/files) 

Exercise: try to make a PR to that repo introducing a valid OAS3 statement
which is not compliant with the ruleset.

---

## OAS & TDD

Defining an OAS file full of examples enables us to test and improve the
 interface.
 
Consider the `maximum` function we wrote in [01-tdd.md.ipynb](01-tdd.md.ipynb)

```python
%loadpy tdd_course/utils.py
```

Let's write an OAS3 specification file based on the one present in the linter
that wraps the `maximum` method.

Write the examples in the input/output starting from the skeleton provided in

```python
%loadpy openapi.skel
```

and save it in `openapi.yaml`

----

Once we have the spec, we can bind them to the actual function `maximum
` via the `operationId` property.

It is done via

```yaml
...
paths:
  /max:
    post:
      operationId: tdd_course.utils.maximum
...
```

Now try running your API in connexion.

```bash
connexion run openapi.yaml --port 9990 --debug
```

----

We can use OAS to generate test data and do some smoking tests, for example.

`schemathesis` is a tool that enable us to do this.

```bash

schemathesis  run http://0.0.0.0:9990/openapi.yaml -c all

```

Schemathesis helps us in refining schemas *after the first implementation*.