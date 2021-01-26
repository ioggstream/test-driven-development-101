---
# OAS Design

```python
cd ex-04
```
----

## Goals

- design and implement a simple API with OAS
- use linting and mocking tools

## Tools

- swagger editor, spectral, connexion, python
- github, docker

---

# OAS design practice
 
Let's write `openapi.yaml`, an OAS spec describing an API which:

- receives from the client a list of numbers;
- returns the maximum in the response.

Start from 

```python
%loadpy openapi.skel
```

Hint: use [swagger editor](editor.swagger.io)

----

Providing examples in an OAS file enables us to test and
 improve the interface.

Add some examples in the input/output to the spec.
See [this doc page](https://swagger.io/docs/specification/adding-examples/)
for further info.

----

Exercise:

  - lint the spec with spectral and with 
    [api-oas-checker](teamdigitale.github.io/api-oas-checker)
    
  - use yamllint to cleanup the yaml syntax.
    
  - Mock the server  [in a terminal](/terminals/1) using 
  
```bash
connexion run --mock=all openapi.yaml
```
  
---

# API Mocking

API mocking is important to provide feedback to users during the design
phase.

Using `connexion --mock=all` we allow our consumer (clients) to test
our API design so that we can get feedback and improve before spending
time in the actual development.

Connexion can mock either all methods or only unimplemented methods.

----

[Stoplight Prism] is another framework for mocking APIs.

Prism generates fake data on every response according to the examples
provided in the OAS spec.

See [Prism guide](https://github.com/stoplightio/prism/blob/master/docs/guides/01-mocking.md#Response-Generation)
  
Exercise: run prism on your openapi.yaml using docker

```bash
docker run --rm -v $PWD:/code stoplight/prism mock /code/openapi.yaml
```

Now use the [terminal](/terminal/1) to issue some request.

  
---

## Implementing the API

Implementing an API PoC is very useful for testing the specification.

Python is a convenient language for prototyping and mocking:
let's see how we can use it to 
 bind the spec to a real `maximum` function
 via the `operationId` OAS property.

```yaml
...
paths:
  /maximum:
    post:
      operationId: api.get_maximum
...
```

----

Now implement the `get_maximum()` function using TDD:

- implement `maximum`
- implement `test_get_maximum`
- implement `get_maximum`
- test them:

```bash
pytest -v api.py
```

----

Now run your API in a [terminal](/terminals/1)

```bash
connexion run openapi.yaml --port 9990 --debug
```

```python
from requests import request
url = "http://localhost:5000/openapi.yaml"
# connexion exposes the API spec!
request("GET", url).content
```

And issue some requests using the cell below.

```python
from requests import request
url = "http://localhost:5000/maximum"
data = {"numbers": [1,2,3,4,5]}
r = request("POST", url,  json=data)
r.json()
```

----

---

# Dynamic analysis

We have already introduced Static analysis, which is useful
to check if the code we wrote is syntactically correct or
if it presents some bad patterns.

Dynamic analysis goes a little further and tests the actual
behavior of an application. We can apply this kind of analysis
directly to an API, or we can do it to a complete infrastructure,
eg. to a reverse proxy which may be used to implement features
such as caching, rate-limiting or L7 firewalling.

While in this course we are running Dynamic analysis (aka DAST)
after the development of an application, it is important that
we implement the actual tests beforehand.

There are many tools for DAST: in this course
we will see:

- [schemathesis] which is both a stress tool
  and a library that can be used to programmatically
  write tests;
- [zap-proxy] a tool from OWASP, a cybersecurity foundation, which
  will scan our API using the information provided by its OAS.

The usability of those tools is deeply related to the availability
of the OpenAPI specification: once more we remember the importance
of a contract-firts approach in writing APIs.

## Schemathesis

Tools like [connexion] and [prism] mock the server

other OAS tools like [schemathesis] can mock client and generate test requests

This helps refining schemas *after the first implementation*
and make them secure.

The following command retrieves the OAS specification at a given
URL and creates a bunch of requests, verifying whether the responses
are in the allowed set.

```bash
schemathesis run http://0.0.0.0:9990/openapi.yaml -c all
```

---- 

Exercise:

- use [schemathesis] to check faults in the spec design
- to filter some errors, enable `strict-validation`

```bash
connexion run --strict-validation openapi.yaml
```

- analyze eventual errors and try to fix them in the spec.
  This includes adding required fields or parameters,
  specify array sizes, ...


## OWASP ZAP Proxy

ZAP Proxy is a complete tool capable of performing various tests
on web applications and APIs: see [zap-proxy-oas] for an introduction.

To scan your implemented API with ZAP Proxy you need to either install it
or run it via docker.
The following command will analyze
the API referenced by the given `openapi.json`
using the `openapi` extension


```
docker run \
  -v $PWD:/zap/wrk \
  -w /zap/wrk \
  owasp/zap2docker-weekly \
  zap-api-scan.py \
  -t https://api.example/datetime/v1/openapi.json \
  -f openapi
```

The output will test many possible exploits and checks
the presence of various headers.
In many cases, you might want to adjust the provided headers
using a reverse proxy or a cache (eg. haproxy, varnish, nginx).
 

---

# API Design Workshop

Now we will design an API from scratch using the [python-api-test] repo

[//]: #  (Riferimenti)

[python-api-test]: https://github.com/ioggstream/python-api-test
[schemathesis]: https://github.com/kiwicom/schemathesis
[connexion]: https://github.com/zalando/connexion
[spectral]: https://github.com/stoplight/spectral
[prism]: https://github.com/stoplight/prism
[api-oas-checker]: https://teamdigitale.github.io/api-oas-checker
[zap-proxy-oas]: https://www.zaproxy.org/blog/2017-06-19-scanning-apis-with-zap/