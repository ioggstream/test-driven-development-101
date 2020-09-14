# OpenAPI Implementation

## Goals

  - implement a REST API starting from OAS spec
  
---

# Implementing an API

In this practice we will implement a REST API starting from a template
 repository from github.
 
The steps will be:

  1a. setup a minimal QA framework for the project
  1b. write the OAS spec
  2a. identify the test surface and review the QA framework
  2b. implement the tests 
  3a. identify the deployment strategy and review the QA framework
  3b. implement the code

----  
  Fork the [python-api-test] repository and checkout to the v0 branch.

```bash
git clone https://github.com/$ghuser/python-api-test
cd python-api-test
git checkout -b v0
```

---
 
# QA framework
 
Setup a minimal QA framework:
 
  - readme, license file, template for issues, PR; see the 00-github
   lessons
  
```bash
pytest scripts/test_v0.py -v -k test_v0
```

----

Exercise: 

create a `docker-compose.yml` service running spectral to validate
the OAS we are going to write: openapi/store.yaml

```bash
pytest scripts/test_v0.py -v -k test_v1
# run docker
docker-compose up test-oas
```

----

Exercise:

use [tox.ini](/editor/tox.ini) to check YAML files using yamllint, 
see 01-tdd-04-static-analysis

```bash
grep -A5 ':yamllint' tox.ini
```

To better isolate your environment, use the "test" service in docker-compose:

```bash
docker-compose up test
```

---

# Get API requirements

In [store.yaml#/info/description] you can find the API requirements.

Implement the following operation:

  - post_item: add a json object to the store and assign it an uuid;
  - get_item: retrieve a store object by uuid
  - get_items: list the stored items
  - get_status: test if the service works, it just returns
    `{"status": 200, "title": "Ok"}`

---

# Implement the OAS spec

Complete and test the OAS specification in `openapi/store.yaml`

  - `info` metadata
  - `components.schemas` for all resources
  - identify success and error status codes

Hints:
  * use [editor.swagger.io]
  * validate the fields using the online [api-oas-checker] 
  * examine datatypes

----

Check your spec with docker-compose now!

```bash
docker-compose up test-oas
```

Add to tox another task to check your apis with 

---

# Define the infrastructure

- implement the infrastructure described in the API Documentation
  in docker-compose.yml using the following services:
  
  
- test it in a [terminal]

```bash
# spin it up
docker-compose up -d
# check, consider navigating containers with docker exec
docker-compose ps
# now tear it down
docker-compose down
```

---

# Identify the language to use

In this case we'll use python, but you could use other languages.

Picking a language means:

- define dependency management tool
- validating management (eg. use safety for python or owasp.dependency
.check for java)
- identify container images to run the code
- writing the test pipeline

----





[//]: #  (Riferimenti)
[api-oas-checker]: https://teamdigitale.github.io/api-oas-checker
[python-api-test]: https://github.com/ioggstream/python-api-test
[editor.swagger.io]: https://editor.swagger.io
[terminal]: /terminals/1
[store.yaml]: openapi/store.yaml