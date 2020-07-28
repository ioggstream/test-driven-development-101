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

Lint spec example: the Italian API  [Online linter](https://teamdigitale.github.io/api-oas-checker?url=https://raw.githubusercontent.com/teamdigitale/api-starter-kit/master/openapi/simple.yaml.src)

Rationale of the use of [Spectral]():

- can be run via command line or via server
- can be web-packed as an in-browser validator
- rules are distributed via a single yaml file

----

## Oas file compliance

We can integrate the linter via SaaS and add it to the Development Pipeline
showing comments.

[See example](https://github.com/teamdigitale/api-starter-kit-python/pull/5
/files) 

Exercise: try to make a PR to that repo introducing a valid OAS3 statement
which is not compliant with the ruleset.