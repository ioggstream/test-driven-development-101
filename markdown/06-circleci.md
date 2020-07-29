# CircleCI

---

## Goals

  - Run minimal tests with CircleCI
  - Run a `job` with CircleCI Local
  - Create a simple `workflow`

---

## Prerequisites

  - github account
  - circleci account
  - docker
  - circleci local
  - subscribing to circleci
- testing with circleci
- circleci + tox

  
---

## Agenda

- CircleCI (and other software)
- Create a minimal test with circleci local
- Testing with multiple containers
- Workflows

---

# CircleCI

CircleCI is an online platform for implementing CI workflows.

Workflows are triggered by repository (eg Github) events (eg. push, PR, issue
 changes)

You can pass context information and the set of commands to be executed.

You can check logs and eventually produce artifacts.

Supports reusable configurations via `Orbs`.

----

A CircleCI configuration file

```yaml
# Add .circleci/config.yml to your repository

version: 2.1
jobs:
  build:
    docker: 
      # the primary container, where your job's commands are run
      - image: circleci/python
    steps:
      - checkout # check out the code in the project directory
      - run: echo "hello world" # run the `echo` command

```

----


