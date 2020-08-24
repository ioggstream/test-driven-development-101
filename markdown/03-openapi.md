# OpenAPI & Modeling


---- 

## Goals

 - Designing a minimal API using OAS
 - Using static linters (swagger.editor.io, spectral, ..)
 - Validating spec with tools.
 
---

# Writing Specification

Writing machine readable specification is a great way to prepare
the ground for a testable project.

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

----

## Start with Metadata

In OAS3 we should first describe api metadata, to clarify:

- API goals, audience and context;
- Terms of service;
- Versioning.

Here's a simple OAS3 metadata part, contained in the `info` section.

```
openapi: 3.0.0
info:
  version: "1.0.0"
  title: |-
    Write a short, clear name of your service.
  description: |
    This field may contain the markdown documentation of the api,
    including references to other docs and examples.

  # Legal references and terms of services.
  termsOfService: 'http://swagger.io/terms/'
  contact:
    email: robipolli@gmail.com
    name: Roberto Polli
    url: https://twitter.com/ioggstream
  license:
    name: Apache 2.0
    url: 'http://www.apache.org/licenses/LICENSE-2.0.html'
```

----

Starting from this skeleton file, we will complete an OAS file
using [swagger editor](https://editor.swagger.io).

```yaml
# Complete this file with the required informations
#  using your swagger-editor. You should 
# - fix all the eventual error
# - add the missing parameters
# so that the file become a valid OAS3 spec.
openapi: 3
info:
  version: 0.1
paths: {}
components: {}

```

1- provide contact informations and terms of services

----

In `components.schemas` you can define object schemas. The schema for the
 following object 
 
```json
{
  "given_name": "Leon Battista",
  "family_name": "Alberti",
  "tax_code": "LBRLBT72D25D969F"
}
```

is

```yaml
components:
  schemas:
    Citizen:
      properties:
        given_name:
          type: string
          required: true
          example: Leon Battista
        family_name:
          type: string
          example: Alberti
        tax_code:
          type: string
          pattern: /^[A-Z0-9]{16}/
          example: LBRLBT72D25D969F
```

----

Esercise: define the `ISOTimestamp` schema to represent the following object

```json
{"timestamp":  "2020-01-01T00:00:00Z"}
```

----

Server information can be passed in the `servers` block.

```yaml
servers:
  - description: Development server
    url: https://localhost:8443/datetime/v1
```

----

The `paths` section defines the endpoints for your API.

```yaml
paths:
  /status:
    get:
      summary: Return the application status.
      description: |
        Return the application status. You may want
        to implement this so that it randomically
        returns an error (eg. 429 or 503).
      operationId: api.get_status
      responses:
        '200':
          description: |
            The status is OK.
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/Problem'  # REMOVE ME FOR EXERCISE
         'default':  # WRITEME

```

----

Exercise: describe the `/echo` path:
 
 1- it returns a `200` response
 2- the response media-type is `application/json`
 3- it contains an `ISOTimestamp` object with the current timestamp
 4- in case of error, returns a `Problem` object.
 
---

## OAS files compliance

Writing the spec before the code, forces us to think about:

- API usage
- security and data protection
- use cases and examples

----

## OAS files compliance

Lint spec example: the Italian API validator
[Online linter](https://teamdigitale.github.io/api-oas-checker?url=https://raw.githubusercontent.com/teamdigitale/api-starter-kit/master/openapi/simple.yaml.src)

Rationale of the use of [Spectral linter]():

- can be run via command line or via server
- can be web-packed as an in-browser validator
- rules are distributed via a single yaml file


----

Exercises: 

- use the [Online linter](https://teamdigitale.github.io/api-oas-checker)
  to check the specification you wrote.
- save the spec as `datetime.yaml` and validate them locally with
  the spectral docker image

```bash
docker run --rm -v $PWD:/code stoplight/spectral lint /code/datetime.yaml
```

----

Practice:

- compare `datetime.yaml` to [this one](https://raw.githubusercontent.com/teamdigitale/api-starter-kit/master/openapi/simple.yaml.src)
- add a couple of examples to `datetime.yaml`
- open a [terminal](terminals/1) and run a mock API server

```bash
connexion run datetime.yaml --mock=all & 
```

- now test the endpoint

```bash
curl -v http://localhost/datetime/v1/echo
```
----

## OAS file compliance

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

---

# API Design Workshop

Now we will 

