---

# Github basics

----

## Goals

  - Create a github project
  - Basic github project quality
  
## Tools

  - python
  - github, circleci
  
---

# Preparation

  - register on github

---

# Create a GH project

When you create a project you need to provide QA metadata

  - README & LICENSE information
  - Issues & PR template to properly address contributions
  - Project layout
  
----

[This project](https://github.com/ioggstream/test-driven-development)
stores issues and PR templates in [.github](.github).

Here you can find

```bash
tree ../../.github
```

- an [ISSUE_TEMPLATE.md]()
- a [pull_request_template.md]()

Further info on github templates are [here](https://docs.github.com/en/github/building-a-strong-community/using-templates-to-encourage-useful-issues-and-pull-requests)

Exercise:

- create an issue in this project
- create a PR to this project
  
----
# Create a gh project

  - register on github
  - look for a project template
  - create a project from a template

----


## Exercise: create a gh-project
 
 - create a gh template project
 - add minimal information and layout files
 - mark it as a template  
 - create a new project from a template
 
---

# Pipelines

  - Create a pipeline with github actions to validate OAS spec
  - Create a pipeline with circleci to run property based tests

----

## Pipelines with tox and with gh-actions

- writing a pipeline with tox
- validating files with tox
- running spectral from command line
- running spectral with a gh-action

----

## Implementing pipelines manually


Implementing pipelines manually (tox+circleci)

- writing tox
- testing with tox

----

## Testing with CircleCI

- showcase
- subscribing to circleci
- testing with circleci
- circleci + tox

